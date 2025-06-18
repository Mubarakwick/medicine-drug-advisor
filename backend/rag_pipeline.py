import os
from typing import List, Dict, Any, Optional
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage, HumanMessage
from langchain.callbacks import StreamingStdOutCallbackHandler
import logging
from dotenv import load_dotenv
from vector_db import MedicineVectorDB
from data_fetcher import FDADataFetcher

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MedicineRAGPipeline:
    def __init__(self, vector_db_path: str = "./data/vector_db"):
        self.vector_db = MedicineVectorDB()
        self.vector_db_path = vector_db_path
        self.data_fetcher = FDADataFetcher()
        
        # Initialize LLM
        self.llm = ChatOpenAI(
            temperature=0.1,
            model_name="gpt-3.5-turbo",
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            streaming=True,
            callbacks=[StreamingStdOutCallbackHandler()]
        )
        
        # Load vector database if exists
        if os.path.exists(f"{vector_db_path}.index"):
            self.vector_db.load(vector_db_path)
            logger.info("Loaded existing vector database")
        else:
            logger.info("No existing vector database found")
            
    def classify_query(self, query: str) -> Dict[str, Any]:
        """Classify the user query to determine intent and extract drug names"""
        classification_prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content="""You are a medical query classifier. 
            Analyze the user query and:
            1. Extract all drug/medicine names mentioned
            2. Classify the query type: interaction, side_effects, usage, dosage, warnings, or general
            3. Return a JSON response with: {"drugs": [...], "query_type": "..."}
            """),
            HumanMessage(content=query)
        ])
        
        response = self.llm.invoke(classification_prompt.format_messages())
        
        # Parse response (simplified - in production, use proper JSON parsing)
        try:
            import json
            content = response.content
            # Extract JSON from response
            start = content.find('{')
            end = content.rfind('}') + 1
            if start != -1 and end != 0:
                classification = json.loads(content[start:end])
            else:
                classification = {"drugs": [], "query_type": "general"}
        except:
            classification = {"drugs": [], "query_type": "general"}
            
        return classification
        
    def retrieve_context(self, query: str, drugs: List[str], k: int = 5) -> List[Dict[str, Any]]:
        """Retrieve relevant context from vector database"""
        # Search for query
        results = self.vector_db.search(query, k=k)
        
        # Also search for each drug mentioned
        for drug in drugs:
            drug_results = self.vector_db.search(drug, k=3)
            results.extend(drug_results)
            
        # Deduplicate and sort by relevance
        seen = set()
        unique_results = []
        for r in results:
            content_hash = hash(r['content'])
            if content_hash not in seen:
                seen.add(content_hash)
                unique_results.append(r)
                
        return unique_results[:k]
        
    def generate_response(self, query: str, context: List[Dict[str, Any]], 
                         query_type: str) -> str:
        """Generate response using LLM with retrieved context"""
        
        # Prepare context string
        context_str = "\n\n".join([
            f"Source: {doc['metadata']['source']} - {doc['metadata']['section']}\n{doc['content']}"
            for doc in context
        ])
        
        # Create prompt based on query type
        prompts = {
            "interaction": """You are a medical assistant AI helping with drug interaction queries.
            
Context from FDA and medical databases:
{context}

User Query: {query}

Provide a clear, helpful response about drug interactions. Include:
1. Whether the drugs can be taken together
2. Any known interactions or warnings
3. Common precautions
4. A reminder to consult healthcare providers

Keep the response concise and easy to understand.""",
            
            "side_effects": """You are a medical assistant AI helping with medication side effects.
            
Context from FDA and medical databases:
{context}

User Query: {query}

Provide information about side effects including:
1. Common side effects
2. Serious side effects that require immediate attention
3. How to manage minor side effects
4. When to contact a healthcare provider""",
            
            "usage": """You are a medical assistant AI explaining medication usage.
            
Context from FDA and medical databases:
{context}

User Query: {query}

Explain:
1. What the medication is used for
2. How it works
3. Common conditions it treats
4. Any important usage information""",
            
            "dosage": """You are a medical assistant AI providing dosage information.
            
Context from FDA and medical databases:
{context}

User Query: {query}

Provide:
1. General dosage guidelines
2. Important timing information
3. What to do if a dose is missed
4. Reminder that specific dosage should be determined by healthcare provider""",
            
            "general": """You are a medical assistant AI.
            
Context from FDA and medical databases:
{context}

User Query: {query}

Provide a helpful, accurate response based on the available information. Always remind users to consult healthcare professionals for personalized advice."""
        }
        
        prompt_template = prompts.get(query_type, prompts["general"])
        
        prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content=prompt_template.format(context=context_str, query=query)),
            HumanMessage(content="Please provide a response.")
        ])
        
        response = self.llm.invoke(prompt.format_messages())
        return response.content
        
    def process_query(self, query: str) -> Dict[str, Any]:
        """Main pipeline to process user queries"""
        logger.info(f"Processing query: {query}")
        
        # Step 1: Classify query
        classification = self.classify_query(query)
        drugs = classification.get('drugs', [])
        query_type = classification.get('query_type', 'general')
        
        logger.info(f"Identified drugs: {drugs}, Query type: {query_type}")
        
        # Step 2: Retrieve context
        context = self.retrieve_context(query, drugs)
        
        # Step 3: Generate response
        if context:
            response = self.generate_response(query, context, query_type)
        else:
            response = self._generate_no_data_response(query, drugs)
            
        return {
            'query': query,
            'drugs_identified': drugs,
            'query_type': query_type,
            'response': response,
            'sources_used': len(context)
        }
        
    def _generate_no_data_response(self, query: str, drugs: List[str]) -> str:
        """Generate response when no data is found"""
        drug_names = ", ".join(drugs) if drugs else "the requested medications"
        return f"""I don't have sufficient information about {drug_names} in my database to answer your question confidently.

For accurate and up-to-date information, please:
1. Consult your healthcare provider or pharmacist
2. Check the medication package insert
3. Visit official sources like FDA.gov or MedlinePlus.gov

Your health and safety are important, so always verify medication information with qualified professionals."""
        
    def initialize_database(self):
        """Initialize the vector database with common drug data"""
        logger.info("Initializing vector database with FDA data...")
        
        # Fetch common drugs data
        drugs_data = self.data_fetcher.fetch_common_drugs_data()
        
        # Convert to documents
        all_documents = []
        for drug_data in drugs_data:
            documents = self.data_fetcher.create_document_for_vectordb(drug_data)
            all_documents.extend(documents)
            
        # Add to vector database
        if all_documents:
            self.vector_db.add_documents(all_documents)
            self.vector_db.save(self.vector_db_path)
            logger.info(f"Initialized database with {len(all_documents)} documents")
        else:
            logger.warning("No documents to add to database")
            
    def check_drug_interaction(self, drug1: str, drug2: str) -> Dict[str, Any]:
        """Check for specific drug-drug interactions"""
        # First try RxNorm API
        interaction_data = self.data_fetcher.get_drug_interactions(drug1, drug2)
        
        # Also search vector database for interaction information
        query = f"{drug1} {drug2} interaction"
        context = self.retrieve_context(query, [drug1, drug2], k=10)
        
        # Generate comprehensive response
        if interaction_data['status'] == 'success' or context:
            response = self.generate_response(
                f"Can I take {drug1} with {drug2}?",
                context,
                "interaction"
            )
            
            return {
                'drug1': drug1,
                'drug2': drug2,
                'interaction_found': interaction_data.get('interaction_found', False),
                'interactions': interaction_data.get('interactions', []),
                'response': response,
                'sources': ['RxNorm', 'FDA Labels']
            }
        else:
            return {
                'drug1': drug1,
                'drug2': drug2,
                'interaction_found': False,
                'response': self._generate_no_data_response(
                    f"interaction between {drug1} and {drug2}",
                    [drug1, drug2]
                ),
                'sources': []
            }