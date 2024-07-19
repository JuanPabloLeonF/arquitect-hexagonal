from flask import jsonify
from productApp.models import ProductModel
from productApp.dtos import ProductDTO
from productApp.configuration import db
from sqlalchemy.exc import IntegrityError
import json

class ProductRepository():

    @staticmethod
    def getAll():
        products = ProductModel.query.all()
        productsList = [ProductDTO.serialize(product) for product in products]
        return productsList

    @staticmethod
    def getById(id):
            product = ProductModel.query.get(id)
            if not product:
                raise ValueError(f"Objeto no encontrado con el id: {id}")
            return ProductDTO.serialize(product=product)

    @staticmethod
    def create(product):
        try:
            productModel = ProductModel(name=product.get('name'),code=product.get('code'),price=product.get('price'))
            db.session.add(productModel)
            db.session.commit()
            return ProductDTO.serialize(productModel)
        except IntegrityError as e:
            db.session.rollback()
            raise e
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def updateById(product, id):
        try:
            productGet = ProductModel.query.get(id)
            if not productGet:
                raise ValueError(f"Objeto no encontrado con el id: {id}")

            productGet.name = product.get('name', productGet.name)
            productGet.code = product.get('code', productGet.code)
            productGet.price = product.get('price', productGet.price)
            db.session.commit()
            return ProductDTO.serialize(productGet)
        except IntegrityError as e:
            db.session.rollback()
            raise e
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def deleteById(id):
        try:
            productGet = ProductModel.query.get(id)
            if not productGet:
                raise ValueError(f"Objeto no encontrado con el id: {id}")
            db.session.delete(productGet)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e