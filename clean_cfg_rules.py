def clean_cfg_rules(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    valid_rules = []
    for line in lines:
        line = line.strip()
        if "->" in line:
            lhs, rhs = line.split("->")
            lhs = lhs.strip()
            rhs = rhs.strip()
            # Verwijder regels met lege non-terminalen of terminals en regels met ongewenste symbolen
            if lhs and rhs and "''" not in lhs and "''" not in rhs and lhs not in ['.', '``'] and rhs not in ['.', '``'] and not rhs.startswith("``") and not rhs.startswith("''") and not rhs.endswith("''") and not rhs.endswith("``"):
                valid_rules.append(line)
    
    with open(output_file, 'w') as f:
        for rule in valid_rules:
            f.write(rule + '\n')

if __name__ == "__main__":
    clean_cfg_rules('cfg_rules.txt', 'cleaned_cfg_rules.txt')
    print("Schoongemaakte CFG regels zijn opgeslagen in cleaned_cfg_rules.txt")




