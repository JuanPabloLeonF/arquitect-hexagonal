from flask import jsonify
from entities import ProductEntity
from mappers import IProductEntityMapper
import json
from abc import ABC, abstractmethod

class IProductRepository(ABC):

    def __init__(self, iProductEntityMapper: IProductEntityMapper):
        self.iProductEntityMapper = iProductEntityMapper

    @abstractmethod
    def getAll(self):
        products = ProductEntity.query.all()
        productsList = [self.iProductEntityMapper.mapProductEntityToProduct(product) for product in products]
        return productsList