# Sentiment Analysis API

A web API for the sentiment analysis model built using Flask.

## Installation

If you're on Linux, it's recommended to create a virtual environment first.

```bash
python3 -m venv env
source env/bin/activate
```

Then install the required packages to run locally.

```bash
pip install -r requirements.txt
```

## Testing

Spin up the server using these commands.

```bash
gunicorn app:app
```

Starts up the server on localhost port 5000.
