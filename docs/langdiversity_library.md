# LangDiversity Python Library

pypi project: https://pypi.org/project/langdiversity/

## Install

```bash
pip install langdiversity
```

## Usage

Example:

```python
import os
from dotenv import load_dotenv

from langdiversity.utils import PromptSelection, DiversityMeasureCollector
from langdiversity.models import OpenAIModel
from langdiversity.measures import ShannonEntropyMeasure
from langdiversity.parser import extract_last_letters  # Select a parser that suits your question set

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")  # place your language model's API key in a .env file

# Initialize the OpenAI model and diversity measure
model = OpenAIModel(openai_api_key=openai_api_key, extractor=extract_last_letters)
diversity_measure = ShannonEntropyMeasure()

# Define your list of prompts
prompts = [
    "At the end, say 'the answer is [put the concatenated word here]'.\nQuestion: Take the last letter of each word in \"Tal Evan Lesley Sidney\" and concatenate them..",
    # ... Add more prompts as needed
]

# Create an instance of DiversityMeasureCollector and collect diversity measures
diversity_collector = DiversityMeasureCollector(model=model, num_responses=4, diversity_measure=diversity_measure)
diversity_collector.collect(prompts)

# Create an instance of PromptSelection and select a prompt
prompt_selection = PromptSelection(data=diversity_collector.data, selection="min")
selected_prompt, selected_measure = prompt_selection.select()

print("Selected prompt:", selected_prompt)
print("Selected measure:", selected_measure)
```

### Modules:

LangDiversity offers a variety of modules for different use-cases. Below are the essential modules you can either directly import or use as a foundation for creating your own custom solutions:

- [Language Models](https://github.com/lab-v2/langdiversity/tree/main/langdiversity/models) (`langdiversity.models`)

  - `OpenAIModel`: Interfaces with OpenAI's GPT models.

- [Diversity Measures](https://github.com/lab-v2/langdiversity/tree/main/langdiversity/measures) (`langdiversity.measures`)

  - `ShannonEntropyMeasure`: Implements Shannon's entropy as a diversity measure.
  - `GiniImpurityMeasure`: Implements Gini Impurity as a diversity measure.

- [Utility Classes](https://github.com/lab-v2/langdiversity/tree/main/langdiversity/utils) (`langdiversity.utils`)

  - `PromptSelection`: Handles the selection of prompts based on diversity measures.
  - `DiversityMeasureCollector`: Collects diversity measures for a given set of prompts using a specified language model and diversity measure algorithm.

- [Parsers](https://github.com/lab-v2/langdiversity/tree/main/langdiversity/parser) (`langdiversity.parsers`)
  - `extract_last_letters(response: str)`: Extracts the last letters of each word in the response.
  - `extract_math_answer(response: str)`: Extracts numerical answers from a mathematical question in the response.
  - `extract_multi_choice_answer(response: str)`: Extracts the selected choice (A, B, C, D, E) from a multiple-choice question in the response.

### DiversityMeasureCollector Paramaters:

- `model`: The language model you want to use. In this example, we're using OpenAI's model.

- `diversity_measure`: The measure of diversity measure you want to use. Here, we're using entropy.

- `num_responses`: The number of responses you want the model to generate for each prompt. Default is 1.

### PromptSelection Parameters:

- `data`: A list of dictionaries, each containing information about a prompt, the responses it generated, and its diversity measure. This data is collected using the `DiversityMeasureCollector` class.

- `selection`: Determines how the best prompt is selected based on its diversity measure. It can be:

  - `"min"`: Selects the prompt with the minimum diversity measure. (default)
  - `"max"`: Selects the prompt with the maximum diversity measure.

### Output:

- `selected_prompt`: The prompt that meets the specified diversity criteria (either min or max) among the given list of prompts.
- `selected_measure`: The diversity measure of the `selected_prompt` based on the specified diversity measure (e.g., entropy).
