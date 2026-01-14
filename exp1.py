# Sets
a = {1, 2, 3, 4}
b = {4, 5, 6, 7}
print("The union of two sets", a | b)
print("The intersection of two sets", a & b)
print("The difference of two sets", a - b)
print("The symmetric difference of two sets", a ^ b)

# Ends with '01'
text1 = "000101"
if text1.endswith("01") and all(ch in "01" for ch in text1):
    print("match1")
else:
    print("no match 1")

# Starts and ends with 1
text2 = "1100101"
if text2.startswith("1") and text2.endswith("1") and all(ch in "01" for ch in text2):
    print("match2")
else:
    print("no match 2")

# Only even number of 's'
text3 = "sssssp"
if len(text3) % 2 == 0 and all(ch == "s" for ch in text3):
    print("match3")
else:
    print("no match 3")

# Only 'sp'
text4 = "spspsp"
if text4 == "sp" * (len(text4) // 2):
    print("match4")
else:
    print("no match 4")

# Starts and ends with '12'
text5 = "12111212"
if text5.startswith("12") and text5.endswith("12") and all(ch in "12" for ch in text5):
    print("match5")
else:
    print("no match 5")
