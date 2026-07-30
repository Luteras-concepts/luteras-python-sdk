
# LUTERAS Python SDK

Official Python SDK for the LUTERAS API Platform.

Build software licensing, API key management, subscriptions, JWT authentication and usage tracking into your Python applications in minutes.

## Features

- ✅ Software Licensing
- ✅ API Key Management
- ✅ JWT Authentication
- ✅ Subscription Billing
- ✅ Usage Tracking
- ✅ Developer-friendly API
- ✅ Python 3.9+

## Installation

```bash
pip install luteras
```

Upgrade to the latest version:

```bash
pip install --upgrade luteras


## Quick Start

```python
from luteras import LuterasClient

client = LuterasClient(
    api_key="YOUR_LUTERAS_API_KEY"
)

license = client.licenses.create()

result = client.licenses.verify(
    license["license_key"]
)

print(result)
```
```

## Create a License

```python
from luteras import LuterasClient

client = LuterasClient(
    api_key="YOUR_LUTERAS_API_KEY"
)

license = client.licenses.create()

print(license["license_key"])
```

## Verify a License

```python
from luteras import LuterasClient

client = LuterasClient(
    api_key="YOUR_LUTERAS_API_KEY"
)

result = client.licenses.verify(
    "YOUR_LICENSE_KEY"
)

print(result)
```

## sample response

```json
{
  "valid": true,
  "status": "active",
  "api_limit": 5000,
  "api_usage": 12,
  "expires_at": null,
  "overage_calls": 0,
  "overage_cost": 0.0
}
```


## Error Handling


```python
from luteras import LuterasClient
from luteras.exceptions import (
    LuterasAPIError,
    LuterasNetworkError,
)

client = LuterasClient(
    api_key="YOUR_LUTERAS_API_KEY"
)

try:
    result = client.licenses.verify(
        "YOUR_LICENSE_KEY"
    )
    print(result)

except LuterasAPIError as error:
    print("API Error:", error)

except LuterasNetworkError as error:
    print("Network Error:", error)
```

## Developer Resources

-    Website: https://luteras.com
-    API Documentation: https://luteras.com/docs
-    Swagger UI: https://luteras.com/swagger
-    PyPI: https://pypi.org/project/luteras/
-    GitHub: https://github.com/luteras-concepts/luteras-python-sdk

## Support

If you need help integrating LUTERAS into your application:

-  Email: support@luteras.com
-  Website: https://luteras.com
-  Documentation: https://luteras.com/docs


## License

This project is licensed under the MIT License.

See the LICENSE file for details.

