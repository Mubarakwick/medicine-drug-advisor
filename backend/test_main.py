from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Medicine & Drug Interaction Advisor API - Demo Mode", version="1.0.0")

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
    
class QueryResponse(BaseModel):
    query: str
    drugs_identified: List[str]
    query_type: str
    response: str
    sources_used: int
    
class DrugInteractionResponse(BaseModel):
    drug1: str
    drug2: str
    interaction_found: bool
    interactions: List[Dict[str, Any]]
    response: str
    sources: List[str]

# Mock responses for demonstration - INCLUDING INDIAN MEDICINES
MOCK_INTERACTIONS = {
    ("ibuprofen", "amoxicillin"): {
        "interaction_found": False,
        "response": "Ibuprofen and amoxicillin are generally safe to take together. There are no significant drug interactions reported between these medications. However, both may cause stomach upset, so it's recommended to take them with food. Always consult your healthcare provider before combining medications."
    },
    ("aspirin", "warfarin"): {
        "interaction_found": True,
        "response": "WARNING: Aspirin and warfarin have a major drug interaction. Both medications affect blood clotting and taking them together significantly increases the risk of bleeding. This combination should only be used under strict medical supervision. Contact your healthcare provider immediately."
    },
    ("metformin", "lisinopril"): {
        "interaction_found": False,
        "response": "Metformin and lisinopril can generally be taken together safely. In fact, they are often prescribed together for patients with diabetes and high blood pressure. Monitor your blood sugar and blood pressure regularly. Consult your healthcare provider for personalized advice."
    },
    # Indian medicine interactions
    ("crocin", "combiflam"): {
        "interaction_found": True,
        "response": "WARNING: Crocin (paracetamol) and Combiflam (ibuprofen + paracetamol) both contain paracetamol. Taking them together can lead to paracetamol overdose, which can cause serious liver damage. Do not take these medications together. Choose one or consult your doctor."
    },
    ("pan 40", "ecosprin"): {
        "interaction_found": False,
        "response": "Pan 40 (pantoprazole) and Ecosprin (aspirin) can be taken together. In fact, Pan 40 is often prescribed with Ecosprin to protect the stomach from aspirin's side effects. Take Pan 40 before meals and Ecosprin after meals as directed by your doctor."
    }
}

