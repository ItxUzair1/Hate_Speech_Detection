from dataclasses import dataclass
import os
from src.constants import (RAW_DATA_DIR,RAW_FILE_NAME,ARTIFACTS,TEST_FILE_NAME,TRAIN_FILE_NAME,INGESTED_DIR,DATA_INGESTION
                           ,DATA_TRANSFORMATION,TRANSFORMED_DIR,TRANSFORMED_TRAIN_FILE,TRANSFORMED_TEST_FILE,
                           DATA_VECTORIZATION,TEST_VECTORS_FILE_NAME,TRAIN_VECTORS_FILE_NAME,
                           VECTORIZER_MODEL_NAME,MODEL_DIR,MODEL_NAME)

@dataclass
class DataIngestionConfig:
    ingested_dir=os.path.join(ARTIFACTS,DATA_INGESTION,INGESTED_DIR)
    train_file_path=os.path.join(ingested_dir,TRAIN_FILE_NAME)
    test_file_path=os.path.join(ingested_dir,TEST_FILE_NAME)
    raw_data_path=os.path.join(RAW_DATA_DIR,RAW_FILE_NAME)


@dataclass
class DataTransformationConfig:
    transformed_dir=os.path.join(ARTIFACTS,DATA_TRANSFORMATION,TRANSFORMED_DIR)
    transformed_train_file_path=os.path.join(transformed_dir,TRANSFORMED_TRAIN_FILE)
    transformed_test_file_path=os.path.join(transformed_dir,TRANSFORMED_TEST_FILE)


@dataclass
class DataVectorizationConfig:
    vectorization_dir=os.path.join(ARTIFACTS,DATA_VECTORIZATION)
    train_vectors_file_path=os.path.join(vectorization_dir,TRAIN_VECTORS_FILE_NAME)
    test_vectors_file_path=os.path.join(vectorization_dir,TEST_VECTORS_FILE_NAME)
    vectorizor_model_path=os.path.join(MODEL_DIR,VECTORIZER_MODEL_NAME)


@dataclass
class ModelTrainConfig:
    train_model_path=os.path.join(MODEL_DIR,MODEL_NAME)