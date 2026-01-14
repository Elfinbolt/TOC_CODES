# Number of transitions
t_count = int(input("Enter number of transitions: "))
fsm_rules = {}

print("Enter transitions in format: state input next_state output")

# Taking transitions as input
for _ in range(t_count):
    st, ch, nxt, op = input().split()
    fsm_rules[(st, ch)] = (nxt, op)

# Starting state and input string
start = input("Enter starting state: ")
bin_str = input("Enter a binary number: ")

result = ""
curr = start

# Process the binary string in reverse
for bit in reversed(bin_str):
    if (curr, bit) in fsm_rules:
        nxt_state, op_val = fsm_rules[(curr, bit)]
        result = op_val + result
        curr = nxt_state
    else:
        print(f"No rule for state {curr} with input {bit}")
        break

# Final output
print("Input binary :", bin_str)
print("Output string:", result)
