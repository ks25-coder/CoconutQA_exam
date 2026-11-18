from custom_requester.custom_requester import CustomRequester

MOVIES = "/movies"

class MoviesApi(CustomRequester):
    def __init__(self, session, base_url):
        super().__init__(session=session, base_url=base_url)

    def get_movies(self, expected_status=200, **kwargs):
        return self.send_request(
            method="GET",
            endpoint=MOVIES,
            expected_status=expected_status,
            **kwargs
        )

    def create_movie(self, data, expected_status=201, **kwargs):
        return self.send_request(
            method="POST",
            endpoint=MOVIES,
            expected_status=expected_status,
            data=data,
            **kwargs
        )

    def get_movie(self, movie_id, expected_status=200, **kwargs):
        return self.send_request(
            method="GET",
            endpoint=f'{MOVIES}/{movie_id}',
            expected_status=expected_status,
            **kwargs
        )

    def delete_movie(self, movie_id, expected_status=200, **kwargs):
        return self.send_request(
            method="DELETE",
            endpoint=f'{MOVIES}/{movie_id}',
            expected_status=expected_status,
            **kwargs
        )

    def update_movie(self, movie_id, data, expected_status=200, **kwargs):
        return self.send_request(
            method="PATCH",
            endpoint=f'{MOVIES}/{movie_id}',
            expected_status=expected_status,
            data=data,
            **kwargs
        )
