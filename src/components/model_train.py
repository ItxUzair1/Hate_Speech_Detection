import sys
import os
import logging
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

from src.exception.exception import CustomException
from src.entity.config_entity import ModelTrainConfig
from src.entity.artifacts_entity import DataVectorizationArtifacts, ModelTrainArtifacts
from src.utils.main_utlils import load_numpy_array, save_object
import numpy as np


class ModelTrain:
    def __init__(self, data_vectorization_artifacts: DataVectorizationArtifacts, model_train_config: ModelTrainConfig):
        self.data_vectorization_artifacts = data_vectorization_artifacts
        self.model_train_config = model_train_config

    def initiate_model_train(self):
        try:
            logging.info("Loading vectorized training and test data...")
            X_train = load_numpy_array(self.data_vectorization_artifacts.train_vectors_file_path)
            X_test = load_numpy_array(self.data_vectorization_artifacts.test_vectors_file_path)
            y_train = self.data_vectorization_artifacts.y_train
            y_test = self.data_vectorization_artifacts.y_test



            xgb_clf = XGBClassifier(
                objective='binary:logistic',
                eval_metric='logloss',
                scale_pos_weight=4.56,
                n_estimators=100,
                learning_rate=0.1,
                max_depth=10,
                random_state=42
            )

            logging.info("Training XGBoost classifier...")
            xgb_clf.fit(X_train, y_train)

            logging.info("Evaluating model...")
            y_pred = xgb_clf.predict(X_test)

            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
            recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
            f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)

            logging.info(f"Model evaluation complete: Accuracy={accuracy:.4f}, Precision={precision:.4f}, Recall={recall:.4f}, F1={f1:.4f}")

            save_object(self.model_train_config.train_model_path, xgb_clf)
            logging.info(f"Model saved at {self.model_train_config.train_model_path}")

            return ModelTrainArtifacts(
                self.model_train_config.train_model_path,
                self.data_vectorization_artifacts.vectorizor_model_path,
                float(precision),
                float(recall),
                float(accuracy),
                float(f1)
            )

        except Exception as e:
            logging.error("Exception occurred in model training", exc_info=True)
            raise CustomException(e, sys)# type:ignore
