from abc import ABC, abstractmethod

#aqui recibe las request y devuelve responses
class IProductHandler(ABC):

    @abstractmethod
    def getAll(self):
        pass