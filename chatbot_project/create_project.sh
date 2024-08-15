#!/bin/bash

# Set project name
PROJECT_NAME="chatbot_project"

# Function to create a directory and echo it
create_dir() {
    mkdir -p "$1"
    echo "Created directory: $1"
}

# Function to create a file and echo it
create_file() {
    touch "$1"
    echo "Created file: $1"
}

# Create project root directory
create_dir $PROJECT_NAME

# Create app directories and files
create_dir "$PROJECT_NAME/app"
create_file "$PROJECT_NAME/app/__init__.py"
create_file "$PROJECT_NAME/app/main.py"
create_file "$PROJECT_NAME/app/router.py"
create_file "$PROJECT_NAME/app/nlu.py"
create_file "$PROJECT_NAME/app/config.py"
create_file "$PROJECT_NAME/app/utils.py"
create_file "$PROJECT_NAME/app/continuous_learning.py"

# Create agents directories and files
create_dir "$PROJECT_NAME/app/agents"
create_file "$PROJECT_NAME/app/agents/__init__.py"
create_file "$PROJECT_NAME/app/agents/localai_agent.py"
create_file "$PROJECT_NAME/app/agents/openai_agent.py"
create_file "$PROJECT_NAME/app/agents/shellgpt_agent.py"
create_file "$PROJECT_NAME/app/agents/async_agents.py"

# Create models directories and files
create_dir "$PROJECT_NAME/app/models"
create_file "$PROJECT_NAME/app/models/__init__.py"
create_file "$PROJECT_NAME/app/models/router_model.py"

# Create tests directories and files
create_dir "$PROJECT_NAME/tests"
create_file "$PROJECT_NAME/tests/test_router_model.py"
create_file "$PROJECT_NAME/tests/test_agents.py"

# Create project root files
create_file "$PROJECT_NAME/requirements.txt"
create_file "$PROJECT_NAME/Dockerfile"
create_file "$PROJECT_NAME/docker-compose.yml"
create_file "$PROJECT_NAME/README.md"
create_file "$PROJECT_NAME/.env"

# Initialize a Python virtual environment
python3 -m venv "$PROJECT_NAME/venv"
echo "Created virtual environment in $PROJECT_NAME/venv"

# Activate the virtual environment
source "$PROJECT_NAME/venv/bin/activate"

# Install basic dependencies (if any)
pip install --upgrade pip setuptools
pip freeze > "$PROJECT_NAME/requirements.txt"
echo "Created requirements.txt with installed packages"

# Initialize a Git repository
cd "$PROJECT_NAME"
git init
echo "Initialized empty Git repository in $PROJECT_NAME"

# Create a .gitignore file
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
echo ".env" >> .gitignore
echo "logs/" >> .gitignore
echo "Created .gitignore"

echo "Project structure for '$PROJECT_NAME' created successfully!"