MOCK_SIDE_EFFECTS = {
    # International medicines
    "metformin": "Common side effects of metformin include: nausea, vomiting, stomach upset, diarrhea, and metallic taste. Serious but rare side effects include lactic acidosis. Take with food to reduce stomach upset. Contact your doctor if side effects persist.",
    "ibuprofen": "Common side effects of ibuprofen include: stomach pain, heartburn, nausea, and dizziness. Serious side effects may include stomach bleeding, kidney problems, and increased heart attack risk with long-term use. Take with food or milk.",
    "amoxicillin": "Common side effects of amoxicillin include: diarrhea, nausea, and skin rash. Serious side effects may include severe allergic reactions. Complete the full course of antibiotics even if you feel better.",
    
    # Indian medicines
    "crocin": "Crocin (paracetamol/acetaminophen) side effects: Generally well-tolerated. Rare side effects include allergic reactions, skin rash, and liver damage with overdose. Maximum dose is 4g per day. Avoid alcohol while taking this medication.",
    "combiflam": "Combiflam (ibuprofen + paracetamol) side effects: Stomach upset, heartburn, nausea, dizziness. May cause stomach ulcers with long-term use. Take with food. Not recommended for patients with kidney disease, heart disease, or stomach ulcers.",
    "pan 40": "Pan 40 (pantoprazole) side effects: Headache, diarrhea, nausea, stomach pain, gas. Long-term use may cause vitamin B12 deficiency. Rare: bone fractures, kidney problems. Take 30-60 minutes before meals.",
    "ecosprin": "Ecosprin (aspirin) side effects: Stomach upset, heartburn, increased bleeding risk. Can cause stomach ulcers. Not for children with viral infections (Reye's syndrome risk). Take with food or after meals.",
    "azithral": "Azithral (azithromycin) side effects: Diarrhea, nausea, stomach pain, headache. Rare: irregular heartbeat, liver problems. Complete the full course. Take 1 hour before or 2 hours after meals.",
    "dolo 650": "Dolo 650 (paracetamol) side effects: Similar to Crocin - generally safe when used as directed. Overdose can cause serious liver damage. Do not exceed 4g per day. Avoid if you have liver disease.",
    "shelcal": "Shelcal (calcium + vitamin D3) side effects: Constipation, gas, bloating. Rare: kidney stones with high doses. Take with meals for better absorption. Maintain adequate water intake.",
    "zincovit": "Zincovit (multivitamin + minerals) side effects: Generally well-tolerated. May cause nausea if taken on empty stomach, mild stomach upset, or unusual taste. Take with food. May turn urine bright yellow (harmless).",
    
    # Ayurvedic medicines
    "ashwagandha": "Ashwagandha side effects: Generally safe. May cause drowsiness, stomach upset, diarrhea in some people. Can lower blood sugar and blood pressure. Avoid during pregnancy. May interact with thyroid medications.",
    "triphala": "Triphala side effects: May cause diarrhea, abdominal cramps, especially in high doses. Start with small dose. Generally safe for long-term use. Helps with constipation and digestive health.",
    "tulsi": "Tulsi (Holy Basil) side effects: Generally very safe. May lower blood sugar levels. Can act as a blood thinner. Avoid before surgery. May affect fertility in high doses. Safe for daily use in moderate amounts."
}

MOCK_USAGE = {
    # Indian medicines
    "crocin": "Crocin is used for: Fever reduction, mild to moderate pain relief including headache, toothache, body ache, and period pain. Active ingredient: Paracetamol (acetaminophen). Available as tablets and syrup.",
    "combiflam": "Combiflam is used for: Pain relief and fever reduction. More effective than plain paracetamol for inflammation-related pain. Contains ibuprofen + paracetamol. Used for headaches, dental pain, menstrual cramps, arthritis.",
    "pan 40": "Pan 40 is used for: Acid reflux, GERD, peptic ulcers, Zollinger-Ellison syndrome. It's a proton pump inhibitor that reduces stomach acid production. Take before meals for best effect.",
    "ecosprin": "Ecosprin is used for: Heart attack prevention, stroke prevention in high-risk patients, and as a blood thinner. Low-dose aspirin (75-150mg) for cardiac protection. Also used for pain relief in higher doses.",
    "azithral": "Azithral is used for: Bacterial infections including respiratory tract infections, skin infections, ear infections, and sexually transmitted diseases. It's an antibiotic (azithromycin). Usually given as 3-day or 5-day course."
}

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Medicine & Drug Interaction Advisor API - Demo Mode with Indian Medicines",
        "version": "1.0.0",
        "note": "Running in demo mode without OpenAI API - includes Indian medicines"
    }

