from app.model.music_chart import MusicChartDocument, SongDocument
from datetime import datetime as Datetime

from muse import melon, genie, bugs
from multiprocessing import Process

from util import process_logger
import time


def parse_music_chart_songs(site_name, songs):
    current_datetime = Datetime.now().replace(minute=0, second=0, microsecond=0)
    chart = MusicChartDocument(site=site_name, datetime=current_datetime)

    for s in songs:
        song = SongDocument(rank=s['rank'], title=s['title'], artist=s['artist'], album=s['album'])
        song.save()

        chart.songs.append(song)

    chart.save()


def parse_music_chart_site(site_name=None):
    songs = None

    if site_name is None:
        parse_music_chart_site('melon')
        parse_music_chart_site('genie')
        parse_music_chart_site('bugs')

    elif site_name == 'melon':
        songs = melon.get_real_time_chart_songs()

    elif site_name == 'genie':
        songs = genie.get_real_time_chart_songs()

    elif site_name == 'bugs':
        songs = bugs.get_real_time_chart_songs()

    if songs is not None:
        # logging for start chart parsing
        process_logger.log('info', 'parse {0} chart was started'.format(site_name))

        # parsing music chart songs
        parse_music_chart_songs(site_name, songs)

        # logging for finish chart parsing
        process_logger.log('info', 'parse {0} chart was finished'.format(site_name))


def run():
    MusicChartDocument.drop_collection()

    Process(name='melon-chart-parser', target=parse_music_chart_site, args=('melon',)).start()
    Process(name='genie-chart-parser', target=parse_music_chart_site, args=('genie',)).start()
    Process(name='bugs-chart-parser', target=parse_music_chart_site, args=('bugs',)).start()
