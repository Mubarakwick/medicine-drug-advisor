import os
import numpy as np
from typing import List, Dict, Any
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MedicineVectorDB:
    def __init__(self, embedding_model_name: str = "all-MiniLM-L6-v2"):
        self.embedding_model = SentenceTransformer(embedding_model_name)
        self.dimension = 384  # Dimension for all-MiniLM-L6-v2
        self.index = None
        self.documents = []
        self.metadata = []
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        
    def create_index(self):
        """Create a new FAISS index"""
        self.index = faiss.IndexFlatL2(self.dimension)
        logger.info(f"Created FAISS index with dimension {self.dimension}")
        
    def add_documents(self, documents: List[Dict[str, Any]]):
        """Add documents to the vector database"""
        if self.index is None:
            self.create_index()
            
        for doc in documents:
            # Split document into chunks
            text = doc.get('content', '')
            chunks = self.text_splitter.split_text(text)
            
            for i, chunk in enumerate(chunks):
                # Create embedding
                embedding = self.embedding_model.encode([chunk])[0]
                
                # Add to index
                self.index.add(np.array([embedding], dtype=np.float32))
                
                # Store document and metadata
                self.documents.append(chunk)
                self.metadata.append({
                    'drug_name': doc.get('drug_name', ''),
                    'source': doc.get('source', ''),
                    'section': doc.get('section', ''),
                    'chunk_id': i,
                    'total_chunks': len(chunks)
                })
                
        logger.info(f"Added {len(documents)} documents to vector database")
        
    def search(self, query: str, k: int = 5) -> List[Dict[str, Any]]:
        """Search for similar documents"""
        if self.index is None or self.index.ntotal == 0:
            logger.warning("Vector database is empty")
            return []
            
        # Create query embedding
        query_embedding = self.embedding_model.encode([query])[0]
        
        # Search in FAISS
        distances, indices = self.index.search(
            np.array([query_embedding], dtype=np.float32), k
        )
        
        # Prepare results
        results = []
        for i, idx in enumerate(indices[0]):
            if idx != -1:  # Valid result
                results.append({
                    'content': self.documents[idx],
                    'metadata': self.metadata[idx],
                    'distance': float(distances[0][i])
                })
                
        return results
        
    def save(self, path: str):
        """Save the vector database to disk"""
        os.makedirs(os.path.dirname(path), exist_ok=True)
        
        # Save FAISS index
        faiss.write_index(self.index, f"{path}.index")
        
        # Save documents and metadata
        with open(f"{path}.pkl", 'wb') as f:
            pickle.dump({
                'documents': self.documents,
                'metadata': self.metadata
            }, f)
            
        logger.info(f"Saved vector database to {path}")
        
    def load(self, path: str):
        """Load the vector database from disk"""
        # Load FAISS index
        self.index = faiss.read_index(f"{path}.index")
        
        # Load documents and metadata
        with open(f"{path}.pkl", 'rb') as f:
            data = pickle.load(f)
            self.documents = data['documents']
            self.metadata = data['metadata']
            
        logger.info(f"Loaded vector database from {path}")
        
    def get_stats(self) -> Dict[str, Any]:
        """Get statistics about the vector database"""
        return {
            'total_documents': len(self.documents),
            'total_vectors': self.index.ntotal if self.index else 0,
            'dimension': self.dimension,
            'unique_drugs': len(set(m['drug_name'] for m in self.metadata))
        }