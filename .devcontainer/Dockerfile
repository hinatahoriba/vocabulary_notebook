FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /api

COPY . /api

RUN pip install --no-cache-dir -r requirements.txt