@app.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    """Process a general medicine-related query"""
    query_lower = request.query.lower()
    
    # Simple drug extraction - now includes Indian medicines
    drugs = []
    all_drugs = [
        # International
        "ibuprofen", "metformin", "amoxicillin", "aspirin", "warfarin", "lisinopril",
        # Indian medicines
        "crocin", "combiflam", "pan 40", "pan 40", "ecosprin", "azithral", 
        "dolo 650", "dolo", "shelcal", "zincovit",
        # Ayurvedic
        "ashwagandha", "triphala", "tulsi"
    ]
    
    for drug in all_drugs:
        if drug in query_lower:
            drugs.append(drug)
    
    # Determine query type
    if "side effect" in query_lower or "effects" in query_lower:
        query_type = "side_effects"
        if drugs:
            response = MOCK_SIDE_EFFECTS.get(drugs[0], 
                "Please consult your healthcare provider for information about this medication's side effects.")
        else:
            response = "Please specify which medication you'd like to know about. I have information on Indian medicines like Crocin, Combiflam, Pan 40, Ecosprin, and many others."
    elif "interaction" in query_lower or "together" in query_lower:
        query_type = "interaction"
        response = "Please use the drug interaction checker to check specific drug combinations. Try combinations like 'Crocin + Combiflam' or 'Pan 40 + Ecosprin'."
    elif "what is" in query_lower or "used for" in query_lower or "uses" in query_lower:
        query_type = "usage"
        if drugs:
            response = MOCK_USAGE.get(drugs[0], 
                "This medication information is not available in the demo. Please consult your healthcare provider.")
        else:
            response = "Please specify which medication you'd like to know about. I have information on Indian medicines like Crocin, Combiflam, Pan 40, Azithral, and others."
    else:
        query_type = "general"
        response = "I can help you with medication side effects, uses, and drug interactions. Try asking about Indian medicines like Crocin, Combiflam, Pan 40, or Ayurvedic medicines like Ashwagandha."
    
    return QueryResponse(
        query=request.query,
        drugs_identified=drugs,
        query_type=query_type,
        response=response,
        sources_used=1
    )

@app.post("/check-interaction", response_model=DrugInteractionResponse)
async def check_drug_interaction(request: DrugInteractionRequest):
    """Check for interactions between two specific drugs"""
    drug1_lower = request.drug1.lower()
    drug2_lower = request.drug2.lower()
    
    # Check in both orders
    interaction_key = (drug1_lower, drug2_lower)
    reverse_key = (drug2_lower, drug1_lower)
    
    if interaction_key in MOCK_INTERACTIONS:
        interaction_data = MOCK_INTERACTIONS[interaction_key]
    elif reverse_key in MOCK_INTERACTIONS:
        interaction_data = MOCK_INTERACTIONS[reverse_key]
    else:
        interaction_data = {
            "interaction_found": False,
            "response": f"I don't have specific interaction data for {request.drug1} and {request.drug2} in the demo database. For accurate information, please consult your healthcare provider or pharmacist. Note: I have interaction data for combinations like 'Crocin + Combiflam' and 'Pan 40 + Ecosprin'."
        }
    
    return DrugInteractionResponse(
        drug1=request.drug1,
        drug2=request.drug2,
        interaction_found=interaction_data["interaction_found"],
        interactions=[],
        response=interaction_data["response"],
        sources=["Demo Database with Indian Medicines"]
    )

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "mode": "demo",
        "vector_db_stats": {
            "total_documents": 0,
            "total_vectors": 0,
            "dimension": 384,
            "unique_drugs": 25,
            "indian_medicines": 15,
            "ayurvedic_medicines": 3
        }
    }

@app.get("/available-medicines")
async def get_available_medicines():
    """Get list of available medicines in demo"""
    return {
        "international_medicines": [
            "ibuprofen", "metformin", "amoxicillin", "aspirin", "warfarin", "lisinopril"
        ],
        "indian_medicines": [
            "Crocin (Paracetamol)",
            "Combiflam (Ibuprofen + Paracetamol)", 
            "Pan 40 (Pantoprazole)",
            "Ecosprin (Aspirin)",
            "Azithral (Azithromycin)",
            "Dolo 650 (Paracetamol)",
            "Shelcal (Calcium + Vitamin D3)",
            "Zincovit (Multivitamin)"
        ],
        "ayurvedic_medicines": [
            "Ashwagandha",
            "Triphala",
            "Tulsi (Holy Basil)"
        ],
        "sample_interactions": [
            "Crocin + Combiflam (Dangerous - both contain paracetamol)",
            "Pan 40 + Ecosprin (Safe - often prescribed together)"
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("test_main:app", host="0.0.0.0", port=8000, reload=True)