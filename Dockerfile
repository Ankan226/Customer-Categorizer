# STAGE 1: Builder
FROM python:3.10-slim-bullseye AS builder
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends build-essential
COPY requirements.txt .
# Pre-install core conflict fixers
RUN pip install --no-cache-dir PyYAML==6.0.1 starlette==0.19.1 "pydantic<2.0.0" "urllib3<2.0.0" "numpy<2.0.0"
RUN pip install --no-cache-dir -r requirements.txt || pip install --no-cache-dir -r requirements.txt --use-deprecated=legacy-resolver

# STAGE 2: Production
FROM python:3.10-slim-bullseye
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . .
RUN touch .project-root
EXPOSE 5000
CMD ["python", "app.py"]