from nltk.parse.corenlp import CoreNLPParser
import json

# Verbinden met de CoreNLP-server
parser = CoreNLPParser(url='http://localhost:9000')

# Laad de geparste corpus
with open("preprocessed_corpus.json", "r") as infile:
    preprocessed_corpus = json.load(infile)

# Selecteer enkele voorbeeldzinnen om te parsen
example_sentences = [
    "Ella's father met another woman",
    "The stepmother treated her terribly",
    "Cinderella went to the ball"
]

# Parse de zinnen en druk de parse-bomen af
for sentence in example_sentences:
    parse_tree = next(parser.raw_parse(sentence))
    print(parse_tree)
