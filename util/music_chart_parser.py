from app.model.song import SongDocument

from muse import melon, genie, bugs
from util import process_logger


def parse_music_chart_songs(site_name, songs):
    for s in songs:
        song = SongDocument.objects(title=s['title'])

        query = {
            'set__title': s['title'],
            'set__artist': s['artist'],
            'set__album': s['album'],
            'set__rank__{}'.format(site_name): s['rank']
        }

        song.modify(**query, upsert=True)


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
        process_logger.log('info', 'parse {} chart was started'.format(site_name))
        parse_music_chart_songs(site_name, songs)
        process_logger.log('info', 'parse {} chart was finished'.format(site_name))


def parse():
    SongDocument.drop_collection()

    parse_music_chart_site('melon')
    parse_music_chart_site('genie')
    parse_music_chart_site('bugs')
