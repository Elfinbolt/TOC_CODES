def get_productions(non_terminals):
    productions = {}
    for nt in non_terminals:
        rules = input(f"{nt} -> ").split("/")
        productions[nt] = rules
    return productions


def find_nullable_nonterminals(productions):
    nullable = set()
    for nt, rules in productions.items():
        for r in rules:
            if r == "^":
                nullable.add(nt)
    return nullable


def eliminate_null_productions(productions, start_symbol):
    nullable = find_nullable_nonterminals(productions)
    for nt in list(productions.keys()):
        rules = productions[nt]
        new_rules = []
        for r in rules:
            if r == "^":
                continue
            for i in range(len(r)):
                if r[i] in nullable:
                    new_rule = r[:i] + r[i+1:]
                    if new_rule and new_rule not in new_rules:
                        new_rules.append(new_rule)
        rules.extend(new_rules)
        productions[nt] = list(set(rules))
    for nt in list(productions.keys()):
        if nt != start_symbol and "^" in productions[nt]:
            productions[nt].remove("^")


def find_unit_productions(productions):
    unit_productions = {}
    for nt, rules in productions.items():
        for r in rules:
            if r in productions and r != nt:
                unit_productions.setdefault(nt, []).append(r)
    return unit_productions


def remove_unit_productions(productions):
    changed = True
    while changed:
        changed = False
        for nt in list(productions.keys()):
            to_add = []
            to_remove = []
            for r in productions[nt]:
                if r in productions and r != nt:
                    for rr in productions[r]:
                        if rr not in productions[nt]:
                            to_add.append(rr)
                    to_remove.append(r)
            if to_add or to_remove:
                changed = True
                for x in to_remove:
                    if x in productions[nt]:
                        productions[nt].remove(x)
                productions[nt].extend(to_add)
                productions[nt] = list(set(productions[nt]))


def convert_to_cnf(productions, non_terminals, terminals):
    new_productions = {}
    term_map = {}
    next_index = 1

    def get_new_symbol():
        nonlocal next_index
        sym = f"X{next_index}"
        next_index += 1
        return sym

    updated = {}
    for nt in list(productions.keys()):
        updated_rules = []
        for rule in productions[nt]:
            if rule == "^":
                continue
            symbols = list(rule)
            if len(symbols) == 1 and symbols[0] in terminals:
                updated_rules.append(rule)
                continue
            for i, s in enumerate(symbols):
                if s in terminals:
                    if s not in term_map:
                        new_nt = get_new_symbol()
                        term_map[s] = new_nt
                        new_productions[new_nt] = [s]
                    symbols[i] = term_map[s]
            while len(symbols) > 2:
                new_nt = get_new_symbol()
                new_productions[new_nt] = [''.join(symbols[0:2])]
                symbols = [new_nt] + symbols[2:]
            updated_rules.append(''.join(symbols))
        updated[nt] = list(set(updated_rules))
    for k, v in updated.items():
        productions[k] = v
    for k, v in new_productions.items():
        productions[k] = v


def print_productions(productions):
    for nt in sorted(productions.keys(), key=lambda x: (len(x), x)):
        rhs = "/".join(sorted(productions[nt]))
        print(f"{nt} -> {rhs}")


def main():
    non_terminals = input("Enter Non-Terminal Symbols: ").split()
    terminals = input("Enter Terminal Symbols: ").split()
    start_symbol = non_terminals[0]
    productions = get_productions(non_terminals)
    print("\n--- Removing Null Productions ---")
    eliminate_null_productions(productions, start_symbol)
    print_productions(productions)
    print("\n--- Removing Unit Productions ---")
    remove_unit_productions(productions)
    print_productions(productions)
    print("\n--- Converting to Strict CNF ---")
    convert_to_cnf(productions, non_terminals, terminals)
    print_productions(productions)


if __name__ == "__main__":
    main()
