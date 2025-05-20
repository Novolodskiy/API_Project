
def test_get_all_memes(create_get_all_memes_endpoint, create_token_for_test):
    create_get_all_memes_endpoint.get_memes(create_token_for_test)
    create_get_all_memes_endpoint.check_status_code_200()

def test_post_meme(create_post_meme_endpoint, create_token_for_test):
    create_post_meme_endpoint.post_meme(create_token_for_test)
    create_post_meme_endpoint.check_status_code_200()

def test_get_meme_by_id(create_get_meme_by_id_endpoint, meme_for_test, create_token_for_test):
    create_get_meme_by_id_endpoint.get_meme_by_id(meme_for_test, create_token_for_test)
    create_get_meme_by_id_endpoint.check_status_code_200()

def test_put_meme(create_put_meme_endpoint, meme_for_test, create_token_for_test):
    create_put_meme_endpoint.put_meme(meme_for_test, create_token_for_test)
    create_put_meme_endpoint.check_status_code_200()

def test_delete_meme(create_delete_meme_endpoint, meme_for_test, create_token_for_test):
    create_delete_meme_endpoint.delete_meme(meme_for_test, create_token_for_test)
    create_delete_meme_endpoint.check_status_code_200()
