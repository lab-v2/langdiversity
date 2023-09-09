import unittest
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

from langdiversity.models import OpenAIModel

class TestOpenAI(unittest.TestCase):
    def test_basic(self):
        openai_model = OpenAIModel(openai_api_key=openai_api_key, model="gpt-3.5-turbo")
        response = openai_model.generate("hi", count=2)
        print(response)