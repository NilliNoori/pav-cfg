def check_cleaned_rules(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    problem_patterns = [
        "''",
        "``",
        ". -> '.'",
        "INTJ -> UH .",
        "PP -> IN NP",
        "VP -> VB ADVP PRN `` NP",
        "VP -> VBG NP `` NP",
        "VP -> VB ADVP PRN `` NP",
        "VP -> VBG NP `` NP",
    ]

    recursive_patterns = [
        "S -> S",
        "NP -> NP",
        "VP -> VP",
        "ADJP -> ADJP",
        "ADVP -> ADVP",
        "PP -> PP",
        "SBAR -> SBAR",
        "SQ -> SQ",
        "SINV -> SINV",
        "FRAG -> FRAG",
        "X -> X",
    ]

    problematic_rules = [line.strip() for line in lines if any(pattern in line for pattern in problem_patterns + recursive_patterns)]
    
    if problematic_rules:
        print("Problematic rules found:")
        for rule in problematic_rules:
            print(rule.strip())
    else:
        print("No problematic rules found.")

if __name__ == "__main__":
    check_cleaned_rules('final_cleaned_cfg_rules.txt')


