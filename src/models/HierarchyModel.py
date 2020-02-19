from . import db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Hierarchy(db.Model):
    ___tablename___ = 'hierarchy'

    id = db.Column(db.Integer, primary_key=True)
    hierarchy_node_type_id = db.Column(db.Integer,
                                       db.ForeignKey('hierarchy_node_type.id'),
                                       nullable=False)
    hierarchy_node_type = db.relationship('HierarchyNodeType',
                                          backref='node_types')
    predecessor_id = db.Column(db.Integer, db.ForeignKey('hierarchy.id'),
                               nullable=False)
    company = db.Column(db.Integer)
    is_active = db.Column(db.Boolean)


class HierarchyNodeTypeModel(db.Model):
    # table name
    __tablename__ = 'hierarchy_node_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean, default=False)

    @classmethod
    def get_node_types(cls):
        return cls.query.all()

    def insert(self, name, is_active):
        node_type = HierarchyNodeTypeModel(name=name, is_active=is_active)
        db.session.add(node_type)
        db.session.commit()

# class UserHierarchy(db.Model):
#     """
#     User Hierarchy model
#     """
#     
#     # table name 
#     __
