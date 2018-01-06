# Class 4.2

# Comparision operators

3 < 5

3 > 5

3 >= 3

# Equal
3 == 3

# Not Equal
3 != 9

x_1 = input("number: ")
x = float(x_1)
if x > 25:
    print("number greater than 25")
else:
    print("x was", x)
    x = 26
    print("x now is: ", x)

# review code and run cell
x = 21
if x > 25:
    print("x is already bigger than 25")
else:
    print("x was", x)
    x = 25
    print("now x is", x)

# review code and run cell
x = 18
if x + 18 == x + x:
    print("Pass: x + 18 is equal to", x + x)
else:
    print("Fail: x + 18 is not equal to", x + x)

# review code and run cell. "!" means "not"
x = 18
test_value = 18
if x != test_value:
    print('x is not', test_value)
else:
    print('x is', test_value)

# review code and run cell
# DON'T ASSIGN (x = 2) when you mean to COMPARE (x == 2)
x = 2

if x == 2:
    print('"==" tests for, is equal to')
else:
    pass
