from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            return store.json()

        return {'message':"Store not found"}

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "The store with name '{}' already exists.".format(name)}

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error ouccred while inserting the store.'}

        return store.json()
    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'The store deleted.'}

class StoreList(Resource):
    """docstring for StroeList"""
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}