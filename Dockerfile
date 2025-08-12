FROM python:3.11-slim
WORKDIR /app

# Cài dependency Python
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
COPY slow-responder.py .
CMD ["python", "slow-responder.py"]
