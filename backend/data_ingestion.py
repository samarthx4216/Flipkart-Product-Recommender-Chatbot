import os
import pandas as pd
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_astradb import AstraDBVectorStore
from langchain_core.documents import Document
from backend.logger import setup_logger

load_dotenv()
logger = setup_logger("data_ingestion")

def load_products(csv_path: str) -> list:
    logger.info(f"Loading products from {csv_path}")
    df = pd.read_csv(csv_path)
    documents = []
    for _, row in df.iterrows():
        content = f"""
Product: {row['name']}
Category: {row['category']}
Price: Rs.{row['price']}
Rating: {row['rating']}/5
Description: {row['description']}
        """.strip()
        doc = Document(
            page_content=content,
            metadata={
                "product_id": str(row['product_id']),
                "name": row['name'],
                "category": row['category'],
                "price": str(row['price']),
                "rating": str(row['rating']),
            }
        )
        documents.append(doc)
    logger.info(f"Loaded {len(documents)} products")
    return documents

def get_embeddings():
    logger.info("Loading HuggingFace embeddings")
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

def get_vector_store():
    embeddings = get_embeddings()
    vector_store = AstraDBVectorStore(
        embedding=embeddings,
        collection_name=os.getenv("ASTRA_DB_COLLECTION"),
        api_endpoint=os.getenv("ASTRA_DB_API_ENDPOINT"),
        token=os.getenv("ASTRA_DB_APPLICATION_TOKEN"),
    )
    return vector_store

def ingest_data(csv_path: str = "data/flipkart_products.csv"):
    logger.info("Starting data ingestion to AstraDB")
    documents = load_products(csv_path)
    vector_store = get_vector_store()
    vector_store.add_documents(documents)
    logger.info(f"Successfully ingested {len(documents)} products!")
    return len(documents)

if __name__ == "__main__":
    ingest_data()