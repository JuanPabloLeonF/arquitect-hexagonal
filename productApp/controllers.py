from flask import Blueprint, request
from productApp.services import ProductService

productRoute = Blueprint('product', __name__, url_prefix='/product')

@productRoute.route("/getAll", methods=["GET"])
def getAll():
    return ProductService.getAll()

@productRoute.route("/getById/<string:id>", methods=["GET"])
def getById(id):
    return ProductService.getById(id)

@productRoute.route("/create", methods=["POST"])
def create():
    productData = request.data
    return ProductService.create(productData)

@productRoute.route("/updateById/<string:id>", methods=["PUT"])
def updateById(id):
    productData = request.data
    return ProductService.updateById(productData, id)

@productRoute.route("/deleteById/<string:id>", methods=["DELETE"])
def deleteById(id):
    return ProductService.deleteById(id)
