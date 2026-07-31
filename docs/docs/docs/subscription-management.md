# Subscription Management

The LUTERAS Python SDK allows you to create and manage customer subscriptions.

## Create a Subscription

```python
from luteras import Luteras

client = Luteras(
    api_key="YOUR_API_KEY"
)

subscription = client.subscriptions.create(
    customer_email="customer@example.com",
    plan="pro"
)

print(subscription)
```

## Best Practices

- Create subscriptions after successful payment.
- Keep customer email addresses up to date.
- Handle failed payments gracefully.
- Cancel inactive subscriptions when appropriate.