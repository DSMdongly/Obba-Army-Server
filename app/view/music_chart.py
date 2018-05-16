from app.doc.music_chart import MUSIC_CHART_GET_SPEC
from app.view.support import api_helper, response_helper
from app.model.support import mongo_helper

from flask import Blueprint, request
from flask_restful import Api, Resource
from flasgger import swag_from

api = Api(Blueprint('music-chart-api', __name__))


@api.resource('/chart')
class MusicChartResource(Resource):
    @swag_from(MUSIC_CHART_GET_SPEC)
    def get(self):
        site_name = request.args['site_name']
        songs = api_helper.search_music_chart_songs(site_name=site_name)

        page_index = int(request.args.get('page_index', 1))
        page_length = int(request.args.get('page_length', 5))

        songs = api_helper.paging_items(songs, page_index, page_length)
        song_dicts = mongo_helper.mongo_list_to_python_list(songs)

        return response_helper.unicode_safe_json_respnose(song_dicts)
