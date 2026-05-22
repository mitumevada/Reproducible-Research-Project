FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install pandas matplotlib

CMD ["python", "src/pipeline.py"]