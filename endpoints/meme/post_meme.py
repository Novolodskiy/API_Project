from endpoints.meme.base_meme import BaseMeme
import requests
from test_s.test_meme.test_data.data import generate_meme_data
import allure

class PostMeme(BaseMeme):
    @allure.step("Добавление нового мема")
    def post_meme(self, cache_data, meme_data=None):
        if meme_data is None:
            meme_data = generate_meme_data()
        self.response = requests.post(
            self.url,
            json=meme_data,
            headers=self.get_headers(cache_data["token"])
        )
        self.status_code = self.response.status_code
        print(self.response.json(), self.status_code)
        return self.response
