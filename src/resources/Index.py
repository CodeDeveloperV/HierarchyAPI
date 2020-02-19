from flask_restful import Resource
from flask import redirect


class Index(Resource):
    def get(self):
        return "Congrats! Your endpoint is working"
