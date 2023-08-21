# How to sort a Python dict by value
# (== get a representation sorted by value)

rep = {"a":4, "b":3, "c":2, "d":1}
sorted(rep.items(), key=lambda x: x[1])
print(rep)