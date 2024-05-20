import random
from nltk import CFG
from nltk.parse.generate import generate

def load_grammar(filename):
    with open(filename, 'r') as f:
        grammar_content = f.read().strip()  # Verwijder overtollige witruimte
        if not grammar_content:
            raise ValueError("De grammatica is leeg!")
    print("Loaded Grammar:\n", grammar_content)  # Print de grammatica voor debugging
    return CFG.fromstring(grammar_content)

def generate_random_sentences(grammar, n=12):
    sentences = list(generate(grammar, depth=10))
    random.shuffle(sentences)  # Shuffle sentences to introduce randomness
    return sentences[:n]  # Return only n sentences

if __name__ == "__main__":
    try:
        grammar = load_grammar('final_cleaned_cfg_rules.txt')
        
        # Genereer willekeurige zinnen
        random_sentences = generate_random_sentences(grammar, n=12)
        for sentence in random_sentences:
            print(' '.join(sentence))
    except ValueError as e:
        print(f"Error: {e}")








