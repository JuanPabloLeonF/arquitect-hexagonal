from domain.spi.IProductPersistencePort import IProductPersistencePort
from sqlSchamel.repositories import IProductRepository

class ProductAdapter(IProductPersistencePort):

    def __init__(self, iProductRepository: IProductRepository):
        self.iProductRepository = iProductRepository

    #OVERRIDE
    def getAll(self):
        return self.iProductRepository.getAll()