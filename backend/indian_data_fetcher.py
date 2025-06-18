import requests
import pandas as pd
import json
import logging
from typing import List, Dict, Any, Optional
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class IndianMedicineDataFetcher:
    """Fetcher for Indian medicine data from various sources"""
    
    def __init__(self):
        self.myupchar_base_url = "https://beta.myupchar.com/api/medicine"
        self.session = requests.Session()
        
    def search_myupchar(self, medicine_name: str, api_key: str = None) -> List[Dict[str, Any]]:
        """
        Search Indian medicines using MyUpchar API
        Returns medicines with real-time pricing
        """
        if not api_key:
            logger.warning("MyUpchar API key not provided. Register at myupchar.com")
            return []
            
        try:
            url = f"{self.myupchar_base_url}/search"
            params = {
                'api_key': api_key,
                'name': medicine_name,
                'type': 'allopathic',  # Options: allopathic, ayurvedic, homeopathic
                'page': 1
            }
            
            response = self.session.get(url, params=params)
            
            if response.status_code == 200:
                data = response.json()
                results = []
                
                for medicine in data.get('medicines', []):
                    results.append({
                        'name': medicine.get('name'),
                        'manufacturer': medicine.get('manufacturer'),
                        'price': medicine.get('price'),
                        'composition': medicine.get('composition'),
                        'type': medicine.get('type'),
                        'source': 'MyUpchar'
                    })
                    
                logger.info(f"Found {len(results)} results from MyUpchar")
                return results
            else:
                logger.error(f"MyUpchar API error: {response.status_code}")
                return []
                
        except Exception as e:
            logger.error(f"Error fetching MyUpchar data: {str(e)}")
            return []
            
    def load_kaggle_dataset(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Load Indian medicine data from Kaggle dataset
        Dataset: https://www.kaggle.com/datasets/mohneesh7/indian-medicine-data
        """
        try:
            # Load CSV file
            df = pd.read_csv(file_path)
            
            # Convert to list of dictionaries
            medicines = []
            for _, row in df.iterrows():
                medicines.append({
                    'name': row.get('name', ''),
                    'manufacturer': row.get('manufacturer', ''),
                    'composition': row.get('composition', ''),
                    'uses': row.get('uses', ''),
                    'side_effects': row.get('side_effects', ''),
                    'price': row.get('price', ''),
                    'source': 'Kaggle Indian Medicine Dataset'
                })
                
            logger.info(f"Loaded {len(medicines)} medicines from Kaggle dataset")
            return medicines
            
        except Exception as e:
            logger.error(f"Error loading Kaggle dataset: {str(e)}")
            return []
            
    def load_github_dataset(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Load Indian medicine data from GitHub dataset
        Dataset: https://github.com/junioralive/Indian-Medicine-Dataset
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                
            medicines = []
            for medicine in data:
                medicines.append({
                    'name': medicine.get('brand_name', ''),
                    'generic_name': medicine.get('generic_name', ''),
                    'manufacturer': medicine.get('manufacturer', ''),
                    'composition': medicine.get('composition', ''),
                    'category': medicine.get('category', ''),
                    'price': medicine.get('price', ''),
                    'source': 'GitHub Indian Medicine Dataset'
                })
                
            logger.info(f"Loaded {len(medicines)} medicines from GitHub dataset")
            return medicines
            
        except Exception as e:
            logger.error(f"Error loading GitHub dataset: {str(e)}")
            return []
            
    def create_documents_for_vectordb(self, medicine_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Convert Indian medicine data into documents for vector database"""
        documents = []
        
        # Create comprehensive document
        content_parts = [
            f"Medicine: {medicine_data.get('name', '')}",
            f"Manufacturer: {medicine_data.get('manufacturer', '')}",
            f"Composition: {medicine_data.get('composition', '')}",
        ]
        
        if medicine_data.get('uses'):
            content_parts.append(f"Uses: {medicine_data.get('uses')}")
            
        if medicine_data.get('side_effects'):
            content_parts.append(f"Side Effects: {medicine_data.get('side_effects')}")
            
        if medicine_data.get('price'):
            content_parts.append(f"Price: ₹{medicine_data.get('price')}")
            
        documents.append({
            'drug_name': medicine_data.get('name', ''),
            'content': '\n'.join(content_parts),
            'source': medicine_data.get('source', 'Indian Medicine Database'),
            'section': 'complete_info'
        })
        
        # Create separate documents for searchability
        if medicine_data.get('uses'):
            documents.append({
                'drug_name': medicine_data.get('name', ''),
                'content': f"Medicine: {medicine_data.get('name')}\nUses: {medicine_data.get('uses')}",
                'source': medicine_data.get('source', 'Indian Medicine Database'),
                'section': 'uses'
            })
            
        if medicine_data.get('side_effects'):
            documents.append({
                'drug_name': medicine_data.get('name', ''),
                'content': f"Medicine: {medicine_data.get('name')}\nSide Effects: {medicine_data.get('side_effects')}",
                'source': medicine_data.get('source', 'Indian Medicine Database'),
                'section': 'side_effects'
            })
            
        return documents
        
    def fetch_ayush_data(self) -> List[Dict[str, Any]]:
        """
        Fetch data from government AYUSH sources
        Note: This is a placeholder - actual implementation would depend on
        available AYUSH APIs or datasets
        """
        # Common Ayurvedic medicines for demo
        ayurvedic_medicines = [
            {
                'name': 'Ashwagandha',
                'type': 'Ayurvedic',
                'uses': 'Stress relief, immunity booster, general wellness',
                'side_effects': 'May cause drowsiness, stomach upset in some people',
                'composition': 'Withania somnifera root extract',
                'source': 'AYUSH'
            },
            {
                'name': 'Triphala',
                'type': 'Ayurvedic',
                'uses': 'Digestive health, detoxification, constipation relief',
                'side_effects': 'May cause diarrhea if taken in excess',
                'composition': 'Amalaki, Bibhitaki, Haritaki',
                'source': 'AYUSH'
            },
            {
                'name': 'Tulsi (Holy Basil)',
                'type': 'Ayurvedic',
                'uses': 'Respiratory health, immunity, stress management',
                'side_effects': 'Generally safe, may interact with blood thinners',
                'composition': 'Ocimum sanctum leaf extract',
                'source': 'AYUSH'
            }
        ]
        
        return ayurvedic_medicines