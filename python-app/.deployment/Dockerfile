# Stage 1: Build stage
FROM python:3.10-slim as builder

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Stage 2: Runtime stage
FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY --from=builder /app /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

