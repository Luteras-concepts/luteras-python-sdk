# Usage Tracking

The LUTERAS Python SDK allows you to monitor API usage for your applications.

## Retrieve Usage

```python
from luteras import Luteras

client = Luteras(
    api_key="YOUR_API_KEY"
)

usage = client.usage.retrieve()

print(usage)
```

## Example Response

```json
{
  "requests": 1250,
  "successful_requests": 1238,
  "failed_requests": 12
}
```

## Best Practices

- Monitor usage regularly.
- Set alerts for unusual traffic.
- Review failed requests.
- Upgrade your plan when approaching usage limits.