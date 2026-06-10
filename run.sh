#!/bin/sh

mkdir -p /app/output

python src/pipeline.py

jupyter nbconvert \
    --execute \
    --to html \
    "Macroeconomic TSA.ipynb" \
    --output-dir=/app/output