FROM python:3.11-slim

# System basics (optional but handy)
RUN apt-get update -qq && apt-get install -y --no-install-recommends \
    curl && rm -rf /var/lib/apt/lists/*

# Python deps (FastAPI, server, and HTTP client)
RUN pip install --no-cache-dir fastapi uvicorn httpx pydantic

WORKDIR /app
COPY . /app
