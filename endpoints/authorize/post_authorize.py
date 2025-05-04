from endpoints.authorize.base_authorize import BaseAuthorize
import requests
import allure

class PostAuthorize(BaseAuthorize):

    @allure.step("Получение токена авторизации")
    def post_authorize(self, name: str):
        data = {"name": name}
        self.response = requests.post(f"{self.url}", json=data, headers=self.get_headers())
        self.status_code = self.response.status_code
        print(self.response.json(), self.status_code)
        return self.response
    
    @allure.step("Проверка ответа от сервера")
    def check_response_body(self, name):
        assert self.response.json()["user"] == name, f"Имя не совпадает: {self.response.json()['user']}"
        assert self.response.json()["token"] != None, "Токен не создан"

    
