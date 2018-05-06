from app.model.music_chart import MusicChartDocument


def search_music_charts(chart_site_name=None, chart_datetime=None):
    query = {}

    if chart_site_name is not None:
        query['site'] = chart_site_name

    if chart_datetime is not None:
        query['datetime'] = chart_datetime

    charts = MusicChartDocument.objects(**query)
    return charts