import pytest
from endpoints.authorize.post_authorize import PostAuthorize
from endpoints.authorize.get_authorize_token import GetAuthorizeToken
from faker import Faker

faker = Faker()

_cached_token = 'xOHClaXJN59Vg6s'
_cached_name = 'William'


def is_token_alive(cached_token, cached_name):
    cached_data = {"token": cached_token, "name": cached_name}
    checker = GetAuthorizeToken()
    response = checker.get_authorize_token(cached_data)
    return response.status_code == 200

@pytest.fixture()
def create_token_for_test():
    global _cached_token, _cached_name
    if _cached_token and is_token_alive(_cached_token, _cached_name):
        cached_data = {"token": _cached_token, "name": _cached_name}
        print('Token True')
        return cached_data
    # Генерируем новый токен и имя
    post_auth = PostAuthorize()
    post_auth.post_authorize(faker.first_name())
    _cached_token = post_auth.response.json()["token"]
    _cached_name = post_auth.response.json()["user"]
    cached_data = {"token": _cached_token, "name": _cached_name}
    return cached_data
