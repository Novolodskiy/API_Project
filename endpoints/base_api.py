class BaseApi:
    response = None
    status_code = None
    base_url = "http://167.172.172.115:52355"
    base_headers = {
        "Content-Type": "application/json"
    }

    def check_status_code_200(self):
        assert self.status_code < 300, f"Status code is not less than 300: {self.status_code}"

    def get_headers(self, token=None):
        headers = self.base_headers.copy()
        if token:
            headers["Authorization"] = f"{token}"
        return headers 