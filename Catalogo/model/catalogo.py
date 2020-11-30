from mongoengine import *

class Catalogo(Document):
    nome = StringField(required=True)
    individuos = ListField(required=True)
    userId = ObjectIdField(required=True)