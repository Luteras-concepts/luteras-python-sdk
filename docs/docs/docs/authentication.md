# Authentication

The LUTERAS Python SDK uses API Keys to authenticate every request.

## Generate an API Key

1. Sign in to your LUTERAS Developer Dashboard.
2. Open **API Keys**.
3. Click **Create API Key**.
4. Copy the generated key.

## Configure Authentication

```python
from luteras import Luteras

client = Luteras(
    api_key="YOUR_API_KEY"
)
```

## Keep Your API Key Secure

- Never expose your API key in frontend applications.
- Never commit API keys to GitHub.
- Store API keys in environment variables.
- Rotate compromised keys immediately.

## Example Using Environment Variables

```python
import os
from luteras import Luteras

client = Luteras(
    api_key=os.getenv("LUTERAS_API_KEY")
)
```