from .utils import RequestHandler


class LuterasAccountClient:
    """
    Account-level client for JWT-protected LUTERAS endpoints.

    Use this client for dashboard, billing, onboarding, and admin endpoints.

    Example:
        from luteras.account_client import LuterasAccountClient

        account = LuterasAccountClient(token="YOUR_JWT_TOKEN")
    """

    def __init__(
        self,
        token: str,
        base_url: str = "https://luteras.com/api"
    ):
        if not token:
            raise ValueError("token is required")

        self.token = token
        self.base_url = base_url.rstrip("/")

        self._request_handler = RequestHandler(
            api_key=None,
            base_url=self.base_url,
            token=self.token
        )
