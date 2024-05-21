from nltk.parse.corenlp import CoreNLPParser
from nltk.tokenize import sent_tokenize

# Step 1: Read the Text File
file_path = 'Documents/KI/PAV/Cinderella.txt'  # Replace with the path to your .txt file
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Step 2: Import Required Libraries (already done above)
# from nltk.parse.corenlp import CoreNLPParser
# from nltk.tokenize import sent_tokenize

# Step 3: Initialize CoreNLPParser
parser = CoreNLPParser(url='http://localhost:9000')

# Step 4: Tokenize Text into Sentences
sentences = sent_tokenize(text)

# Step 5: Parse Each Sentence
parsed_trees = []
for sentence in sentences:
    parsed_tree = next(parser.raw_parse(sentence))
    parsed_trees.append(parsed_tree)

# Step 6: Print or Process Parsed Trees
for tree in parsed_trees:
    print(tree)