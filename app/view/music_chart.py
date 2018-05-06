from app.view.support import api_helper, response_helper
from app.model.support import mongo_helper

from datetime import datetime as Datetime
from flask import Blueprint, request
from flask_restful import Api, Resource

api = Api(Blueprint('music-chart-api', __name__))


@api.resource('/chart')
class MusicChartResource(Resource):
    def get(self):
        chart_site_name = request.args.get('chart_site_name')

        charts = api_helper.search_music_charts(chart_site_name=chart_site_name)
        chart_dicts = mongo_helper.mongo_list_to_python_list(charts)

        return response_helper.unicode_safe_json_respnose(chart_dicts)
