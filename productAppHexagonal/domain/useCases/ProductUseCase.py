from apis.IProductServicePort import IProductServicePort
from spi.IProductPersistencePort import IProductPersistencePort

class ProductUseCase(IProductServicePort):

    def __init__(self, iProductPersistencePort: IProductPersistencePort):
        self.iProductPersistencePort = iProductPersistencePort
    
    #OVERRIDE
    def getAll(self):
        print("implemento")
        return self.iProductPersistencePort.getAll()