from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import logging
from comprehensive_drug_database import COMPREHENSIVE_DRUG_DATABASE
import difflib

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Medicine & Drug Interaction Advisor API - Enhanced", version="2.0.0")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response models
class QueryRequest(BaseModel):
    query: str
    
class DrugInteractionRequest(BaseModel):
    drug1: str
    drug2: str
    
class SearchRequest(BaseModel):
    query: str
    category: Optional[str] = None
    
class QueryResponse(BaseModel):
    query: str
    drugs_identified: List[str]
    query_type: str
    response: str
    sources_used: int
    drug_details: Optional[Dict[str, Any]] = None
    
class DrugInteractionResponse(BaseModel):
    drug1: str
    drug2: str
    interaction_found: bool
    interactions: List[Dict[str, Any]]
    response: str
    sources: List[str]

# Helper functions
def find_drug_by_name(drug_name: str) -> Optional[tuple[str, Dict[str, Any]]]:
    """Find drug in database by generic or brand name"""
    drug_name_lower = drug_name.lower().strip()
    
    # First try exact match
    if drug_name_lower in COMPREHENSIVE_DRUG_DATABASE:
        return drug_name_lower, COMPREHENSIVE_DRUG_DATABASE[drug_name_lower]
    
    # Then try brand names
    for generic_name, drug_info in COMPREHENSIVE_DRUG_DATABASE.items():
        brand_names_lower = [b.lower() for b in drug_info['brand_names']]
        if drug_name_lower in brand_names_lower:
            return generic_name, drug_info
            
    # Try fuzzy matching
    all_names = list(COMPREHENSIVE_DRUG_DATABASE.keys())
    for drug in COMPREHENSIVE_DRUG_DATABASE.values():
        all_names.extend([b.lower() for b in drug['brand_names']])
    
    matches = difflib.get_close_matches(drug_name_lower, all_names, n=1, cutoff=0.8)
    if matches:
        matched_name = matches[0]
        # Find which drug this belongs to
        for generic_name, drug_info in COMPREHENSIVE_DRUG_DATABASE.items():
            if generic_name == matched_name or matched_name in [b.lower() for b in drug_info['brand_names']]:
                return generic_name, drug_info
    
    return None

def check_drug_interaction(drug1_name: str, drug2_name: str) -> Dict[str, Any]:
    """Check for interactions between two drugs"""
    drug1_data = find_drug_by_name(drug1_name)
    drug2_data = find_drug_by_name(drug2_name)
    
    if not drug1_data or not drug2_data:
        return {
            "interaction_found": False,
            "response": f"Could not find complete information for one or both drugs. Please verify drug names.",
            "drug1_found": drug1_data is not None,
            "drug2_found": drug2_data is not None
        }
    
    drug1_generic, drug1_info = drug1_data
    drug2_generic, drug2_info = drug2_data
    
    # Check if drug2 is in drug1's interactions
    interactions_found = []
    
    for interaction in drug1_info.get('interactions', []):
        if drug2_generic in interaction.lower() or any(brand.lower() in interaction.lower() for brand in drug2_info['brand_names']):
            interactions_found.append({
                "type": "direct",
                "description": f"{drug1_info['generic_name']} may interact with {drug2_info['generic_name']}"
            })
    
    # Check category-based interactions
    if drug1_info['category'] == 'Benzodiazepine' and drug2_info['category'] == 'Benzodiazepine':
        interactions_found.append({
            "type": "category",
            "description": "Using multiple benzodiazepines increases risk of excessive sedation and respiratory depression"
        })
    
    if ('SSRI' in drug1_info['category'] and 'NSAID' in drug2_info['category']) or \
       ('NSAID' in drug1_info['category'] and 'SSRI' in drug2_info['category']):
        interactions_found.append({
            "type": "category",
            "description": "SSRIs with NSAIDs may increase risk of bleeding"
        })
    
    # Check for duplicate active ingredients
    if drug1_generic == drug2_generic:
        interactions_found.append({
            "type": "duplicate",
            "description": "Same active ingredient - risk of overdose"
        })
    
    return {
        "interaction_found": len(interactions_found) > 0,
        "interactions": interactions_found,
        "drug1_info": drug1_info,
        "drug2_info": drug2_info
    }

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Medicine & Drug Interaction Advisor API - Enhanced Version",
        "version": "2.0.0",
        "total_drugs": len(COMPREHENSIVE_DRUG_DATABASE),
        "categories": list(set(drug['category'] for drug in COMPREHENSIVE_DRUG_DATABASE.values()))
    }

