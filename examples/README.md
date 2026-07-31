# LUTERAS SDK Examples

This directory contains practical examples of using the LUTERAS Python SDK.

Each example demonstrates a common integration scenario with the LUTERAS API.

## Installation

```bash
pip install luteras
```

## License Verification Example

```python
from luteras import Luteras

client = Luteras(api_key="YOUR_API_KEY")

response = client.licenses.verify(
    license_key="LICENSE_KEY"
)

print(response)
```

## API Key Authentication Example

```python
from luteras import Luteras

client = Luteras(api_key="YOUR_API_KEY")

print(client.api_key)
```

## Create License Example

```python
from luteras import Luteras

client = Luteras(api_key="YOUR_API_KEY")

license = client.licenses.create(
    product_id="PRODUCT_ID",
    customer_email="customer@example.com"
)

print(license)
```

## Subscription Example

```python
from luteras import Luteras

client = Luteras(api_key="YOUR_API_KEY")

subscription = client.subscriptions.create(
    customer_email="customer@example.com",
    plan="pro"
)

print(subscription)
```

## Error Handling Example

```python
from luteras import Luteras
from luteras.exceptions import LuterasError

client = Luteras(api_key="YOUR_API_KEY")

try:
    response = client.licenses.verify(
        license_key="LICENSE_KEY"
    )
    print(response)
except LuterasError as e:
    print(f"Error: {e}")
```