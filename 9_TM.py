tape = list(input("Enter a binary string (e.g. 0101): "))
tape.append('_')  
head = 0
state = 'q0'  

def move_head(direction):
    global head
    if direction == 'R':
        head += 1
    elif direction == 'L':
        head -= 1

def print_tape():
    print("".join(tape))
    print(" " * head + "^")
    print(f"State: {state}\n")

while True:
    print_tape()
    symbol = tape[head]

    if state == 'q0':  
        if symbol == '0':
            move_head('R')
        elif symbol == '1':
            state = 'q1'  
            move_head('R')
        elif symbol == '_':
            state = 'accept'
            break

    elif state == 'q1':  
        if symbol == '0':
            move_head('R')
        elif symbol == '1':
            state = 'q0'  
            move_head('R')
        elif symbol == '_':
            state = 'reject'
            break
    else:
        break

if state == 'accept':
    print("String has even number of '1's. ACCEPTED.")
else:
    print("String has odd number of '1's. REJECTED.")