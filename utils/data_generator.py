import random
import uuid


class DataGenerator:

    @staticmethod
    def generate_random_movie_name():
        return "Test Movie " + str(uuid.uuid4())

    @staticmethod
    def generate_random_price():
        return random.randint(100, 1000)

    @staticmethod
    def generate_random_description():
        descriptions = ['An exciting adventure', 'A story about friendship', 'A mysterious journey']
        return random.choice(descriptions)

    @staticmethod
    def generate_random_location():
        locations = ['MSK', 'SPB']
        return random.choice(locations)

    @staticmethod
    def generate_random_published():
        published = [True, False]
        return random.choice(published)

    @staticmethod
    def generate_random_genre_id():
        genre_ids = [7, 8, 9, 10]
        return random.choice(genre_ids)
