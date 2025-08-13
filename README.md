# Flask Delay Response App

A simple Flask application that allows you to test HTTP responses with configurable delays. Perfect for testing timeout handling, loading states, or simulating slow network conditions.

## Features

- ✅ Configurable delay via query parameters
- ✅ Configurable delay via URL path
- ✅ Instant response when no delay is specified
- ✅ Simple and lightweight
- ✅ Easy to deploy and use

## Installation

1. Make sure you have Python installed on your system
2. Install Flask:
```bash
pip install flask
```

3. Save the code to a file (e.g., `app.py`)

## Usage

### Starting the Server

Run the application:
```bash
python app.py
```

The server will start on `http://localhost:8080`

### API Endpoints

#### 1. Root Endpoint with Query Parameter

**Endpoint:** `GET /`

**Examples:**
- `http://localhost:8080/` - Immediate response (no delay)
- `http://localhost:8080/?delay=5` - 5 seconds delay
- `http://localhost:8080/?delay=10` - 10 seconds delay
- `http://localhost:8080/?delay=0` - No delay (immediate response)

#### 2. Path Parameter Endpoint

**Endpoint:** `GET /<delay_seconds>`

**Examples:**
- `http://localhost:8080/5` - 5 seconds delay
- `http://localhost:8080/10` - 10 seconds delay
- `http://localhost:8080/0` - No delay (immediate response)

### Response Format

The application returns a simple text response:

**With delay:**
```
Done after X seconds
=====================


```

**Without delay:**
```
Done immediately (no delay)
=====================


```

## Use Cases

- **Testing timeout handling** in your applications
- **Simulating slow API responses** for development
- **Load testing** with controlled delays
- **Debugging race conditions** in async code
- **Testing loading states** in frontend applications

## Configuration

### Changing Host and Port

Edit the last line in `app.py`:
```python
app.run(host="0.0.0.0", port=8080)
```

- `host="0.0.0.0"` - Allows access from any IP address
- `port=8080` - Change to your desired port number

### Production Deployment

For production use, consider using a WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8080 app:app
```

## Examples with cURL

```bash
# Immediate response
curl http://localhost:8080/

# 3 second delay using query parameter
curl http://localhost:8080/?delay=3

# 5 second delay using path parameter
curl http://localhost:8080/5

# Test with timing
time curl http://localhost:8080/10
```

## Code Structure

```python
from flask import Flask, request
import time

app = Flask(__name__)

@app.route("/")
def slow():
    # Query parameter approach
    delay = request.args.get('delay', default=0, type=int)
    # ... logic

@app.route("/<int:delay>")
def slow_with_path(delay):
    # URL path approach
    # ... logic
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE).
