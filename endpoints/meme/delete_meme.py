from endpoints.meme.base_meme import BaseMeme
import requests
import allure

class DeleteMeme(BaseMeme):
    
    @allure.step("Удаление мема")
    def delete_meme(self, meme_id: int, cache_data):
        url = f"{self.url}/{meme_id}"
        self.response = requests.delete(url, headers=self.get_headers(cache_data["token"]))
        self.status_code = self.response.status_code
        print(self.response.text, self.status_code)
        return self.response
