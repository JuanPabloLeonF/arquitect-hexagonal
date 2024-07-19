from IProductHandler import IProductHandler
from domain.apis.IProductServicePort import IProductServicePort
from mappers.IProductRequestMapper import IProductRequestMapper
from mappers.IProductResponseMapper import IProductResponseMapper

class ProductHandlerImplementation(IProductHandler):

    def __init__(self, iProductServicePort: IProductServicePort, iProductRequestMapper: IProductRequestMapper, iProductResponseMapper: IProductResponseMapper):
        self.iProductServicePort = iProductServicePort
        self.iProductRequestMapper = iProductRequestMapper
        self.iProductResponseMapper = iProductResponseMapper

    #OVERRRIDE
    def getAll(self):
        print("implementacion")
        return self.iProductResponseMapper.mapProductModelToProductResponse(self.iProductServicePort.getAll())
