from nltk import WordNetLemmatizer, pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation

import re
import nltk

def clean(text: str):
    stop_words = set(stopwords.words("english")) - {"not", "no"}
    lemmatizer = WordNetLemmatizer()

    text = text.lower()
    text = text.replace("n't", " not ")
    text = re.sub(r"(?:\'ll |\'re |\'d |\'ve)", " ", text)
    text = re.sub(r"\d+", "", text)

    # Tokenize and filter stopwords
    tokens = [
        word
        for word in word_tokenize(text)
        if word not in stop_words and word not in punctuation
    ]

    pos_tags = pos_tag(tokens)
    cleaned_text = [
        (
            lemmatizer.lemmatize(word, pos[0].lower())
            if pos[0] in "nv"
            else word
        )
        for word, pos in pos_tags
    ]

    return " ".join(cleaned_text)
