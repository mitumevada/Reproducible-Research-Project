FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install pandas matplotlib numpy statsmodels notebook nbconvert

RUN chmod +x run.sh

CMD ["./run.sh"]

