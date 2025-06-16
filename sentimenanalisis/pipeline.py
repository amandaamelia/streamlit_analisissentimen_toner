import re
import string
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# --- Case folding
def case_folding(text):
    if isinstance(text, str):
        return text.lower()
    return text

# --- Clean text
def clean_text(text):
    if not isinstance(text, str):
        return text
    text = re.sub(r'http\S+', '', text)                 # remove URLs
    text = re.sub(r'@\S+', '', text)                    # remove mentions
    text = re.sub(r'#\S+', '', text)                    # remove hashtags
    text = re.sub(r'[^\x00-\x7F]+', '', text)           # remove emojis
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)          # remove special chars
    text = re.sub(r'\s+', ' ', text).strip()            # remove extra whitespace
    text = re.sub(r'[0-9]+', '', text)                  # remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
    return text

# --- Tokenize
def tokenize(text):
    return text.split()

# --- Load kamus normalisasi
import pandas as pd
normalized_word = pd.read_csv("sentimenanalisis/kamuskatabaku.csv", header=None, names=["original", "normalized"])
normalized_word = normalized_word.dropna()  # Remove rows with NaN values
normalized_word_dict = dict(zip(normalized_word.iloc[:, 0], normalized_word.iloc[:, 1]))

# --- Normalize
def normalized_term(tokens):
    return [normalized_word_dict.get(term, term) for term in tokens]

# --- Load stopwords
txt_stopword = pd.read_csv("sentimenanalisis/stopwordbahasa.txt", names=["stopwords"], header=None)
list_stopwords = set(txt_stopword["stopwords"])

# --- Remove stopwords
def stopwords_removal(words):
    return [word for word in words if word not in list_stopwords]

# --- Stemming
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def stemmed_wrapper(term):
    return stemmer.stem(term)

# --- Apply stemming with caching (optional)
term_dict = {}

def get_stemmed_term(document):
    result = []
    for term in document:
        if term not in term_dict:
            term_dict[term] = stemmed_wrapper(term)
        result.append(term_dict[term])
    return result

# --- Full pipeline (opsional)
def full_preprocessing(text):
    text = case_folding(text)
    text = clean_text(text)
    tokens = tokenize(text)
    tokens = normalized_term(tokens)
    tokens = stopwords_removal(tokens)
    tokens = get_stemmed_term(tokens)
    return ' '.join(tokens)
