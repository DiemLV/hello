FROM python:3.11-slim
WORKDIR /app
COPY slow-responder.py .
CMD ["python", "app.py"]