@app.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    """Process a general medicine-related query"""
    query_lower = request.query.lower()
    
    # Identify drugs mentioned
    drugs_identified = []
    drug_details = None
    
    for drug_name in COMPREHENSIVE_DRUG_DATABASE.keys():
        if drug_name in query_lower:
            drugs_identified.append(drug_name)
            
    # Also check brand names
    for generic_name, drug_info in COMPREHENSIVE_DRUG_DATABASE.items():
        for brand in drug_info['brand_names']:
            if brand.lower() in query_lower:
                drugs_identified.append(generic_name)
                break
    
    drugs_identified = list(set(drugs_identified))  # Remove duplicates
    
    # Determine query type
    if "side effect" in query_lower or "effects" in query_lower:
        query_type = "side_effects"
        if drugs_identified:
            drug_data = find_drug_by_name(drugs_identified[0])
            if drug_data:
                _, drug_info = drug_data
                response = f"{drug_info['generic_name']} ({', '.join(drug_info['brand_names'])}) side effects:\n\n{drug_info['side_effects']}\n\nCategory: {drug_info['category']}\nPrescription Required: {'Yes' if drug_info['prescription_required'] else 'No'}"
                drug_details = drug_info
            else:
                response = "Drug not found in database."
        else:
            response = "Please specify which medication you'd like to know about."
            
    elif "interaction" in query_lower or "together" in query_lower:
        query_type = "interaction"
        response = "Please use the drug interaction checker endpoint for detailed interaction analysis."
        
    elif "what is" in query_lower or "used for" in query_lower or "uses" in query_lower:
        query_type = "usage"
        if drugs_identified:
            drug_data = find_drug_by_name(drugs_identified[0])
            if drug_data:
                _, drug_info = drug_data
                response = f"{drug_info['generic_name']} ({', '.join(drug_info['brand_names'])}) is used for:\n\n{drug_info['uses']}\n\nCategory: {drug_info['category']}\nDosage: {drug_info['dosage']}\nPrice Range: {drug_info['price_range']}"
                drug_details = drug_info
            else:
                response = "Drug not found in database."
        else:
            response = "Please specify which medication you'd like to know about."
            
    elif "dosage" in query_lower or "dose" in query_lower or "how much" in query_lower:
        query_type = "dosage"
        if drugs_identified:
            drug_data = find_drug_by_name(drugs_identified[0])
            if drug_data:
                _, drug_info = drug_data
                response = f"{drug_info['generic_name']} dosage:\n\n{drug_info['dosage']}\n\nWarnings: {drug_info['warnings']}"
                drug_details = drug_info
            else:
                response = "Drug not found in database."
        else:
            response = "Please specify which medication you'd like to know about."
            
    elif "mental health" in query_lower or "depression" in query_lower or "anxiety" in query_lower or "psychotropic" in query_lower:
        query_type = "category_search"
        mental_health_drugs = [
            (name, info) for name, info in COMPREHENSIVE_DRUG_DATABASE.items() 
            if any(cat in info['category'] for cat in ['Antidepressant', 'Anti-anxiety', 'Antipsychotic', 'Mood Stabilizer', 'Benzodiazepine'])
        ]
        response = "Mental Health Medications in our database:\n\n"
        for drug_name, drug_info in mental_health_drugs[:10]:  # Show first 10
            response += f"• {drug_info['generic_name']} ({drug_info['brand_names'][0]}): {drug_info['category']} - {drug_info['uses'][:100]}...\n"
    else:
        query_type = "general"
        response = f"I can help you with medication information. Our database includes {len(COMPREHENSIVE_DRUG_DATABASE)} drugs including mental health medications, antibiotics, pain relievers, and more. Ask about side effects, uses, dosage, or interactions."
    
    return QueryResponse(
        query=request.query,
        drugs_identified=drugs_identified,
        query_type=query_type,
        response=response,
        sources_used=1,
        drug_details=drug_details
    )

