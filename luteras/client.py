from .utils import RequestHandler
from .licenses import LicensesAPI


class LuterasClient:
    """
    Official Python SDK client for the LUTERAS API Platform.

    Example:
        from luteras import LuterasClient

        client = LuterasClient(api_key="YOUR_API_KEY")
        license = client.licenses.create()
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://luteras.com/api/v1"
    ):
        if not api_key:
            raise ValueError("api_key is required")

        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

        self._request_handler = RequestHandler(
            api_key=self.api_key,
            base_url=self.base_url
        )

        self.licenses = LicensesAPI(
            self._request_handler
        )
