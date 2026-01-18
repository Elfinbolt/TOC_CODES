# Python Program to Convert a Context-Free Grammar (CFG) to Pushdown Automata (PDA)
# Includes terminal-matching transitions like δ(q, a, a) → (q, ε)

# ---------- CFG Definition ----------
variables = ["S","A","B"]
terminals = ["a", "b"]
start_symbol = "S"
productions = {
    "S": ["AB", "BA"],
    "A":["a"],
    "B":["b"]
}

transitions = []

# ---------- Display CFG ----------
def display_cfg():
    print("===== Context-Free Grammar (CFG) =====")
    print("Variables (V):", variables)
    print("Terminals (Σ):", terminals)
    print("Start Symbol (S):", start_symbol)
    print("\nProductions (R):")
    for var, rules in productions.items():
        print(f"  {var} → {' | '.join(rules)}")
    print("======================================\n")


# ---------- Convert CFG to PDA ----------
def convert_to_pda():
    state = "q"
    print("Converting CFG to PDA...\n")

    # 1. Transitions for CFG productions
    for variable in productions:
        for production in productions[variable]:
            if all(symbol in terminals for symbol in production):
                # A → a
                transition = (state, production, variable, state, "ε")
                transitions.append(transition)
            else:
                # A → combination of variables/terminals (e.g., aSb)
                transition = (state, "ε", variable, state, production)
                transitions.append(transition)

    # 2. Transitions for terminal matching
    for t in terminals:
        transition = (state, t, t, state, "ε")
        transitions.append(transition)

    print("✅ PDA Transitions Generated Successfully!\n")


# ---------- Display PDA ----------
def display_pda():
    print("===== Pushdown Automata (PDA) =====")
    print("Q = { q }")
    print(f"Σ (Input symbols) = {terminals}")
    print(f"Γ (Stack symbols) = {variables + terminals}")
    print("Start state = q")
    print(f"Start stack symbol = {start_symbol}")
    print("F (Final states) = { q }\n")

    print("Transitions:")
    for t in transitions:
        print(f"  δ({t[0]}, {t[1]}, {t[2]}) → ({t[3]}, {t[4]})")
    print("=====================================\n")


# ---------- Run Program ----------
display_cfg()
convert_to_pda()
display_pda()