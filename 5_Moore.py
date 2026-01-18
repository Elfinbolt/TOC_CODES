# Number of transitions
t_count = int(input("Enter number of transitions: "))
fsm_rules = {}

print("Enter transitions in format: state input next_state")

# Taking transitions as input
for _ in range(t_count):
    st, ch, nxt = input().split()
    fsm_rules[(st, ch)] = nxt

# State outputs
state_output = {}
s_count = int(input("Enter number of states with outputs: "))
print("Enter in format: state output")
for _ in range(s_count):
    st, op = input().split()
    state_output[st] = op

# Starting state and input string
start = input("Enter starting state: ")
bin_str = input("Enter a binary number: ")

result = ""
curr = start

# Moore machine: output depends only on the current state
result += state_output.get(curr, "")

# Process the binary string in reverse
for bit in bin_str:
    if (curr, bit) in fsm_rules:
        curr = fsm_rules[(curr, bit)]
        result += state_output.get(curr, "")
    else:
        print(f"No rule for state {curr} with input {bit}")
        break

# Final output
print("Input binary :", bin_str)
print("Output string:", result)
