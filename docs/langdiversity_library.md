# LangDiversity Python Library

pypi project: https://pypi.org/project/langdiversity/

## Install

```bash
pip install langdiversity
```

## Usage

Example:

```python
from langdiversity.models import OpenAIModel
from langdiversity.measures import ShannonEntropyMeasure
from langdiversity.utils import PromptSelection
from langdiversity.parser import # Select a parser that suits your question set

# Initialize the OpenAI model and diversity measure
model = OpenAIModel(openai_api_key="[YOUR API KEY]", extractor="[SELECT YOUR PARSER](optional)")
diversity_measure = ShannonEntropyMeasure()

# Use the PromptSelection utility
prompt_selection = PromptSelection(model=model, num_responses=10, diversity_measure=diversity_measure)

# Pass in question set to the LLM & selects the prompt with the configured diversity measure criteria from the LLM's 10 responses
selected_prompt, selected_measure = prompt_selection.generate(["Your list of prompts here..."])

print("Selected Prompt:", selected_prompt)
print("Selected Measure:", selected_measure)
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
  - `DiversityCalculator`: Calculates various diversity measures for a given set of values. Supports Shannon's entropy and Gini impurity by default.

- [Parsers](https://github.com/lab-v2/langdiversity/tree/main/langdiversity/parser) (`langdiversity.parsers`)
  - `extract_last_letters(response: str)`: Extracts the last letters of each word in the response.
  - `extract_math_answer(response: str)`: Extracts numerical answers from a mathematical question in the response.
  - `extract_multi_choice_answer(response: str)`: Extracts the selected choice (A, B, C, D, E) from a multiple-choice question in the response.

### PromptSelection Paramaters:

- `model`: The language model you want to use. In this example, we're using OpenAI's model.

- `diversity_measure`: The measure of diversity measure you want to use. Here, we're using entropy.

- `num_responses`: The number of responses you want the model to generate for each prompt. Default is 1.

- `selection`: Determines how the best prompt is selected based on its diversity measure. It can be:

  - `"min"`: Selects the prompt with the minimum diversity measure. (default)
  - `"max"`: Selects the prompt with the maximum diversity measure.

### Output:

- `selected_prompt`: The prompt that meets the specified diversity criteria (either min or max) among the given list of prompts.
- `selected_measure`: The diversity measure of the `selected_prompt` based on the specified diversity measure (e.g., entropy).
