from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel' , lazy='dynamic')


    def __init__(self,name):
        self.name = name

    def json(self):
        return {'name':self.name,'items':[item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def save_to_db(cls,item):
        db.session.add(item)
        db.session.commit()

    @classmethod
    def delete_from_db(cls,item):
        db.session.delete(item)
        db.session.commit()
