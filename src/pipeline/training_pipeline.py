import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.data_vectorization import DataVectorization
from src.components.model_train import ModelTrain
from src.entity.config_entity import (
    DataIngestionConfig,
    DataTransformationConfig,
    DataVectorizationConfig,
    ModelTrainConfig
)

# Setup logging
logging.basicConfig(
    format="%(asctime)s : %(levelname)s : %(message)s",
    level=logging.INFO
)

def run_training_pipeline():
    try:
        # Step 1: Data Ingestion
        logging.info("🚀 Starting data ingestion...")
        data_ingestion = DataIngestion(DataIngestionConfig())
        ingestion_artifact = data_ingestion.initate_data_ingestion()
        logging.info("✅ Data ingestion completed.")
        logging.info(f"📄 Train data path: {ingestion_artifact.train_file_path}")
        logging.info(f"📄 Test data path: {ingestion_artifact.test_file_path}")

        # Step 2: Data Transformation
        logging.info("🔄 Starting data transformation...")
        data_transformation = DataTransformation(DataTransformationConfig(), ingestion_artifact)
        transformation_artifacts = data_transformation.initiate_data_transformation()
        logging.info("✅ Data transformation completed.")
        logging.info(f"📝 Transformed train path: {transformation_artifacts.transformed_train_file_path}")
        logging.info(f"📝 Transformed test path: {transformation_artifacts.transformed_test_file_path}")

        # Step 3: Vectorization
        logging.info("🔡 Starting vectorization (Word2Vec)...")
        vectorizer = DataVectorization(transformation_artifacts, DataVectorizationConfig())
        vectorization_artifact = vectorizer.initate_data_vectorization()
        logging.info("✅ Vectorization completed.")
        logging.info(f"📦 Train vectors path: {vectorization_artifact.train_vectors_file_path}")
        logging.info(f"📦 Test vectors path: {vectorization_artifact.test_vectors_file_path}")

        # Step 4: Model Training
        logging.info("🏋️‍♂️ Starting model training...")
        model_train = ModelTrain(vectorization_artifact, ModelTrainConfig())
        model_train_artifact = model_train.initiate_model_train()
        logging.info("✅ Model training completed.")
        logging.info(f"🗃️ Model saved at: {model_train_artifact.train_model_path}")
        logging.info(f"📊 Model Metrics: Precision={model_train_artifact.precision:.4f}, Recall={model_train_artifact.recall:.4f}, Accuracy={model_train_artifact.accuracy:.4f}, F1 Score={model_train_artifact.f1_score:.4f}")

    except Exception as e:
        logging.exception(f"🔥 Pipeline failed due to: {e}")

if __name__ == "__main__":
    run_training_pipeline()
