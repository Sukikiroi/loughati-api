from flask import request
from flask_restful import Resource
from .model import User

class Register(Resource):
    def post(self):
        data = request.get_json()
        print(data)
