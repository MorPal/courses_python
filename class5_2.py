# Class 5.2

# Basic math operators

# [ ] review and run example
print("3 + 5 =",3 + 5)
print("3 + 5 - 9 =", 3 + 5 - 9)
print("48/9 =", 48/9)
print("5*5 =", 5*5)
print("(14 - 8)*(19/4) =", (14 - 8)*(19/4))

# [ ] review and run example - 'million_maker'
def million_maker():
    make_big = input("enter a non-decimal number you wish were bigger: ")
    return int(make_big)*1000000

print("Now you have", million_maker())
