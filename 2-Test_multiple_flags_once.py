# Different ways to test multiple flags at once in Python
x, y, z = 0, 1, 0

if x==1 or y==1 or z==1:
    print("### First ###")
    print("Passed")
    print("")
    print("### Next ###")

if 1 in (x, y, z):
    print("Passed")
    print("")
    print("### Next ###")

# Testing for truthiness
if x or y or z == 1:
    print("Passed")
    print("")
    print("### Next ###")

if any((x, y, z)):
    print("Passed")
    print("")
