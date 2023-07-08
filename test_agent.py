#try:
from langchain_app import Agent
#except ImportError:
#    #import sys
#    #import os
#    #sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#    from ..langchain_app import Agent

from dotenv import load_dotenv
import os
import pytest


@pytest.fixture
def dummy_string_EN():
    return "What would be a good company name for a company that makes colorful socks?"

@pytest.mark.aaa
def test_load_language_models(dummy_string_EN):
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")

    a = Agent(API_KEY, 0.9)
    tee = a.llm.predict(dummy_string_EN)
    print(tee)
    assert  True == True

@pytest.mark.bbb
def test_print_fixture(dummy_string_EN):
    d = dummy_string_EN
    print(d)
    assert  True == False 