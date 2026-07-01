import requests

from .exceptions import LuterasAPIError, LuterasNetworkError


class RequestHandler:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def headers(self):
        return {
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }

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
