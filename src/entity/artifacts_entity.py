from dataclasses import dataclass

@dataclass
class DataIngestionArtifacts:
    train_file_path:str
    test_file_path:str


@dataclass
class DataTransforamtionArtifacts:
    transformed_train_file_path:str
    transformed_test_file_path:str