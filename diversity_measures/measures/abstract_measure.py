import abc
import typing


class AbstractMeasure(abc.ABC):
    def generate(self, values: typing.List[typing.Hashable]) -> float:
        pass
