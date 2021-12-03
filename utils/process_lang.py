import re
from pymystem3 import Mystem
mystem = Mystem()
from string import punctuation
from nltk.corpus import stopwords
russian_stopwords = stopwords.words("russian")

def preprocess_text(text):
    r = re.compile("[а-яА-Я]+")
    text = text.replace("#", "").replace("  ", " ").replace("\n"," ")
    tokens = text.lower().split(" ")
    tokens = [w.lower() for w in filter(r.match, tokens)]
    tokens = mystem.lemmatize(" ".join(tokens))
    tokens = [
        token
        for token in tokens
        if token not in russian_stopwords
           and token != " "
           and token.strip() not in punctuation
    ]
    return " ".join(tokens)