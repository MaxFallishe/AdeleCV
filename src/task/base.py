from abc import abstractmethod, ABC


class BaseTask(ABC):
    def __init__(self, dataset):
        self.dataset = dataset
