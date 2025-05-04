from endpoints.base_api import BaseApi

class BaseAuthorize(BaseApi):
    url = BaseApi.base_url + "/authorize"