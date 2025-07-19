from dataclasses import dataclass
import numpy as np

@dataclass
class DataIngestionArtifacts:
    train_file_path:str
    test_file_path:str


@dataclass
class DataTransforamtionArtifacts:
    transformed_train_file_path:str
    transformed_test_file_path:str

@dataclass
class DataVectorizationArtifacts:
    train_vectors_file_path:str
    test_vectors_file_path:str
    vectorizor_model_path:str
    y_train:np.ndarray
    y_test:np.ndarray

@dataclass
class ModelTrainArtifacts:
    train_model_path:str
    vectorizor_model_path:str
    precision:float
    recall:float
    accuracy:float
    f1_score:float