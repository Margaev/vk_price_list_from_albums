import vk
import time


class Album:

    def __init__(self):
        self.token = '###'
        self.group_id = '###'

        self.session = vk.Session(self.token)
        self.api = vk.API(self.session)

        self.album = self.api.photos.getAlbums(owner_id=self.group_id, v='5.87')

    def get_album_titles(self):
        album_titles = []
        for item in self.album['items']:
            album_titles.append(item['title'])
        return album_titles

    def get_albums(self):
        return self.album

    def get_photos(self, album_ids):
        photos = {}
        for album_id in album_ids:
            offset = 1
            photos[album_id] = []
            while True:
                response = self.api.photos.get(owner_id=self.group_id, album_id=album_id, extended=1,
                                               offset=offset, count=100, v='5.87')
                photos[album_id].extend(response['items'])
                offset += 100
                time.sleep(0.3)
                if len(response['items']) < 100:
                    break
        return photos
