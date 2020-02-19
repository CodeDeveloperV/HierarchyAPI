from flask_restful import Resource
from flask import Response
from flask import jsonify
from ..models.HierarchyModel import HierarchyNodeTypeModel


class Hierarchy(Resource):
    def get(self, hierarchy):
        return jsonify(hierarchy=hierarchy)

    def post(self, hierarchy=None):
        if hierarchy is None:
            return


class HierarchyNodeType(Resource):

    def get(self):
        nodes = HierarchyNodeTypeModel.query.all()
        return nodes
