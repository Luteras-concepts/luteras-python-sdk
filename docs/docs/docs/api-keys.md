# API Keys

API Keys allow your application to securely communicate with the LUTERAS API.

## Creating an API Key

1. Log in to your LUTERAS Developer Dashboard.
2. Navigate to **API Keys**.
3. Click **Create API Key**.
4. Copy and securely store the generated key.

## Example

```python
from luteras import Luteras

client = Luteras(
    api_key="YOUR_API_KEY"
)

print(client.api_key)
```

## Best Practices

- Never share your API key.
- Store API keys in environment variables.
- Rotate API keys regularly.
- Delete unused API keys immediately.