# Error Handling

The LUTERAS Python SDK raises clear exceptions when an API request fails. Always handle errors gracefully in your application.

## Example

```python
from luteras import Luteras

client = Luteras(
    api_key="YOUR_API_KEY"
)

try:
    usage = client.usage.retrieve()
    print(usage)

except Exception as e:
    print(f"Error: {e}")
```

## Common Errors

| Error | Meaning |
|--------|---------|
| 401 Unauthorized | Invalid API Key |
| 403 Forbidden | Access denied |
| 404 Not Found | Resource does not exist |
| 429 Too Many Requests | Rate limit exceeded |
| 500 Internal Server Error | LUTERAS server error |

## Best Practices

- Always wrap API calls in a `try`/`except` block.
- Log errors for debugging.
- Retry temporary failures when appropriate.
- Never expose internal error messages to end users.
- Contact LUTERAS support if errors persist.