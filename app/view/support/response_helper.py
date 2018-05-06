from flask import Response
import json


def unicode_safe_json_respnose(data, status_code=200, **kwargs):
    return Response(
        json.dumps(data),
        status_code,
        content_type="application/json; charset=utf8",
        **kwargs
    )
