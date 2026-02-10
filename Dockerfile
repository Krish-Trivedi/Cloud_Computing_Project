FROM python:3.9-slim

WORKDIR /app

COPY data_analysis.py .

CMD ["python", "data_analysis.py"]
