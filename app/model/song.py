from mongoengine import *


class SongDocument(Document):
    rank = IntField(required=True)
    title = StringField(required=True)
    artist = StringField(required=True)
    album = StringField(required=True)