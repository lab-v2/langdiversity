import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

from langdiversity.measures import ShannonEntropyMeasure
diversity_measure = ShannonEntropyMeasure()

from langdiversity.models import OpenAIModel
from langdiversity.parser import extract_last_letters
model = OpenAIModel(openai_api_key=openai_api_key, extractor=extract_last_letters)

from langdiversity.utils import DiversityMeasureCollector

original_question = "\nAt the end, say 'the answer is [put the concatenated word here]'.\nQuestion: Take the last letter of each word in \"Tal Evan Lesley Sidney\" and concatenate them.."

fewshot_prompts = [
    f"Example 1: Concatenate the last letters of 'Hello World' -> 'od'\nExample 2: Concatenate the last letters of 'Python Ruby' -> 'ny'\nExample 3: Concatenate the last letters of 'Learning Teaching' -> 'gg'\nExample 4: Concatenate the last letters of 'Reading Writing' -> 'gg'\nExample 5: Concatenate the last letters of 'Singing Dancing' -> 'gg'{original_question}",
    f"Example 1: Get the last letters of 'Innovation Creation' and concatenate them -> 'nn'\nExample 2: Get the last letters of 'Motivation Dedications' and concatenate them -> 'ns'\nExample 3: Get the last letters of 'Education Solute' and concatenate them -> 'ne'\nExample 4: Get the last letters of 'Integration Pizza' and concatenate them -> 'na'\nExample 5: Get the last letters of 'Inspiration Aspire' and concatenate them -> 'ne'{original_question}",
    f"Example 1: For 'Dance Sing', the last letters when concatenated form -> 'eg'\nExample 2: For 'Jump School', the last letters when concatenated form -> 'pl'\nExample 3: For 'Run Walk', the last letters when concatenated form -> 'nk'\nExample 4: For 'Hop Jam', the last letters when concatenated form -> 'pm'\nExample 5: For 'Sit Stand', the last letters when concatenated form -> 'td'{original_question}",
    f"Example 1: From 'Cake Bake', the concatenated last letters are -> 'ee'\nExample 2: From 'Drive Ride', the concatenated last letters are -> 'ee'\nExample 3: From 'Love Live', the concatenated last letters are -> 'ee'\nExample 4: From 'Give Take', the concatenated last letters are -> 'ee'\nExample 5: From 'Make Bake', the concatenated last letters are -> 'ee'{original_question}",
    f"Example 1: 'Read Write' ends in -> 'de'\nExample 2: 'Play Stay' ends in -> 'yy'\nExample 3: 'Dream Scream' ends in -> 'mm'\nExample 4: 'Teach Reach' ends in -> 'hh'\nExample 5: 'Learn Earn' ends in -> 'nn'{original_question}"
]

diversity_collector = DiversityMeasureCollector(model=model, num_responses=4, diversity_measure=diversity_measure)
diversity_collector.collect(fewshot_prompts, verbose=True)  

from langdiversity.utils import PromptSelection
prompt_selection = PromptSelection(data=diversity_collector.data, selection="min")
selected_data = prompt_selection.select()

print(f"DIVERSITY SCORE: {selected_data['diversity']}")
print("SELECTED PROMPTS:")
for prompt in selected_data['selected_prompts']:
    print(prompt)
    print('-' * 80)  