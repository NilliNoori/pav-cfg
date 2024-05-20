import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import string
from collections import Counter
import json

# Download necessary NLTK data
nltk.download('punkt')

# Load the provided text corpus
file_path = "Cinderella.txt"  # Pas dit pad aan naar jouw bestand
with open(file_path, "r", encoding="utf-8-sig") as file:
    corpus = file.read()

# Preprocessing steps
def preprocess_text(text):
    # Tokenize sentences
    sentences = sent_tokenize(text)
    # Tokenize words within sentences
    words = [word_tokenize(sentence) for sentence in sentences]
    # Lowercase and remove punctuation
    words = [[word.lower() for word in sentence if word not in string.punctuation] for sentence in words]
    return words

# Apply preprocessing
preprocessed_corpus = preprocess_text(corpus)

# Save preprocessed data to a JSON file
with open("preprocessed_corpus.json", "w") as outfile:
    json.dump(preprocessed_corpus, outfile)

# Flatten list of words
all_words = [word for sentence in preprocessed_corpus for word in sentence]

# Vocabulary size
vocab_size = len(set(all_words))

# Sentence lengths
sentence_lengths = [len(sentence) for sentence in preprocessed_corpus]

# Most common words
most_common_words = Counter(all_words).most_common(10)

# Output results
print(f"Vocabulary Size: {vocab_size}")
print(f"Average Sentence Length: {sum(sentence_lengths) / len(sentence_lengths)}")
print(f"Most Common Words: {most_common_words}")
print(f"First 5 Preprocessed Sentences: {preprocessed_corpus[:5]}")

