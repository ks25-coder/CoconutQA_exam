from clients.movies_api import MoviesApi
from clients.auth_api import AuthApi
from config.base_urls import API_BASE_URL

class ApiManager:
    def __init__(self, session):
        self.movies_api = MoviesApi(session, API_BASE_URL)
        self.auth_api = AuthApi(session)