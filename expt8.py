# Python Program to Convert a Context-Free Grammar (CFG) to Pushdown Automata (PDA)
# Includes terminal-matching transitions like δ(q, a, a) → (q, ε)

class CFGtoPDA:
    def __init__(self, variables, terminals, start_symbol, productions):
        self.variables = variables
        self.terminals = terminals
        self.start_symbol = start_symbol
        self.productions = productions
        self.transitions = []

    def display_cfg(self):
        print("===== Context-Free Grammar (CFG) =====")
        print("Variables (V):", self.variables)
        print("Terminals (Σ):", self.terminals)
        print("Start Symbol (S):", self.start_symbol)
        print("\nProductions (R):")
        for var, rules in self.productions.items():
            print(f"  {var} → {' | '.join(rules)}")
        print("======================================\n")

    def convert_to_pda(self):
        state = "q"
        print("Converting CFG to PDA...\n")

        # 1. Transitions for CFG productions
        for variable in self.productions:
            for production in self.productions[variable]:
                if all(symbol in self.terminals for symbol in production):
                    # A → a
                    transition = (state, production, variable, state, "ε")
                    self.transitions.append(transition)
                else:
                    # A → combination of variables/terminals (e.g., aSb)
                    transition = (state, "ε", variable, state, production)
                    self.transitions.append(transition)

        # 2. Transitions for terminal matching (to pop terminals)
        for t in self.terminals:
            transition = (state, t, t, state, "ε")
            self.transitions.append(transition)

        print("✅ PDA Transitions Generated Successfully!\n")

    def display_pda(self):
        print("===== Pushdown Automata (PDA) =====")
        print("Q = { q }")
        print(f"Σ (Input symbols) = {self.terminals}")
        print(f"Γ (Stack symbols) = {self.variables + self.terminals}")
        print(f"Start state = q")
        print(f"Start stack symbol = {self.start_symbol}")
        print("F (Final states) = { q }\n")

        print("Transitions:")
        for t in self.transitions:
            print(f"  δ({t[0]}, {t[1]}, {t[2]}) → ({t[3]}, {t[4]})")
        print("=====================================\n")


# Example CFG for L = { a^n b^n | n ≥ 1 }
variables = ["S"]
terminals = ["a", "b"]
start_symbol = "S"
productions = {
    "S": ["aSb", "ab"]
}

# Run the converter
converter = CFGtoPDA(variables, terminals, start_symbol, productions)
converter.display_cfg()
converter.convert_to_pda()
converter.display_pda()
