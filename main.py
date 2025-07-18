from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.entity.config_entity import DataIngestionConfig, DataTransformationConfig

if __name__ == "__main__":
    # Step 1: Data Ingestion
    data_ingestion = DataIngestion(DataIngestionConfig())
    ingestion_artifact = data_ingestion.initate_data_ingestion()
    print("✅ Data ingestion completed.")
    print(f"📄 Train data path: {ingestion_artifact.train_file_path}")
    print(f"📄 Test data path: {ingestion_artifact.test_file_path}")

    # Step 2: Data Transformation (Fixed: Pass DataTransformationConfig)
    data_transformation = DataTransformation(DataTransformationConfig(), ingestion_artifact)
    transformation_artifacts = data_transformation.initiate_data_transformation()
    print("✅ Data transformation completed.")
    print(f"📝 Transformed train path: {transformation_artifacts.transformed_train_file_path}")
    print(f"📝 Transformed test path: {transformation_artifacts.transformed_test_file_path}")
