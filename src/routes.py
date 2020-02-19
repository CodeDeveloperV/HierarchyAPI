from flask_restful import Api
from src.resources.Hierarchy import Hierarchy, HierarchyNodeType
from src.resources.Index import Index


api = Api(prefix='/api/v1/')

api.add_resource(Index, '/')
api.add_resource(Hierarchy, '/hierarchy/<int:hierarchy>')
api.add_resource(HierarchyNodeType, '/hierarchyNodes')
