from dataclasses import dataclass
import os
from src.constants import RAW_DATA_DIR,RAW_FILE_NAME,ARTIFACTS,TEST_FILE_NAME,TRAIN_FILE_NAME,INGESTED_DIR,DATA_INGESTION

@dataclass
class DataIngestionConfig:
    ingested_dir=os.path.join(ARTIFACTS,DATA_INGESTION,INGESTED_DIR)
    train_file_path=os.path.join(ingested_dir,TRAIN_FILE_NAME)
    test_file_path=os.path.join(ingested_dir,TEST_FILE_NAME)
    raw_data_path=os.path.join(RAW_DATA_DIR,RAW_FILE_NAME)