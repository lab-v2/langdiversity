import os
from dotenv import load_dotenv

from langdiversity.utils import PromptSelection, DiversityMeasureCollector
from langdiversity.models import OpenAIModel
from langdiversity.measures import ShannonEntropyMeasure
from langdiversity.parser import extract_last_letters

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

diversity_measure = ShannonEntropyMeasure()
model = OpenAIModel(openai_api_key=openai_api_key, extractor=extract_last_letters)

prompts = [
    "At the end, say 'the answer is [put the concatenated word here]'.\nQuestion: Take the last letter of each word in \"Tal Evan Lesley Sidney\" and concatenate them..",
    "At the end, say 'the answer is [put the concatenated word here]'.\nQuestion: Concatenate the last letter of each word in \"Tal Evan Lesley Sidney\".",
    "At the end, say 'the answer is [put the concatenated word here]'.\nQuestion: Combine the last letter of each word in \"Tal Evan Lesley Sidney\".",
]

diversity_collector = DiversityMeasureCollector(model=model, num_responses=4, diversity_measure=diversity_measure)
diversity_collector.collect(prompts, verbose=True)  

prompt_selection = PromptSelection(data=diversity_collector.data, selection="min")
selected_prompt, selected_diversity = prompt_selection.select() 

print("SELECTED PROMPT:", selected_prompt)
print("SELECTED DIVERSITY:", selected_diversity)
