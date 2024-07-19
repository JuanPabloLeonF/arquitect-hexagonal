class ProductDTO():
    def __init__(self, id, name, code, price):
        self.id = id
        self.name = name
        self.code = code
        self.price = price

    @staticmethod
    def serialize(product):
        return {
            'id': product.id,
            'name': product.name,
            'code': product.code,
            'price': product.price
        }

class ResponseError():
    def __init__(self, statusCode, status, error):
        self.statusCode = statusCode
        self.status = status
        self.error = error

    @staticmethod
    def serialize(statusCode, status, error):
        return {
            'statusCode': statusCode,
            'status': status,
            'error': error
        }