
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