class LuterasError(Exception):
    """Base exception for all LUTERAS SDK errors."""
    pass


class LuterasAPIError(LuterasError):
    """Raised when the LUTERAS API returns an error response."""
    pass


class LuterasNetworkError(LuterasError):
    """Raised when the SDK cannot connect to the LUTERAS API."""
    pass
