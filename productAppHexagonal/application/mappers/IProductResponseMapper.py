from abc import ABC, abstractmethod

class IProductResponseMapper(ABC):

    @abstractmethod
    def mapProductModelToProductResponse(self, productModel):
        pass

    @abstractmethod
    def mapProductResponseToProductModel(self, productResponse):
        pass