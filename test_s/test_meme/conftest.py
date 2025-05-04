import pytest
from endpoints.meme.get_meme import GetMemes
from endpoints.meme.get_meme_id import GetMemeById
from endpoints.meme.post_meme import PostMeme
from endpoints.meme.put_meme import PutMeme
from endpoints.meme.delete_meme import DeleteMeme


@pytest.fixture()
def create_get_all_memes_endpoint():
    return GetMemes()

@pytest.fixture()
def create_get_meme_by_id_endpoint():
    return GetMemeById()

@pytest.fixture()
def create_post_meme_endpoint():
    return PostMeme()

@pytest.fixture()
def create_put_meme_endpoint():
    return PutMeme()

@pytest.fixture()
def create_delete_meme_endpoint():
    return DeleteMeme()

@pytest.fixture()
def meme_for_test(create_post_meme_endpoint, create_delete_meme_endpoint, create_token_for_test):
    response = create_post_meme_endpoint.post_meme(create_token_for_test)
    meme_id = response.json().get("id")
    yield meme_id
    create_delete_meme_endpoint.delete_meme(meme_id, create_token_for_test)
