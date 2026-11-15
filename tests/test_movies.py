from utils.data_generator import DataGenerator


def test_get_movies(api_manager):
    response = api_manager.movies_api.get_movies()

    assert "movies" in response.json()
    assert isinstance(response.json()["movies"], list)


def test_get_movie(api_manager, created_movie):
    movie_id = created_movie["id"]
    response = api_manager.movies_api.get_movie(movie_id)

    assert response.json()["id"] == movie_id
    assert response.json()["name"] == created_movie["name"]

def test_create_movie(api_manager, created_movie, test_movie):
    movie_id = created_movie["id"]

    get_response = api_manager.movies_api.get_movie(movie_id)

    assert get_response.json()["id"] == movie_id
    assert get_response.json()["name"] == test_movie["name"]
    assert get_response.json()["price"] == test_movie["price"]
    assert get_response.json()["location"] == test_movie["location"]
    assert get_response.json()["imageUrl"] == test_movie["imageUrl"]
    assert get_response.json()["description"] == test_movie["description"]
    assert get_response.json()["published"] == test_movie["published"]
    assert get_response.json()["genreId"] == test_movie["genreId"]


def test_update_movie(api_manager, created_movie):
    movie_id = created_movie["id"]

    update_data = {
        "name": DataGenerator.generate_random_movie_name(),
        "description": created_movie["description"],
        "price": created_movie["price"],
        "location": created_movie["location"],
        "imageUrl": created_movie["imageUrl"],
        "published": created_movie["published"],
        "genreId": created_movie["genreId"]
    }

    api_manager.movies_api.update_movie(movie_id, update_data)

    get_response = api_manager.movies_api.get_movie(movie_id)

    assert get_response.json()["name"] == update_data["name"]


def test_delete_movie(api_manager, test_movie, authenticated_admin):
    created_movie = api_manager.movies_api.create_movie(test_movie)
    movie_id = created_movie.json()["id"]

    api_manager.movies_api.delete_movie(movie_id)
    api_manager.movies_api.get_movie(movie_id, expected_status=404)


def test_get_movies_by_price(api_manager):
    response = api_manager.movies_api.get_movies(
        params={
        "minPrice": 100,
        "maxPrice": 500
        }
    )
    for movie in response.json()["movies"]:
        assert movie["price"] >= 100
        assert movie["price"] <= 500

def test_create_movie_negative(api_manager, test_movie, authenticated_admin):
    invalid_movie = test_movie.copy()
    invalid_movie.pop("name")

    api_manager.movies_api.create_movie(invalid_movie, expected_status=400)


def test_create_movie_duplicate(api_manager, created_movie, test_movie):
    api_manager.movies_api.create_movie(test_movie, expected_status=409)



def test_get_movies_id_negative(api_manager):
    api_manager.movies_api.get_movie(999999999, expected_status=404)


def test_update_negative(api_manager, test_movie, authenticated_admin):
    api_manager.movies_api.update_movie(movie_id=999999999, data=test_movie, expected_status=404)


def test_delete_movie_negative(api_manager, authenticated_admin):
    api_manager.movies_api.delete_movie(movie_id=999999999, expected_status=404)







