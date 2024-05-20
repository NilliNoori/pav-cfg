def remove_problematic_rules(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    problem_patterns = [
        "''",
        "``",
        ". -> '.'",
        "INTJ -> UH .",
        "PP -> IN NP .",
        "PP -> IN NP",
        "ADVP -> ADVP SBAR",
        "VP -> VB ADVP PRN `` NP",
        "VP -> VBG NP `` NP",
        "VP -> VB ADVP PRN `` NP",
        "VP -> VBG NP `` NP",
        "$",
    ]

    recursive_patterns = [
        "ADJP -> ADJP",
        "NP -> NP",
        "VP -> VP",
        "S -> S",
        "SBAR -> SBAR",
        "FRAG -> FRAG",
        "X -> X",
    ]

    valid_rules = []
    for line in lines:
        line = line.strip()
        if "->" in line:
            lhs, rhs = line.split("->")
            lhs = lhs.strip()
            rhs = rhs.strip()
            rule = f"{lhs} -> {rhs}"
            if lhs and rhs and not any(pattern in rule for pattern in problem_patterns) and not any(pattern in rule for pattern in recursive_patterns):
                valid_rules.append(line)
    
    with open(output_file, 'w') as f:
        for rule in valid_rules:
            f.write(rule + '\n')

if __name__ == "__main__":
    remove_problematic_rules('cleaned_cfg_rules.txt', 'final_cleaned_cfg_rules.txt')
    print("Problematische regels zijn verwijderd en opgeslagen in final_cleaned_cfg_rules.txt")
