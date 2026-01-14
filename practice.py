ip_string = list(input("enter a string 0,1 only :"))
head = 0
state = 'q0'

def move_head(direction):
  global head
  if direction == 'R':
    head += 1
  elif direction == 'L':
    head -= 1

def print_tape():
  print("".join(ip_string))
  print(head * " " + "^")
  print(f"state = {state}\n")
  
while(True):
  print_tape()
  symbol=ip_string[head]
  if state=='q0':
    if symbol==0:
      move_head('R')
    