from src.exception.exception import CustomException
from src.logging.logger import logging
from src.entity.config_entity import DataVectorizationConfig
from src.entity.artifacts_entity import DataTransforamtionArtifacts, DataVectorizationArtifacts
from src.utils.main_utlils import save_numpy_array, save_object

import pandas as pd
import numpy as np
import sys
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize


class DataVectorization:
    def __init__(
        self,
        data_transformation_artifacts: DataTransforamtionArtifacts,
        data_vectorization_config: DataVectorizationConfig,
    ):
        self.data_transformation_artifacts = data_transformation_artifacts
        self.data_vectorization_config = data_vectorization_config

    def get_avg_Word2Vec(self, sentence, model):
        try:
            vectors = [model.wv[word] for word in sentence if word in model.wv.index_to_key]
            if not vectors:
                logging.warning(f"No valid vectors found for sentence: {' '.join(sentence)}")
                return np.zeros(model.vector_size)
            return np.mean(vectors, axis=0)

        except Exception as e:
            logging.error(f"Error in get_avg_Word2Vec: {e}")
            raise CustomException(e, sys)#type:ignore

    def get_vectorizor(self, tokenized_sentences):
        try:
            logging.info("Training Word2Vec model...")
            model = Word2Vec(sentences=tokenized_sentences, vector_size=100, window=5, min_count=5, sg=1)
            save_object(self.data_vectorization_config.vectorizor_model_path, model)
            logging.info("Word2Vec model saved successfully.")
            return model

        except Exception as e:
            logging.error(f"Error in get_vectorizor: {e}")
            raise CustomException(e, sys)#type:ignore

    def initate_data_vectorization(self):
        try:
            logging.info("Reading transformed training and testing datasets...")
            train_df = pd.read_csv(self.data_transformation_artifacts.transformed_train_file_path)
            test_df = pd.read_csv(self.data_transformation_artifacts.transformed_test_file_path)

            X_train = train_df.iloc[:, :-1].astype(str)
            y_train = np.array(train_df.iloc[:, -1].values)

            X_test = test_df.iloc[:, :-1].astype(str)
            y_test = np.array(test_df.iloc[:, -1].values)

            logging.info("Tokenizing sentences...")
            X_train_tokens = [word_tokenize(" ".join(row)) for row in X_train.values]
            X_test_tokens = [word_tokenize(" ".join(row)) for row in X_test.values]

            vectorizor = self.get_vectorizor(X_train_tokens)

            logging.info("Vectorizing training and test sentences...")
            X_train_vectors = np.array([self.get_avg_Word2Vec(sentence, vectorizor) for sentence in X_train_tokens])
            X_test_vectors = np.array([self.get_avg_Word2Vec(sentence, vectorizor) for sentence in X_test_tokens])

            logging.info(f"Train vectors shape: {X_train_vectors.shape}")
            logging.info(f"Test vectors shape: {X_test_vectors.shape}")

            logging.info("Saving vectorized arrays to disk...")
            save_numpy_array(self.data_vectorization_config.train_vectors_file_path, X_train_vectors)
            save_numpy_array(self.data_vectorization_config.test_vectors_file_path, X_test_vectors)

            logging.info("Data vectorization complete.")
            return DataVectorizationArtifacts(
                self.data_vectorization_config.train_vectors_file_path,
                self.data_vectorization_config.test_vectors_file_path,
                vectorizor_model_path=self.data_vectorization_config.vectorizor_model_path,
                y_train=y_train,
                y_test=y_test
            )

        except Exception as e:
            logging.error(f"Error in initate_data_vectorization: {e}")
            raise CustomException(e, sys)#type: ignore
