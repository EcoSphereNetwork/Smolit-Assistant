import pytest
from app.agents.localai_agent import query_localai
from app.agents.openai_agent import query_openai
from app.agents.shellgpt_agent import execute_shell_command

def test_localai_agent(monkeypatch):
    def mock_post(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        return MockResponse({"response": "This is a mock response from LocalAI"}, 200)

    monkeypatch.setattr("requests.post", mock_post)

    response = query_localai("What's the weather?")
    assert response == "This is a mock response from LocalAI"

def test_openai_agent(monkeypatch):
    def mock_completion_create(*args, **kwargs):
        class MockResponse:
            def __init__(self):
                self.choices = [{"text": "This is a mock response from OpenAI"}]

        return MockResponse()

    monkeypatch.setattr("openai.Completion.create", mock_completion_create)

    response = query_openai("Tell me a joke")
    assert response == "This is a mock response from OpenAI"

def test_shellgpt_agent():
    response = execute_shell_command("ls")
    assert "Error" not in response
    response = execute_shell_command("rm -rf /")  # Should be disallowed
    assert "Error: Command 'rm' is not allowed." in response
