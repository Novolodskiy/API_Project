from endpoints.authorize.base_authorize import BaseAuthorize
import requests
import allure


class GetAuthorizeToken(BaseAuthorize):

    @allure.step("Проверка токена авторизации")
    def get_authorize_token(self, cache_data):
        self.response = requests.get(f"{self.url}/{cache_data['token']}", headers=self.get_headers())
        self.status_code = self.response.status_code
        print(self.response.text, self.status_code)
        return self.response
    