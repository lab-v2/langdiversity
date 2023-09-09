# LangDiversity Python Library

pypi project: https://pypi.org/project/langdiversity/

## Install

```bash
pip install langchain
```

## Usage

Example:

```python
from langdiversity.models import OpenAIModel
from langdiversity.measures import ShannonEntropyMeasure
from langdiversity.utils import PromptSelection

# Initialize the OpenAI model and diversity measure
model = OpenAIModel(openai_api_key="YOUR_OPENAI_API_KEY")
diversity_measure = ShannonEntropyMeasure()

# Use the PromptSelection utility
prompt_selection = PromptSelection(model=model, num_responses=10, diversity_measure=diversity_measure)

# Selects the prompt with the configured diversity measure criteria from the LLM's 10 responses
selected_prompt, selected_measure = prompt_selection.generate(["Your list of prompts here..."])

print("Selected Prompt:", selected_prompt)
print("Selected Measure:", selected_measure)
```

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
