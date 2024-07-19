from abc import ABC, abstractmethod

class IProductPersistencePort(ABC):

    @abstractmethod
    def getAll(self):
        pass