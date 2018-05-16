from app.view.support import api_helper, response_helper
from app.model.support import mongo_helper

from flask import Blueprint, request
from flask_restful import Api, Resource

api = Api(Blueprint('song-api', __name__))


@api.resource('/song')
class SongResource(Resource):
    def get(self):
        song_title = request.args.get('song_title')
        songs = api_helper.search_songs(song_title=song_title)

        page_index = int(request.args.get('page_index', 1))
        page_length = int(request.args.get('page_length', 5))

        songs = api_helper.paging_items(songs, page_index, page_length)
        song_dicts = mongo_helper.mongo_list_to_python_list(songs)

        return response_helper.unicode_safe_json_respnose(song_dicts)
