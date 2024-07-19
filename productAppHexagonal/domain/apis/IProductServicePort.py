from abc import ABC, abstractmethod

class IProductServicePort(ABC):

    @abstractmethod
    def getAll(self):
        pass