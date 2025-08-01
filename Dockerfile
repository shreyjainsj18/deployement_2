# ---------- build ----------
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip wheel --no-cache-dir --no-deps -r requirements.txt -w /wheels

# ---------- run ----------
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/*
COPY . .
ENV PYTHONUNBUFFERED=1
# Ensure .env is inside container
COPY .env . 
ENV PORT=5000
EXPOSE 5000
CMD gunicorn --bind 0.0.0.0:${PORT} app.app:app



# CMD ["gunicorn", "--bind", "0.0.0.0:${PORT}", "app.app:app"]
