from flask import jsonify, request
import json
from productApp.repositories import ProductRepository
from productApp.dtos import ProductDTO, ResponseError
from sqlalchemy.exc import IntegrityError

class ProductService():
    
    @staticmethod
    def getAll():
        return jsonify(ProductRepository.getAll()), 200

    @staticmethod
    def getById(id):
        try:
            return jsonify(ProductRepository.getById(id)), 200
        except ValueError as e:
            return jsonify(ResponseError.serialize(statusCode=400, status='BAD REQUEST', error=str(e))), 400
        except Exception as e:
            return jsonify(ResponseError.serialize(statusCode=500, status='INTERNAL SERVER ERROR', error=str(e))), 500

    @staticmethod
    def create(product):
        try:
            productData = json.loads(product)
            if not productData.get('name') or not productData.get('code') or not productData.get('price'):
                raise ValueError("Los campos no puden estar vacios")
            return jsonify(ProductRepository.create(productData)), 201
        except IntegrityError as e:
            return jsonify(ResponseError.serialize(statusCode=409, status='ALGUNOS DE LOS COMPOS YA EXISTE EN LA BASE DE DATOS', error=str(e))), 409
        except ValueError as e:
            return jsonify(ResponseError.serialize(statusCode=400, status='BAD REQUEST', error=str(e))), 400
        except Exception as e:
            return jsonify(ResponseError.serialize(statusCode=500, status='INTERNAL SERVER ERROR', error=str(e))), 500

    @staticmethod
    def updateById(product, id):
        try:
            productData = json.loads(product)
            if not productData.get('name') or not productData.get('code') or not productData.get('price'):
                raise ValueError("Los campos no puden estar vacios")
            return jsonify(ProductRepository.updateById(productData, id)), 200
        except IntegrityError as e:
            return jsonify(ResponseError.serialize(statusCode=409, status='ALGUNOS DE LOS COMPOS YA EXISTE EN LA BASE DE DATOS', error=str(e))), 409
        except ValueError as e:
            return jsonify(ResponseError.serialize(statusCode=400, status='BAD REQUEST', error=str(e))), 400
        except Exception as e:
            return jsonify(ResponseError.serialize(statusCode=500, status='INTERNAL SERVER ERROR', error=str(e))), 500

    @staticmethod
    def deleteById(id):
        try:
            ProductRepository.deleteById(id)
            return jsonify({'message': 'User deleted successfully'}), 200
        except ValueError as e:
            return jsonify(ResponseError.serialize(statusCode=404, status='NOT FOUND', error=str(e))), 404
        except Exception as e:
            return jsonify(ResponseError.serialize(statusCode=500, status='INTERNAL SERVER ERROR', error=str(e))), 500