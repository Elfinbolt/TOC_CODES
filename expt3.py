def show_table(trans_map, state_list, symbols, caption):
    print("\n" + caption)
    print("State\t" + "\t".join(symbols))
    for st in state_list:
        row = [st]
        for sym in symbols:
            row.append(",".join(trans_map.get((st, sym), [])))
        print("\t".join(row))


def convert_nfa_to_dfa(nfa_map, start_node, final_nodes, symbols):
    dfa_states = [[start_node]]
    dfa_transitions = {}
    dfa_final_nodes = []

    for current in dfa_states:
        for sym in symbols:
            next_state = []
            for sub in current:
                next_state.extend(nfa_map.get((sub, sym), []))
            next_state = sorted(set(next_state))

            if next_state:
                dfa_transitions[(tuple(current), sym)] = next_state
                if next_state not in dfa_states:
                    dfa_states.append(next_state)

    for group in dfa_states:
        for f in final_nodes:
            if f in group:
                dfa_final_nodes.append(group)
                break

    return dfa_states, dfa_transitions, [start_node], dfa_final_nodes


# Input Alphabet
symbols = ['0', '1']
start_node = 'p0'
final_nodes = ['p2']

# NFA definition (Example: accepts strings ending with "01")
nfa_map = {
    ('p0', '0'): ['p0', 'p1'],
    ('p0', '1'): ['p0'],
    ('p1', '1'): ['p2'],
}

nfa_state_list = ['p0', 'p1', 'p2']

# Print NFA Table
show_table(nfa_map, nfa_state_list, symbols, "NFA Transition Table")

# Convert to DFA
dfa_states, dfa_transitions, dfa_start, dfa_finals = convert_nfa_to_dfa(
    nfa_map, start_node, final_nodes, symbols
)

dfa_state_names = ["".join(st) for st in dfa_states]
dfa_trans_str = {("".join(s), sym): ["".join(t)]
                 for (s, sym), t in dfa_transitions.items()}

# Print DFA Table
show_table(dfa_trans_str, dfa_state_names, symbols, "DFA Transition Table")

print("\nDFA Start State:", "".join(dfa_start))
print("DFA Final States:", ["".join(st) for st in dfa_finals])
