from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message':'Store Not Found'},404

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db(store)
        return {'message':'The Store Has Been Deleted Fam!'}

    def post(self,name):
        if StoreModel.find_by_name(name):
            return {'message':'A Store With The Name {} Already Exists'.format(name)}
        store = StoreModel(name)
        try:
            store.save_to_db(store)
        except:
            return {'message':'An Error Has Occured While Inserting The Store!'},500
        return store.json(), 201

class StoreList(Resource):

    def get(self):
        return {'stores':[store.json() for store in StoreModel.query.all()]}
