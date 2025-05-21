from endpoints.meme.base_meme import BaseMeme
import requests
import allure

class GetMemeById(BaseMeme):
    
    @allure.step("Получение мема по id")
    def get_meme_by_id(self, meme_id: int, cache_data):
        url = f"{self.url}/{meme_id}"
        self.response = requests.get(url, headers=self.get_headers(cache_data["token"]))
        self.status_code = self.response.status_code
        print(self.response, self.status_code)
        return self.response
