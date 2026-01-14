# DFA components
states = {'q0', 'q1'}
alphabet = {'0', '1'}

# Transitions
transitions = {
    ('q0', '0'): 'q1',
    ('q0', '1'): 'q0',
    ('q1', '0'): 'q0',
    ('q1', '1'): 'q1'
}

start_state = 'q0'
accept_state = {'q0'}  # Even number of 0's

# Get input from user
input_string = input("Enter input string: ")

# DFA simulation
current_state = start_state
for symbol in input_string:
    if (current_state, symbol) in transitions:
        current_state = transitions[(current_state, symbol)]
    else:
        print("Rejected: symbol not in alphabet or no transition defined.")
        break
else:
    if current_state in accept_state:
        print("Accepted")
    else:
        print("Rejected")
