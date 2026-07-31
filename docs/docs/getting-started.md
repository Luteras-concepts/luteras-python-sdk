# Getting Started

This guide will help you install and configure the LUTERAS Python SDK.

## Requirements

- Python 3.9+
- A LUTERAS account
- An API Key

## Installation

```bash
pip install luteras
```

## Import the SDK

```python
from luteras import Luteras
```

## Configure the Client

```python
client = Luteras(
    api_key="YOUR_API_KEY"
)
```

Replace `YOUR_API_KEY` with the API key generated from your LUTERAS Developer Dashboard.

## Test Your Connection

```python
print(client.api_key)
```

If your API key is configured correctly, you're ready to start using the LUTERAS API.