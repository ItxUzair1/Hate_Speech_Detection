from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig

if __name__ == "__main__":
    data_ingestion = DataIngestion(DataIngestionConfig())
    ingestion_artifact = data_ingestion.initate_data_ingestion()
    print("Data ingestion completed.")
    print(f"Train data path: {ingestion_artifact.train_file_path}")
    print(f"Test data path: {ingestion_artifact.test_file_path}")
