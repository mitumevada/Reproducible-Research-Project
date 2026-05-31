FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install pandas matplotlib numpy statsmodels

CMD ["python", "src/VAR_model.py"]