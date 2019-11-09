import os
import requests


class MovieDB:

    def __init__(self, id):

        # self.TMDB_API_KEY = os.getenv('TMDB_API_KEY')
        self.base_url = f"https://api.themoviedb.org/3/movie/{id}"
        self.headers = {
            "Authorization": f"Bearer {os.environ['TMDB_API_KEY']}",
        }

    def get_movie(self):
        return requests.get(self.base_url, headers=self.headers).json()