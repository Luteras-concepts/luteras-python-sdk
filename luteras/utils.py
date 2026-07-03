import requests

from .exceptions import LuterasAPIError, LuterasNetworkError


class RequestHandler:
    def __init__(self, base_url, api_key=None, token=None):
        self.api_key = api_key
        self.token = token
        self.base_url = base_url.rstrip("/")

    def headers(self):
        headers = {
            "Content-Type": "application/json"
        }

        if self.api_key:
            headers["x-api-key"] = self.api_key

        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        return headers

    def request(self, method, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"

        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers(),
                json=data,
                timeout=15
            )
        except requests.RequestException as exc:
            raise LuterasNetworkError(f"Network error: {exc}") from exc

        try:
            result = response.json()
        except ValueError:
            result = {"error": response.text}

        if not response.ok:
            message = (
                result.get("error")
                or result.get("message")
                or "LUTERAS API request failed"
            )
            raise LuterasAPIError(message)

        return result

