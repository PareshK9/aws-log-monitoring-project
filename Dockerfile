FROM python:3.13-slim

WORKDIR /app

COPY app/log_processor.py .
COPY logs/sample.log ./logs/sample.log

RUN mkdir -p output

CMD ["python", "log_processor.py"]
