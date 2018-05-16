from app.model.song import SongDocument


def paging_items(items, page_index=1, page_length=5):
    start_index = (page_index - 1) * page_length
    finish_index = page_index * page_length

    items_sliced = items[start_index:finish_index]
    return items_sliced


def search_music_chart_songs(site_name):
    query = {
        'rank__' + site_name + '__exists': True
    }

    songs = SongDocument.objects(**query)
    songs = songs.order_by('rank.' + site_name)

    return songs


def search_songs(song_title=None):
    query = {}

    if song_title is not None:
        query['title'] = song_title

    songs = SongDocument.objects(**query)
    return songs
