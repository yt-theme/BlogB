from mongoengine import *
connect('blog')

class User(Document):
    username = StringField(reequired=True)
    website  = URLField()
    tags     = ListField(StringField(max_length=16))