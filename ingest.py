from backend.data_ingestion import ingest_data

if __name__ == "__main__":
    print("Uploading products to AstraDB...")
    count = ingest_data()
    print(f"Done! {count} products uploaded.")