from endpoints.meme.base_meme import BaseMeme
import requests
from test_s.test_meme.test_data.data import generate_meme_data
import allure

class PutMeme(BaseMeme):
    @allure.step("Изменение существующего мема")
    def put_meme(self, meme_id: int, cache_data, meme_data=None):
        if meme_data is None:
            meme_data = generate_meme_data()
        self.response = requests.put(
            f"{self.url}/{meme_id}",
            json={**meme_data, "id": meme_id},
            headers=self.get_headers(cache_data["token"])
        )
        self.status_code = self.response.status_code
        print(self.response.json(), self.status_code)
        return self.response
