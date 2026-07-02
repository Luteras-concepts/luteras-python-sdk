import pytest
from luteras.licenses import LicensesAPI


class FakeRequestHandler:
    def __init__(self):
        self.calls = []

    def request(self, method, path, data=None):
        self.calls.append({
            "method": method,
            "path": path,
            "data": data
        })

        return {"ok": True}


def test_create_license_calls_correct_endpoint():
    handler = FakeRequestHandler()
    licenses = LicensesAPI(handler)

    result = licenses.create()

    assert result == {"ok": True}
    assert handler.calls[0]["method"] == "POST"
    assert handler.calls[0]["path"] == "/licenses/create"


def test_verify_license_requires_license_key():
    handler = FakeRequestHandler()
    licenses = LicensesAPI(handler)

    with pytest.raises(ValueError, match="license_key is required"):
        licenses.verify("")


def test_verify_license_calls_correct_endpoint():
    handler = FakeRequestHandler()
    licenses = LicensesAPI(handler)

    result = licenses.verify("TEST-LICENSE-KEY")

    assert result == {"ok": True}
    assert handler.calls[0]["method"] == "POST"
    assert handler.calls[0]["path"] == "/licenses/verify"
    assert handler.calls[0]["data"] == {
        "license_key": "TEST-LICENSE-KEY"
    }
