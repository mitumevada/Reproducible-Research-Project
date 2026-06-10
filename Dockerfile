FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install pandas matplotlib numpy statsmodels notebook nbconvert

CMD ["sh","-c",
"mkdir -p /app/output && \
python src/pipeline.py && \
jupyter nbconvert --execute --to html 'Macroeconomic TSA.ipynb' \
--output-dir=/app/output"
]

