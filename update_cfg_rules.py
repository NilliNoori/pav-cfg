new_rules = """
S -> NP VP
NP -> DT NN | DT JJ NN | NN | JJ NN | NNP | NNS | PRP
VP -> VB | VB NP | VB PP | VB S
DT -> 'the' | 'a' | 'an' | 'some'
NN -> 'cat' | 'dog' | 'man' | 'woman' | 'house' | 'car' | 'stepmother' | 'stepsisters' | 'prince' | 'ball' | 'dress' | 'slipper' | 'fairy'
JJ -> 'big' | 'small' | 'happy' | 'sad' | 'beautiful' | 'kind' | 'mean'
VB -> 'sees' | 'likes' | 'hates' | 'runs' | 'jumps' | 'finds' | 'helps' | 'meets' | 'loses' | 'dances' | 'wears'
IN -> 'in' | 'on' | 'under' | 'over' | 'with' | 'at' | 'to'
NNP -> 'Cinderella' | 'Ella' | 'Prince Charming'
NNS -> 'cats' | 'dogs' | 'men' | 'women' | 'stepsisters'
PRP -> 'she' | 'he'
"""

with open('final_cleaned_cfg_rules.txt', 'w') as f:
    f.write(new_rules.strip())

print("Final cleaned CFG rules have been updated.")
