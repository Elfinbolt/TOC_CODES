# DFA components
states = {'q0', 'q1', 'q2'}
alphabet = {'0', '1'}

# Transitions
transitions = {
    ('q0', '0'): 'q1',
    ('q0', '1'): 'q0',
    ('q1', '0'): 'q1',
    ('q1', '1'): 'q2',
    ('q2', '0'): 'q1',
    ('q2', '1'): 'q0'
}

start_state = 'q0'
accept_state = 'q2'

# Get input from user
input_string = input("Enter input string: ")

# DFA simulation
current_state = start_state
print(f"Start at state: {current_state}")

for symbol in input_string:
    if (current_state, symbol) in transitions:
        next_state = transitions[(current_state, symbol)]
        print(f"On input '{symbol}', {current_state} → {next_state}")
        current_state = next_state
    else:
        print(f"Rejected: No transition for ({current_state}, '{symbol}')")
        break
else:
    print(f"Final state: {current_state}")
    if current_state == accept_state:
        print("Result: Accepted ✅")
    else:
        print("Result: Rejected ❌")
