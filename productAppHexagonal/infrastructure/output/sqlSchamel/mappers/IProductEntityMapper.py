from abc import ABC, abstractmethod

class IProductEntityMapper(ABC):

    @abstractmethod
    def mapProductToProductEntity(self, product):
        pass

    @abstractmethod
    def mapProductEntityToProduct(self, productEntity):
        pass