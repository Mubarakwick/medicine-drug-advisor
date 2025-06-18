import requests
import logging
from typing import List, Dict, Any, Optional
import time
from datetime import datetime
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FDADataFetcher:
    def __init__(self):
        self.base_url = "https://api.fda.gov/drug"
        self.rxnorm_base_url = "https://rxnav.nlm.nih.gov/REST"
        self.session = requests.Session()
        
    def search_drug_label(self, drug_name: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search FDA drug labels for a specific drug"""
        try:
            url = f"{self.base_url}/label.json"
            params = {
                'search': f'openfda.brand_name:"{drug_name}" OR openfda.generic_name:"{drug_name}"',
                'limit': limit
            }
            
            response = self.session.get(url, params=params)
            
            if response.status_code == 200:
                data = response.json()
                results = []
                
                for result in data.get('results', []):
                    processed = self._process_label_result(result, drug_name)
                    if processed:
                        results.append(processed)
                        
                logger.info(f"Found {len(results)} results for {drug_name}")
                return results
            else:
                logger.error(f"FDA API error: {response.status_code}")
                return []
                
        except Exception as e:
            logger.error(f"Error fetching FDA data: {str(e)}")
            return []
            
    def _process_label_result(self, result: Dict[str, Any], drug_name: str) -> Optional[Dict[str, Any]]:
        """Process a single FDA label result"""
        try:
            # Extract relevant sections
            sections = {
                'indications_and_usage': result.get('indications_and_usage', [''])[0],
                'contraindications': result.get('contraindications', [''])[0],
                'warnings_and_precautions': result.get('warnings_and_precautions', [''])[0],
                'adverse_reactions': result.get('adverse_reactions', [''])[0],
                'drug_interactions': result.get('drug_interactions', [''])[0],
                'dosage_and_administration': result.get('dosage_and_administration', [''])[0],
                'description': result.get('description', [''])[0],
            }
            
            # Get drug names
            openfda = result.get('openfda', {})
            brand_names = openfda.get('brand_name', [])
            generic_names = openfda.get('generic_name', [])
            
            return {
                'drug_name': drug_name,
                'brand_names': brand_names,
                'generic_names': generic_names,
                'sections': sections,
                'source': 'FDA',
                'last_updated': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Error processing label result: {str(e)}")
            return None
            
    def get_drug_interactions(self, drug1: str, drug2: str) -> Dict[str, Any]:
        """Check for interactions between two drugs using RxNorm"""
        try:
            # First, get RxCUI for both drugs
            rxcui1 = self._get_rxcui(drug1)
            rxcui2 = self._get_rxcui(drug2)
            
            if not rxcui1 or not rxcui2:
                return {
                    'status': 'error',
                    'message': 'Could not find one or both drugs in RxNorm database'
                }
                
            # Check for interactions
            url = f"{self.rxnorm_base_url}/interaction/interaction.json"
            params = {
                'rxcui': rxcui1,
                'sources': 'DrugBank'
            }
            
            response = self.session.get(url, params=params)
            
            if response.status_code == 200:
                data = response.json()
                interactions = []
                
                # Look for interactions with the second drug
                interaction_groups = data.get('interactionTypeGroup', [])
                for group in interaction_groups:
                    for interaction_type in group.get('interactionType', []):
                        for pair in interaction_type.get('interactionPair', []):
                            concepts = pair.get('interactionConcept', [])
                            for concept in concepts:
                                if rxcui2 in str(concept.get('minConceptItem', {}).get('rxcui', '')):
                                    interactions.append({
                                        'description': pair.get('description', ''),
                                        'severity': pair.get('severity', 'Unknown')
                                    })
                                    
                return {
                    'status': 'success',
                    'drug1': drug1,
                    'drug2': drug2,
                    'interactions': interactions,
                    'interaction_found': len(interactions) > 0
                }
                
        except Exception as e:
            logger.error(f"Error checking drug interactions: {str(e)}")
            return {
                'status': 'error',
                'message': str(e)
            }
            
    def _get_rxcui(self, drug_name: str) -> Optional[str]:
        """Get RxCUI identifier for a drug name"""
        try:
            url = f"{self.rxnorm_base_url}/rxcui.json"
            params = {'name': drug_name}
            
            response = self.session.get(url, params=params)
            
            if response.status_code == 200:
                data = response.json()
                id_group = data.get('idGroup', {})
                rxnorm_id = id_group.get('rxnormId', [])
                
                if rxnorm_id:
                    return rxnorm_id[0]
                    
        except Exception as e:
            logger.error(f"Error getting RxCUI: {str(e)}")
            
        return None
        
    def fetch_common_drugs_data(self) -> List[Dict[str, Any]]:
        """Fetch data for a list of common drugs"""
        common_drugs = [
            "ibuprofen", "acetaminophen", "amoxicillin", "metformin",
            "lisinopril", "levothyroxine", "amlodipine", "metoprolol",
            "omeprazole", "losartan", "gabapentin", "sertraline",
            "simvastatin", "montelukast", "fluoxetine", "alprazolam",
            "prednisone", "tramadol", "furosemide", "pantoprazole"
        ]
        
        all_results = []
        
        for drug in common_drugs:
            logger.info(f"Fetching data for {drug}...")
            results = self.search_drug_label(drug, limit=1)
            if results:
                all_results.extend(results)
            time.sleep(0.5)  # Rate limiting
            
        return all_results
        
    def create_document_for_vectordb(self, drug_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Convert FDA drug data into documents for vector database"""
        documents = []
        drug_name = drug_data['drug_name']
        
        for section_name, content in drug_data['sections'].items():
            if content and len(content) > 50:  # Skip empty or very short sections
                documents.append({
                    'drug_name': drug_name,
                    'content': f"Drug: {drug_name}\nSection: {section_name.replace('_', ' ').title()}\n\n{content}",
                    'source': 'FDA',
                    'section': section_name
                })
                
        return documents