class LicensesAPI:
    """
    License management for the LUTERAS API.
    """

    def __init__(self, request_handler):
        self._request = request_handler.request

    def verify(self, license_key):
        """
        Verify a software license.
        """
        if not license_key:
            raise ValueError("license_key is required")

        return self._request(
            "POST",
            "/licenses/verify",
            {
                "license_key": license_key
            }
        )

    def create(self):
        """
        Create a new software license.
        """
        return self._request(
            "POST",
            "/licenses/create"
        )
