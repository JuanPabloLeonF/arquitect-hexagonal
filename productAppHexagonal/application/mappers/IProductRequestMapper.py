from abc import ABC, abstractmethod

class IProductRequestMapper(ABC):

    @abstractmethod
    def mapProductModelToProductRequest(self, productModel):
        pass

    @abstractmethod
    def mapProductRequestToProductModel(self, productRequest):
        pass