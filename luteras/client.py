from .utils import RequestHandler
from .licenses import LicensesAPI


class LuterasClient:
    """
    Official Python SDK for the LUTERAS API.
    """

    def __init__(self, api_key, base_url="https://luteras.com/api/v1"):
        if not api_key:
            raise ValueError("api_key is required")

        self._request_handler = RequestHandler(
            api_key=api_key,
            base_url=base_url
        )

        self.licenses = LicensesAPI(
            self._request_handler
        )