@app.post("/check-interaction", response_model=DrugInteractionResponse)
async def check_drug_interaction_endpoint(request: DrugInteractionRequest):
    """Check for interactions between two specific drugs"""
    result = check_drug_interaction(request.drug1, request.drug2)
    
    if result['interaction_found']:
        response = f"⚠️ INTERACTION WARNING: {request.drug1} and {request.drug2}\n\n"
        for interaction in result['interactions']:
            response += f"• {interaction['description']}\n"
        response += "\nAlways consult your healthcare provider before taking these medications together."
    else:
        if result.get('drug1_found') and result.get('drug2_found'):
            response = f"✅ No major interactions found between {request.drug1} and {request.drug2}. However, always consult your healthcare provider before combining medications."
        else:
            response = result['response']
    
    return DrugInteractionResponse(
        drug1=request.drug1,
        drug2=request.drug2,
        interaction_found=result['interaction_found'],
        interactions=result.get('interactions', []),
        response=response,
        sources=["Comprehensive Drug Database"]
    )

@app.get("/search/{category}")
async def search_by_category(category: str):
    """Search drugs by category"""
    category_lower = category.lower()
    
    matching_drugs = []
    for drug_name, drug_info in COMPREHENSIVE_DRUG_DATABASE.items():
        if category_lower in drug_info['category'].lower():
            matching_drugs.append({
                'generic_name': drug_info['generic_name'],
                'brand_names': drug_info['brand_names'],
                'category': drug_info['category'],
                'uses': drug_info['uses'],
                'prescription_required': drug_info['prescription_required']
            })
    
    return {
        'category': category,
        'count': len(matching_drugs),
        'drugs': matching_drugs
    }

@app.get("/drug/{drug_name}")
async def get_drug_details(drug_name: str):
    """Get detailed information about a specific drug"""
    drug_data = find_drug_by_name(drug_name)
    
    if not drug_data:
        raise HTTPException(status_code=404, detail=f"Drug '{drug_name}' not found")
    
    generic_name, drug_info = drug_data
    return {
        'generic_name': generic_name,
        'details': drug_info
    }

@app.get("/mental-health-drugs")
async def get_mental_health_drugs():
    """Get all mental health related drugs"""
    mental_health_categories = [
        'Antidepressant', 'Anti-anxiety', 'Antipsychotic', 
        'Mood Stabilizer', 'Benzodiazepine', 'ADHD', 'CNS Stimulant'
    ]
    
    mental_health_drugs = {}
    for drug_name, drug_info in COMPREHENSIVE_DRUG_DATABASE.items():
        for category in mental_health_categories:
            if category in drug_info['category']:
                if category not in mental_health_drugs:
                    mental_health_drugs[category] = []
                mental_health_drugs[category].append({
                    'generic_name': drug_info['generic_name'],
                    'brand_names': drug_info['brand_names'],
                    'uses': drug_info['uses'],
                    'controlled_substance': drug_info.get('controlled_substance', False)
                })
                break
    
    return mental_health_drugs

@app.get("/all-drugs")
async def get_all_drugs():
    """Get list of all drugs in database"""
    drug_list = []
    for drug_name, drug_info in COMPREHENSIVE_DRUG_DATABASE.items():
        drug_list.append({
            'generic_name': drug_info['generic_name'],
            'brand_names': drug_info['brand_names'],
            'category': drug_info['category']
        })
    
    return {
        'total': len(drug_list),
        'drugs': drug_list
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("enhanced_main:app", host="0.0.0.0", port=8000, reload=True)