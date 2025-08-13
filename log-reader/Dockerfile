FROM python:3.9-slim

RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

RUN chown -R appuser:appuser /app

USER appuser

CMD ["python", "log_reader.py"]
