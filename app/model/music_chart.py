from mongoengine import *


class SongDocument(EmbeddedDocument):
    rank = IntField(required=True)
    title = StringField(required=True)
    artist = StringField(required=True)
    album = StringField(required=True)


class MusicChartDocument(Document):
    meta = {
        'collection': 'music_chart'
    }

    site = StringField(required=True)
    datetime = DateTimeField(required=True)
    songs = ListField(SongDocument, default=list)
