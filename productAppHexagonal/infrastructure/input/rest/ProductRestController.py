from flask import Blueprint, request, jsonify
from application.handlers.IProductHandler import IProductHandler

productRoute = Blueprint('product', __name__, url_prefix='/product')

class ProductRestController():

    def __init__(self, iProductHandler: IProductHandler):
        self.iProductHandler = iProductHandler

    @productRoute.route("/getAll", methods=["GET"])
    def getAll(self):
        return jsonify(self.IProductHandler.getAll()), 200