import pytest
from app.models.router_model import RouterModel

def test_router_model():
    router = RouterModel()
    assert router.predict("What is the weather today?") == "question"
    assert router.predict("Turn on the lights") == "action"
    assert router.predict("Tell me a joke") == "statement"

    # Test for edge cases
    assert router.predict("unknown command") is not None

def test_model_save_load():
    router = RouterModel()
    router.save_model()
    router.load_model()
    assert router.predict("What is the weather today?") == "question"
