import pytest
from faker import Faker

fake = Faker()


def test_post_authorize(create_post_authorize_endpoint, create_get_authorize_token_endpoint):
    name = f"{fake.first_name()}"
    create_post_authorize_endpoint.post_authorize(name)
    create_post_authorize_endpoint.check_status_code_200()
    create_post_authorize_endpoint.check_response_body(name)
    create_get_authorize_token_endpoint.get_authorize_token(create_post_authorize_endpoint.response.json())
    

def test_get_authorize_token(create_get_authorize_token_endpoint, create_token_for_test):
    create_get_authorize_token_endpoint.get_authorize_token(create_token_for_test)
    create_get_authorize_token_endpoint.check_status_code_200()