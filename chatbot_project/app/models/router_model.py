from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import os
import logging

class RouterModel:
    def __init__(self, model_path="app/models/router_model.pkl"):
        self.model_path = model_path
        self.vectorizer = TfidfVectorizer()
        self.model = MultinomialNB()

        if os.path.exists(self.model_path):
            self.load_model()
        else:
            self.train_model()

    def train_model(self):
        try:
            X_train = [
                "What is the weather today?",
                "Turn on the lights",
                "Tell me a joke",
                "How do I cook pasta?",
                "Set an alarm for 7 AM"
            ]
            y_train = ["question", "action", "statement", "question", "action"]

            X_train_vec = self.vectorizer.fit_transform(X_train)
            self.model.fit(X_train_vec, y_train)
            self.save_model()
            logging.info("Router model trained and saved.")
        except Exception as e:
            logging.error(f"Error during model training: {str(e)}")

    def predict(self, user_input):
        try:
            X_input_vec = self.vectorizer.transform([user_input])
            return self.model.predict(X_input_vec)[0]
        except Exception as e:
            logging.error(f"Error during prediction: {str(e)}")
            return None

    def save_model(self):
        try:
            joblib.dump((self.vectorizer, self.model), self.model_path)
            logging.info("Model saved successfully.")
        except Exception as e:
            logging.error(f"Error saving model: {str(e)}")

    def load_model(self):
        try:
            self.vectorizer, self.model = joblib.load(self.model_path)
            logging.info("Model loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading model: {str(e)}")
