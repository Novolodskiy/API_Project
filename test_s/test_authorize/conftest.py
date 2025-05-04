import pytest
from endpoints.authorize.get_authorize_token import GetAuthorizeToken
from endpoints.authorize.post_authorize import PostAuthorize


@pytest.fixture()
def create_get_authorize_token_endpoint():
    return GetAuthorizeToken()

@pytest.fixture()
def create_post_authorize_endpoint():
    return PostAuthorize()