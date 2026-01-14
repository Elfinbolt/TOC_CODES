import re

# Simple sets
a = {1, 2}
b = {2, 3}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric Difference:", a ^ b)

# Regex checks
# Ends with '01'
txt1 = "1101"
m1 = re.fullmatch(r'(0|1)*01', txt1)
print("m1" if m1 else "no match 1")

# Only 'ab' repeated
txt2 = "ababab"
m2 = re.fullmatch(r'(ab)*', txt2)
print("m2" if m2 else "no match 2")

# Only '01' repeated
txt3 = "010101"
m3 = re.fullmatch(r'(01)*', txt3)
print("m3" if m3 else "no match 3")

# Starts and ends with 'sp'
txt4 = "spsp"
m4 = re.fullmatch(r'sp(sp)*', txt4)
print("m4" if m4 else "no match 4")

# Even number of 'a's
txt5 = "aaaa"
m5 = re.fullmatch(r'(aa)*', txt5)
print("m5" if m5 else "no match 5")
