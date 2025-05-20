
def test_meme_lifecycle(create_post_meme_endpoint, create_get_meme_by_id_endpoint, 
                       create_put_meme_endpoint, create_delete_meme_endpoint, 
                       create_token_for_test):
    
    # 1. Create a meme
    create_post_meme_endpoint.post_meme(create_token_for_test)
    create_post_meme_endpoint.check_status_code_200()
    meme_id = create_post_meme_endpoint.response.json()["id"]
    
    # 2. Get the meme by ID
    create_get_meme_by_id_endpoint.get_meme_by_id(meme_id, create_token_for_test)
    create_get_meme_by_id_endpoint.check_status_code_200()
    
    # 3. Update the meme
    create_put_meme_endpoint.put_meme(meme_id, create_token_for_test)
    create_put_meme_endpoint.check_status_code_200()
    
    # 4. Verify the update
    create_get_meme_by_id_endpoint.get_meme_by_id(meme_id, create_token_for_test)
    create_get_meme_by_id_endpoint.check_status_code_200()
    
    # 5. Delete the meme
    create_delete_meme_endpoint.delete_meme(meme_id, create_token_for_test)
    create_delete_meme_endpoint.check_status_code_200()
    
    # 6. Verify the meme is deleted
    create_get_meme_by_id_endpoint.get_meme_by_id(meme_id, create_token_for_test)
    create_get_meme_by_id_endpoint.check_status_code_404()
