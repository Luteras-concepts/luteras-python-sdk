# License Management

The LUTERAS Python SDK allows you to create and verify software licenses.

## Create a License

```python
from luteras import Luteras

client = Luteras(
    api_key="YOUR_API_KEY"
)

license = client.licenses.create(
    product_id="PRODUCT_ID",
    customer_email="customer@example.com"
)

print(license)
```

## Verify a License

```python
response = client.licenses.verify(
    license_key="LICENSE_KEY"
)

print(response)
```

## Best Practices

- Create one license per customer purchase.
- Store license keys securely.
- Verify licenses before granting access.
- Revoke compromised licenses immediately.