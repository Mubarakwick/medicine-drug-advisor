from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import logging
import os
from dotenv import load_dotenv
from rag_pipeline import MedicineRAGPipeline

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Medicine & Drug Interaction Advisor API", version="1.0.0")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize RAG pipeline
rag_pipeline = MedicineRAGPipeline()

# Request/Response models
class QueryRequest(BaseModel):
    query: str
    
class DrugInteractionRequest(BaseModel):
    drug1: str
    drug2: str
    
class InitializeDatabaseRequest(BaseModel):
    confirm: bool = False
    
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
    
class HealthResponse(BaseModel):
    status: str
    vector_db_stats: Dict[str, Any]

@app.get("/", response_model=Dict[str, str])
async def root():
    """Root endpoint"""
    return {
        "message": "Medicine & Drug Interaction Advisor API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    stats = rag_pipeline.vector_db.get_stats()
    return {
        "status": "healthy",
        "vector_db_stats": stats
    }

@app.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    """Process a general medicine-related query"""
    try:
        result = rag_pipeline.process_query(request.query)
        return QueryResponse(**result)
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/check-interaction", response_model=DrugInteractionResponse)
async def check_drug_interaction(request: DrugInteractionRequest):
    """Check for interactions between two specific drugs"""
    try:
        result = rag_pipeline.check_drug_interaction(
            request.drug1,
            request.drug2
        )
        return DrugInteractionResponse(**result)
    except Exception as e:
        logger.error(f"Error checking drug interaction: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/initialize-database")
async def initialize_database(
    request: InitializeDatabaseRequest,
    background_tasks: BackgroundTasks
):
    """Initialize the vector database with FDA drug data"""
    if not request.confirm:
        return {
            "message": "Please confirm database initialization by setting confirm=true",
            "warning": "This will fetch data from FDA API and may take several minutes"
        }
    
    # Run initialization in background
    background_tasks.add_task(rag_pipeline.initialize_database)
    
    return {
        "message": "Database initialization started in background",
        "status": "processing"
    }

@app.get("/supported-queries")
async def get_supported_queries():
    """Get examples of supported query types"""
    return {
        "supported_query_types": [
            {
                "type": "interaction",
                "examples": [
                    "Can I take ibuprofen with amoxicillin?",
                    "Is it safe to combine aspirin and warfarin?",
                    "Drug interactions between metformin and lisinopril"
                ]
            },
            {
                "type": "side_effects",
                "examples": [
                    "What are the side effects of metformin?",
                    "Gabapentin side effects",
                    "Common reactions to prednisone"
                ]
            },
            {
                "type": "usage",
                "examples": [
                    "What is amoxicillin used for?",
                    "When should I take omeprazole?",
                    "How does ibuprofen work?"
                ]
            },
            {
                "type": "dosage",
                "examples": [
                    "How much acetaminophen can I take?",
                    "Proper dosage for ibuprofen",
                    "How often should I take amoxicillin?"
                ]
            },
            {
                "type": "warnings",
                "examples": [
                    "Who should not take aspirin?",
                    "Metformin warnings and precautions",
                    "Is ibuprofen safe during pregnancy?"
                ]
            }
        ]
    }

@app.get("/common-drugs")
async def get_common_drugs():
    """Get list of common drugs in the database"""
    return {
        "common_drugs": [
            "ibuprofen", "acetaminophen", "amoxicillin", "metformin",
            "lisinopril", "levothyroxine", "amlodipine", "metoprolol",
            "omeprazole", "losartan", "gabapentin", "sertraline",
            "simvastatin", "montelukast", "fluoxetine", "alprazolam",
            "prednisone", "tramadol", "furosemide", "pantoprazole"
        ],
        "note": "Database may contain information about other drugs as well"
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)