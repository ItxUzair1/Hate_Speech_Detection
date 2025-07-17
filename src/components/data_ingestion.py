from src.exception.exception import CustomException
from src.logging.logger import logging
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifacts_entity import DataIngestionArtifacts
import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

    def initate_data_ingestion(self):
        try:
            logging.info("Starting the data ingestion process.")

            logging.info(f"Reading dataset from path: {self.data_ingestion_config.raw_data_path}")
            df = pd.read_csv(self.data_ingestion_config.raw_data_path)
            logging.info(f"Dataset successfully loaded. Shape: {df.shape}")

            
            if "Content_int" in df.columns:
                logging.info("Dropping 'Content_int' column.")
                df.drop(columns=["Content_int"], inplace=True, axis=1)
                logging.info("'Content_int' column dropped successfully.")
            else:
                logging.warning("'Content_int' column not found in the dataset.")
                raise CustomException("'Content_int' column does not exist.", sys)  # type: ignore

            logging.info("Removing rows where 'Label' is not a valid class (0 or 1).")
            df = df[df["Label"] != "Label"]

            
            logging.info("Converting 'Label' column data type to integer.")
            df["Label"] = df["Label"].astype(int)
            logging.info("Conversion successful. Unique labels: %s", df["Label"].unique())

      
            logging.info("Splitting the dataset into train and test sets.")
            train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
            logging.info(f"Train set shape: {train_df.shape}, Test set shape: {test_df.shape}")

          
            os.makedirs(self.data_ingestion_config.ingested_dir, exist_ok=True)
            logging.info(f"Saving train set to: {self.data_ingestion_config.train_file_path}")
            train_df.to_csv(self.data_ingestion_config.train_file_path, index=False)
            logging.info(f"Saving test set to: {self.data_ingestion_config.test_file_path}")
            test_df.to_csv(self.data_ingestion_config.test_file_path, index=False)
            logging.info("Data ingestion process completed successfully.")

            return DataIngestionArtifacts(
                train_file_path=self.data_ingestion_config.train_file_path,
                test_file_path=self.data_ingestion_config.test_file_path
            )

        except Exception as e:
            logging.error("Exception occurred during data ingestion: %s", e)
            raise CustomException(e, sys)  # type: ignore
