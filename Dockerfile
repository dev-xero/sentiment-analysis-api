FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Download NLTK data
RUN python -m nltk.downloader averaged_perceptron_tagger wordnet omw stopwords punkt

EXPOSE 5000

CMD ["gunicorn", "app:app"]