
def test_get_movies(api_manager):
    response = api_manager.movies_api.get_movies()

    assert response.status_code == 200
    assert "movies" in response.json()
    assert isinstance(response.json()["movies"], list)


def test_get_movie(api_manager, created_movie):
    movie_id = created_movie["id"]
    response = api_manager.movies_api.get_movie(movie_id)

    assert response.status_code == 200
    assert response.json()["id"] == movie_id
    assert response.json()["name"] == created_movie["name"]

def test_create_movie(created_movie, test_movie):
    assert created_movie["id"] is not None
    assert created_movie["name"] == test_movie["name"]
    assert created_movie["price"] == test_movie["price"]
    assert created_movie["location"] == test_movie["location"]
    assert created_movie["imageUrl"] == test_movie["imageUrl"]
    assert created_movie["description"] == test_movie["description"]
    assert created_movie["published"] == test_movie["published"]
    assert created_movie["genreId"] == test_movie["genreId"]


def test_update_movie(api_manager, created_movie):
    movie_id = created_movie["id"]

    update_data = {
        "name": "Updated Movie",
        "description": created_movie["description"],
        "price": created_movie["price"],
        "location": created_movie["location"],
        "imageUrl": created_movie["imageUrl"],
        "published": created_movie["published"],
        "genreId": created_movie["genreId"]
    }

    response = api_manager.movies_api.update_movie(movie_id, update_data)

    assert response.status_code == 200
    assert response.json()["name"] == "Updated Movie"


def test_delete_movie(api_manager, test_movie, authenticated_admin):
    created_movie = api_manager.movies_api.create_movie(test_movie)
    movie_id = created_movie.json()["id"]

    delete_response = api_manager.movies_api.delete_movie(movie_id)
    assert delete_response.status_code == 200, \
        f"Ожидался статус 200, получен {delete_response.status_code}"

    get_response = api_manager.movies_api.get_movie(movie_id, expected_status=404)
    assert get_response.status_code == 404, \
        f"Ожидался статус 404, получен {get_response.status_code}"


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
    test_movie.pop("name")
    response = api_manager.movies_api.create_movie(test_movie, expected_status=400)
    assert response.status_code == 400

def test_create_movie_duplicate(api_manager, created_movie, test_movie):
    response = api_manager.movies_api.create_movie(test_movie, expected_status=409)
    assert response.status_code == 409


def test_get_movies_id_negative(api_manager):
    response = api_manager.movies_api.get_movie(999999999, expected_status=404)
    assert response.status_code == 404


def test_update_negative(api_manager, test_movie, authenticated_admin):
    response = api_manager.movies_api.update_movie(movie_id=999999999, data=test_movie, expected_status=404)
    assert response.status_code == 404

def test_delete_movie_negative(api_manager, authenticated_admin):
    response = api_manager.movies_api.delete_movie(movie_id=999999999, expected_status=404)
    assert response.status_code == 404






