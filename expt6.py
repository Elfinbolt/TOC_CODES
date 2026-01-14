def find_nullable(productions): 
    nullable = set() 
    changed = True 
    while changed: 
        changed = False 
        for nt, prods in productions.items(): 
            for prod in prods: 
                if prod == "^" or all(c in nullable for c in prod): 
                    if nt not in nullable: 
                        nullable.add(nt) 
                        changed = True 
    return nullable 


def remove_nullable(productions, nullable): 
    new_prods = {} 
    for nt, prods in productions.items(): 
        new_set = set() 
        for prod in prods: 
            if prod == "^": 
                continue 
            n = len(prod) 
            for mask in range(1 << n): 
                s = "".join(prod[i] for i in range(n) if not (mask & (1 << i) and prod[i] in nullable)) 
                if s: 
                    new_set.add(s) 
        new_prods[nt] = list(new_set) 
    return new_prods 


def remove_unit(productions, terminals): 
    units = {nt: set([nt]) for nt in productions} 
    changed = True 
    while changed: 
        changed = False 
        for A in productions: 
            for prod in productions[A]: 
                if len(prod) == 1 and prod not in terminals: 
                    B = prod 
                    if B not in units[A]: 
                        units[A].add(B) 
                        changed = True

    new_prods = {nt: [] for nt in productions} 
    for A in productions: 
        for B in units[A]: 
            for prod in productions[B]: 
                if not (len(prod) == 1 and prod not in terminals): 
                    if prod not in new_prods[A]: 
                        new_prods[A].append(prod) 
    return new_prods 


NT = input("Enter Non-Terminals: ").split() 
T = input("Enter Terminals: ").split() 
productions = {} 
for nt in NT: 
    rhs = input(f"{nt}-> ").split("/") 
    productions[nt] = rhs 

nullable = find_nullable(productions) 
productions = remove_nullable(productions, nullable) 
productions = remove_unit(productions, set(T)) 

print("\nSimplified Grammar:") 
for nt, prods in productions.items(): 
    print(f"{nt}-> {'/'.join(prods)}") 
