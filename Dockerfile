FROM python:3.8-slim
WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm

COPY *.py /app/

ENTRYPOINT ["gunicorn", "-b", ":5000", "01_sentiment_analysis:app"]