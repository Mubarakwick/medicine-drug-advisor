#!/usr/bin/env python3
"""
Script to initialize the vector database with FDA drug data
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

from rag_pipeline import MedicineRAGPipeline
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Initialize the vector database"""
    logger.info("Starting database initialization...")
    
    # Create pipeline
    pipeline = MedicineRAGPipeline(vector_db_path="../data/vector_db")
    
    # Initialize database
    pipeline.initialize_database()
    
    # Print stats
    stats = pipeline.vector_db.get_stats()
    logger.info(f"Database initialized successfully!")
    logger.info(f"Statistics: {stats}")

if __name__ == "__main__":
    main()