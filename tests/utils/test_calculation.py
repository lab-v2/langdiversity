# import unittest
# import os
# from dotenv import load_dotenv
# from langdiversity.models import OpenAIModel
# from langdiversity.utils import DiversityCalculator
# from langdiversity.parser import extract_last_letters

# load_dotenv()
# openai_api_key = os.getenv("OPENAI_API_KEY")

# #TODO: The extractor usage might be sus???
# class TestDiversityMeasuresOnLLMResponses(unittest.TestCase):

#     def setUp(self):
#         self.openai_model = OpenAIModel(openai_api_key=openai_api_key, model="gpt-3.5-turbo", extractor=extract_last_letters)
#         self.diversity_calculator = DiversityCalculator()

#     def test_langdiversity(self):
#         ll_question = "Take the last letter of each word in \"Tal Evan Lesley Sidney\" and concatenate them."
#         prompt = f"At the end, say 'the answer is [put the concatenated word here]'.\nQuestion: {ll_question}.\n "
#         responses = self.openai_model.generate(prompt, count=5)
        
#         diversity_scores = self.diversity_calculator.calculate(responses, measures=['entropy', 'gini'])
        
#         print("LLM Responses:", responses)
#         print("Diversity Scores:", diversity_scores)
