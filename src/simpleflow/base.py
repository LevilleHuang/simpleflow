from abc import ABC, abstractmethod


class Task(ABC):

    @abstractmethod
    def execute(self, context: dict):
        raise NotImplementedError
