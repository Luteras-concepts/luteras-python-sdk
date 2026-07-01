class APIKeysAPI:
    """
    API Key management for the LUTERAS API.
    """

    def __init__(self, request_handler):
        self._request = request_handler.request

    def list(self):
        return self._request(
            "GET",
            "/../api-keys"
        )

    def create(self):
        return self._request(
            "POST",
            "/../create-api-key"
        )

    def get(self, key_id):
        if not key_id:
            raise ValueError("key_id is required")

        return self._request(
            "GET",
            f"/../api-keys/{key_id}"
        )

    def delete(self, key_id):
        if not key_id:
            raise ValueError("key_id is required")

        return self._request(
            "DELETE",
            f"/../api-keys/{key_id}"
        )
