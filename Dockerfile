FROM python:3.11-slim
WORKDIR /app
RUN pip install psycopg2-binary
COPY test_postgres.py .
CMD ["python", "test_postgres.py"]
