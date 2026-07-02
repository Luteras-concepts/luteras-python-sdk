import pytest
from luteras import LuterasClient


def test_client_requires_api_key():
    with pytest.raises(ValueError, match="api_key is required"):
        LuterasClient(api_key="")


def test_client_initializes_licenses_api():
    client = LuterasClient(api_key="test-api-key")

    assert client.licenses is not None
