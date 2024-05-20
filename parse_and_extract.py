from nltk.parse.corenlp import CoreNLPParser
import json

def connect_parser(url='http://localhost:9000'):
    return CoreNLPParser(url=url)

def parse_sentence(parser, sentence):
    parse_tree = next(parser.raw_parse(' '.join(sentence)))
    return parse_tree

def extract_cfg_rules(tree):
    rules = []
    for production in tree.productions():
        rule = str(production)
        if "->" in rule:  # Controleer of de regel geldig is
            rules.append(rule)
    return rules

if __name__ == "__main__":
    # Laad het corpus
    with open('preprocessed_corpus.json', 'r') as f:
        corpus = json.load(f)
    
    # Verbind met de CoreNLP server
    parser = connect_parser()
    
    all_rules = set()
    for sentence in corpus:
        tree = parse_sentence(parser, sentence)
        rules = extract_cfg_rules(tree)
        all_rules.update(rules)
    
    # Combineer en sla de regels op
    grammar_rules = '\n'.join(sorted(all_rules))
    with open('cfg_rules.txt', 'w') as f:
        f.write(grammar_rules)
    
    print("CFG is opgeslagen in cfg_rules.txt")


