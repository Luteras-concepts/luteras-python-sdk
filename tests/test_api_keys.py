from luteras.api_keys import APIKeysAPI


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


def test_list_api_keys_calls_correct_endpoint():
    handler = FakeRequestHandler()
    api_keys = APIKeysAPI(handler)

    result = api_keys.list()

    assert result == {"ok": True}
    assert handler.calls[0]["method"] == "GET"


def test_create_api_key_calls_correct_endpoint():
    handler = FakeRequestHandler()
    api_keys = APIKeysAPI(handler)

    result = api_keys.create()

    assert result == {"ok": True}
    assert handler.calls[0]["method"] == "POST"
