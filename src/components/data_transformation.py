from src.exception.exception import CustomException
from src.logging.logger import logging
from src.entity.config_entity import DataTransformationConfig
from src.entity.artifacts_entity import DataTransforamtionArtifacts,DataIngestionArtifacts
import pandas as pd
import re
from tqdm import tqdm
import sys
import os
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup



class DataTransformation():
    def __init__(self,data_transforamtion_config:DataTransformationConfig,data_ingestion_artifacts:DataIngestionArtifacts):
        self.data_transformation_config=data_transforamtion_config
        self.data_ingestion_artifacts=data_ingestion_artifacts
        tqdm.pandas()

    
    def initiate_data_transformation(self)->DataTransforamtionArtifacts:# type: ignore
        logging.info("initiating the data transforamtion")
        try:
            logging.info(f"reading the train and test data from {self.data_ingestion_artifacts.train_file_path} and {self.data_ingestion_artifacts.test_file_path}")
            train_df=pd.read_csv(self.data_ingestion_artifacts.train_file_path)
            test_df=pd.read_csv(self.data_ingestion_artifacts.test_file_path)

            logging.info("Sucessfully read the train and test data")

            logging.info("applying lower() to train and test data")

            train_df["Content"]=train_df["Content"].str.lower()
            test_df["Content"]=test_df["Content"].str.lower()

            logging.info("Sucessfully lower the train and test data")

            train_df["Content"]=train_df["Content"].progress_apply(lambda x:BeautifulSoup(x,"html.parser").get_text())
            test_df["Content"]=test_df["Content"].progress_apply(lambda x:BeautifulSoup(x,"html.parser").get_text())

            logging.info("Sucessfuly remove html tags from train and test data")

            train_df["Content"]=train_df["Content"].progress_apply(lambda x:re.sub(r"[^a-zA-Z0-9\s]"," ",x))
            test_df["Content"]=test_df["Content"].progress_apply(lambda x:re.sub(r"[^a-zA-Z0-9\s]"," ",x))

            logging.info("Sucessfully removed special charachters from train and test data")

            logging.info("Tokenizing the train and test data")
            train_df["Content"]=train_df["Content"].progress_apply(lambda x:word_tokenize(x))
            test_df["Content"]=test_df["Content"].progress_apply(lambda x:word_tokenize(x))

            logging.info("Sucessfully tokenized train and test data")

            logging.info("Removing stopwords from train and test data")
            wl=WordNetLemmatizer()
            stop_words=set(stopwords.words("english"))
            train_df["Content"]=train_df["Content"].progress_apply(lambda x:" ".join([wl.lemmatize(word) for word in x if not word in stop_words]))
            test_df["Content"]=test_df["Content"].progress_apply(lambda x:" ".join([wl.lemmatize(word) for word in x if not word in stop_words]))

            os.makedirs(self.data_transformation_config.transformed_dir,exist_ok=True)

            train_df.to_csv(self.data_transformation_config.transformed_train_file_path,index=False)
            test_df.to_csv(self.data_transformation_config.transformed_test_file_path,index=False)

            return DataTransforamtionArtifacts(self.data_transformation_config.transformed_train_file_path,self.data_transformation_config.transformed_test_file_path)


        except Exception as e:
            raise CustomException(e,sys)#type: ignore

