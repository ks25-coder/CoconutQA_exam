import pytest
import requests
from utils.data_generator import DataGenerator
from clients.api_manager import ApiManager
from config.credentials import ADMIN_EMAIL, ADMIN_PASSWORD


@pytest.fixture(scope="session")
def session():
    http_session = requests.Session()
    yield http_session
    http_session.close()


@pytest.fixture(scope="session")
def api_manager(session):
    return ApiManager(session)


@pytest.fixture(scope="session")
def authenticated_admin(api_manager):
    api_manager.auth_api.authenticate((ADMIN_EMAIL, ADMIN_PASSWORD))


@pytest.fixture(scope="function")
def test_movie():
    return {
        "name": DataGenerator.generate_random_movie_name(),
        "imageUrl": "https://example.com/image.png",
        "price": DataGenerator.generate_random_price(),
        "description": DataGenerator.generate_random_description(),
        "location": DataGenerator.generate_random_location(),
        "published": DataGenerator.generate_random_published(),
        "genreId": DataGenerator.generate_random_genre_id()
    }


@pytest.fixture(scope="function")
def created_movie(api_manager, test_movie, authenticated_admin):
    response = api_manager.movies_api.create_movie(test_movie)
    movie = response.json()
    yield movie
    api_manager.movies_api.delete_movie(movie["id"])
