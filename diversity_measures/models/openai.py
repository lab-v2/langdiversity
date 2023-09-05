import abc
from typing import List, Optional, Callable

import openai

from .abstract_base_model import AbstractBaseModel

class OpenAIModel(AbstractBaseModel):
    def __init__(
        self, 
        openai_api_key: str, 
        model: str = "gpt-3.5-turbo", 
        extractor: Optional[Callable] = None,
        *args, **kwargs
    ):
        openai.api_key = openai_api_key
        self.kwargs = kwargs
        if 'n' in self.kwargs: del self.kwargs['n']

        self.model = model
        self.extractor = extractor

    def generate(self, message: str, count: int = 1):
        messages = [{"role": "user", "content": message}]

        response = openai.ChatCompletion.create(
            model=self.model, messages=messages, **self.kwargs, n=count, 
        )

        parsed_response = self.__parse_response(response)
        
        # Apply the extractor if provided
        if self.extractor:
            parsed_response = [self.extractor(resp) for resp in parsed_response]
        
        return parsed_response

    def __parse_response(self, response: dict):
        choices = response["choices"]
        messages = [choice["message"]["content"] for choice in choices]
        return messages
