from mongoengine import *


class SongDocument(Document):
    meta = {
        'collection': 'song'
    }

    class RankDocument(EmbeddedDocument):
        melon = IntField()
        genie = IntField()
        bugs = IntField()

    title = StringField(required=True, unique=True)
    artist = StringField(required=True)
    album = StringField(required=True)
    rank = EmbeddedDocumentField(RankDocument)
