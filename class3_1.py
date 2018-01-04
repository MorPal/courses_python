# Class 3.1

# Creating a simple function with a parameter

print("hello","world!")

my_type = type(2.2)

my_type

# Simple function

def say_hi():
    print("hello there!")
    print("hasta la vista, baby")

def three_3_function():
    print(33)

three_3_function()

say_hi()

def yell_it(an):
    print(an.upper() + "!")
# end function yell_it

to_yell = input("que deseas chillar: ")
yell_it(to_yell)

# how to asing default variable
def yell_it(an = "ni idea"):
    print(an.upper() + "!")
# end function yell_it

yell_it()
