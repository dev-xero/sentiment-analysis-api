FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Download NLTK data
RUN python -m nltk.downloader averaged_perceptron_tagger wordnet omw stopwords punkt

EXPOSE 5000

CMD ["python", "app.py"]