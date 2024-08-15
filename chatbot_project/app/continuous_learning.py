import json
import logging
from time import sleep
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from app.utils import log_user_interaction, deploy_model, handle_error
from config import settings

tokenizer = BertTokenizer.from_pretrained(settings.production_model_dir)

def preprocess_interaction_data():
    try:
        user_inputs = []
        labels = []

        with open(settings.interaction_log_file, "r") as log:
            for line in log:
                interaction = json.loads(line)
                user_input = interaction["user_input"]
                user_feedback = interaction.get("user_feedback")
                
                if user_feedback:  # Only use data with feedback for training
                    user_inputs.append(user_input)
                    labels.append(user_feedback)  # Convert feedback to appropriate labels

        tokenized_inputs = tokenizer(user_inputs, padding=True, truncation=True, return_tensors="pt")
        return tokenized_inputs, labels
    
    except Exception as e:
        logging.error(f"Error during data preprocessing: {str(e)}")
        return None, None

def fine_tune_bert(tokenized_inputs, labels):
    try:
        model = BertForSequenceClassification.from_pretrained(settings.production_model_dir)
        
        training_args = TrainingArguments(
            output_dir=settings.fine_tuned_model_dir,
            num_train_epochs=1,
            per_device_train_batch_size=8,
            per_device_eval_batch_size=8,
            warmup_steps=500,
            weight_decay=0.01,
            logging_dir="./logs",
        )
        
        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=tokenized_inputs,
            eval_dataset=None,
        )
        
        trainer.train()
        model.save_pretrained(settings.fine_tuned_model_dir)
        return model
    
    except Exception as e:
        logging.error(f"Error during model fine-tuning: {str(e)}")
        return None

def continuous_learning_pipeline():
    while True:
        try:
            tokenized_inputs, labels = preprocess_interaction_data()

            if labels:
                fine_tune_bert(tokenized_inputs, labels)
                deploy_model()
            
            sleep(settings.training_interval)
        
        except Exception as e:
            logging.error(f"Error in continuous learning pipeline: {str(e)}")
            handle_error(e)

if __name__ == "__main__":
    continuous_learning_pipeline()
