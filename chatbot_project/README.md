🚧 Under Development 🚧

This repository is currently a work in progress and is actively being developed. Please note that features, functionality, and documentation may change frequently as the project evolves.

Feel free to explore, but be aware that the codebase may contain unfinished features and could be subject to significant changes.

Stay tuned for updates!



# Chatbot Project

## Overview

The Chatbot Project is an advanced, modular chatbot designed to provide intelligent responses to user queries using various AI models and services, including OpenAI, LocalAI, and AutoGPT. The chatbot is built with FastAPI and can execute tasks, run Linux commands, and adapt continuously through a learning pipeline.

## Features

- **Multi-Agent Architecture**: Routes queries to OpenAI, LocalAI, or AutoGPT based on context and intent.
- **Command Execution**: Identifies and executes shell commands securely using Shell-GPT.
- **Continuous Learning**: Adapts and improves over time using a continuous learning pipeline.
- **Caching**: Utilizes Redis for caching responses to enhance performance.
- **Asynchronous Processing**: Handles requests asynchronously for improved scalability.
- **Advanced NLU**: Uses Spacy and Hugging Face's Transformers for natural language understanding.

## Project Structure

```plaintext
chatbot_project/
│
├── app/
│   ├── __init__.py             # Initialize the app
│   ├── main.py                 # Main entry point
│   ├── router.py               # Routing logic for agents
│   ├── nlu.py                  # Natural Language Understanding and Intent Detection
│   ├── config.py               # Configuration (API keys, endpoints)
│   ├── utils.py                # Utility functions (e.g., caching, error handling)
│   ├── continuous_learning.py  # Continuous Learning System
│   ├── agents/
│   │   ├── __init__.py         # Initialize the agents module
│   │   ├── localai_agent.py    # Interfacing with LocalAI
│   │   ├── openai_agent.py     # Interfacing with OpenAI
│   │   ├── shellgpt_agent.py   # Executing shell commands with Shell-GPT
│   │   ├── async_agents.py     # Asynchronous API handling
│   └── models/
│       ├── __init__.py         # Initialize the models module
│       ├── router_model.py     # Machine Learning model for routing
│
├── tests/                      # Unit and integration tests
│   ├── test_router_model.py    # Tests for the router model
│   ├── test_agents.py          # Tests for agent functions
│
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration for containerization
├── docker-compose.yml          # Docker Compose for multi-container setup
├── README.md                   # Project documentation
└── .env-template               # Template for environment variables
Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/chatbot_project.git
cd chatbot_project
2. Create and Configure the .env File
Copy the .env-template to .env and fill in the required values:

bash
Copy code
cp .env-template .env
Edit the .env file to add your API keys and configuration:

plaintext
Copy code
OPENAI_API_KEY=your-openai-api-key-here
LOCALAI_API_ENDPOINT=http://localhost:5000/api/v1/chat
CACHE_TTL=300
LOG_LEVEL=INFO
LOG_FILE=logs/chatbot.log
INTERACTION_LOG_FILE=logs/user_interactions.log
FINE_TUNED_MODEL_DIR=./app/models/fine_tuned_bert
PRODUCTION_MODEL_DIR=./app/models/production_model
TRAINING_INTERVAL=3600
REDIS_HOST=redis
REDIS_PORT=6379
3. Build and Run the Application with Docker Compose
Build and start the services using Docker Compose:

bash
Copy code
docker-compose up --build
This will start the chatbot service on http://localhost:8000 and the Redis service on localhost:6379.

4. Access the Application
You can interact with the chatbot by sending POST requests to the /chat endpoint:

bash
Copy code
curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{"message": "Tell me a joke"}'
5. Running Tests
Run the tests to ensure everything is working correctly:

bash
Copy code
docker exec -it chatbot_container pytest tests/
6. Stopping the Application
To stop the application and remove containers:

bash
Copy code
docker-compose down
Usage Examples
1. Querying OpenAI
Send a query to OpenAI through the chatbot:

bash
Copy code
curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{"message": "What is the weather today?"}'
2. Executing Shell Commands
Ask the chatbot to execute a shell command:

bash
Copy code
curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{"message": "Run the command: ls"}'
3. Continuous Learning
The chatbot automatically learns and improves over time, fine-tuning its models based on user interactions.

Extending the Project
1. Adding New Agents
To add a new agent (e.g., for another API):

Create a new file in the app/agents/ directory (e.g., new_agent.py).
Implement the API interaction logic.
Update app/router.py to include routing logic for the new agent.
2. Adding More Tests
Add new test cases in the tests/ directory to cover additional functionality or edge cases.

3. Enhancing NLU
You can enhance the NLU capabilities by fine-tuning the existing models or integrating additional NLP models.

4. Deploying to the Cloud
You can deploy the chatbot to any cloud provider that supports Docker. Ensure that the .env file is properly configured for the production environment.

Contributing
We welcome contributions to the Chatbot Project! Please fork the repository, make your changes, and submit a pull request.

Contribution Guidelines
Ensure your code adheres to the existing style and conventions.
Write tests for any new functionality.
Update the documentation as needed.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgments
FastAPI - Web framework used for the application.
OpenAI - For the powerful GPT models.
Spacy - For Natural Language Processing.
Docker - For containerization.
Redis - For caching and data storage.
