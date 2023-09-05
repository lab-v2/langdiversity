import abc
from typing import List

class AbstractBaseModel(abc.ABC):
    def generate(self, messages: List[List[dict]]):
        pass
