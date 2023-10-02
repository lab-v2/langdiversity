# LangDiversity Python Library

pypi project: https://pypi.org/project/langdiversity/

## Table of Contents

- [Installation](#installation)
- [Utilties](#utilities)
  - [Diversity Measures Utility](#diversity-measures-utility)
  - [Prompt Selection Utility](#prompt-selection-utility)
- [Modules](#modules)

## Installation

```bash
pip install langdiversity
```

## Utilities

### Diversity Measures Utility

Example:

```python
from langdiversity.measures import ShannonEntropyMeasure
from langdiversity.models import OpenAIModel
from langdiversity.utils import DiversityMeasureCollector

diversity_measure = ShannonEntropyMeasure()

model = OpenAIModel(openai_api_key="[YOUR-API-KEY-HERE]")

prompts = [
  # List of prompts/questions to be processed...
]

diversity_collector = DiversityMeasureCollector(model=model, num_responses=5, diversity_measure=diversity_measure)
diversity_collector.collect(prompts, verbose=True)
```

### Prompt Selection Utility

Example:

```python
# Continuing from the implementation above...

from langdiversity.utils import PromptSelection
prompt_selection = PromptSelection(data=diversity_collector.data, selection="min")
selected_data = prompt_selection.select()
```

## Modules:

LangDiversity offers a variety of modules for different use-cases. Below are the essential modules you can either directly import or use as a foundation for creating your own custom solutions:

- [Language Models](https://github.com/lab-v2/langdiversity/tree/main/langdiversity/models) (`langdiversity.models`)

  - `OpenAIModel`: A wrapper around Langchain's ChatOpenAI to interact with OpenAI's GPT models, facilitating the generation of responses based on a provided message. It supports optional response extraction for further processing.

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

- `num_responses`: The number of responses you want the model to generate for each prompt.

### PromptSelection Parameters:

- `data`: A list of dictionaries, each containing information about a prompt, the responses it generated, and its diversity measure. This data is collected using the `DiversityMeasureCollector` class.

- `selection`: Determines how the best prompt is selected based on its diversity measure. It can be:

  - `"min"`: Selects the prompt with the minimum diversity measure. (default)
  - `"max"`: Selects the prompt with the maximum diversity measure.

### Output:

- `selected_data`: A dictionary containing:
  - `selected_prompts`: A list of selected prompts based on the specified diversity criteria (either min or max).
  - `diversity`: The diversity score of these selected prompts, based on the specified diversity measure (e.g., entropy).
