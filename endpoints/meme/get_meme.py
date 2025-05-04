from endpoints.meme.base_meme import BaseMeme
import requests
import allure

class GetMemes(BaseMeme):

    @allure.step("Получение списка всех мемов")
    def get_memes(self, cache_data):
        self.response = requests.get(self.url, headers=self.get_headers(cache_data["token"]))
        self.status_code = self.response.status_code
        return self.response
