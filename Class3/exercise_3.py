# Exercise 3

# [ ] define and call a function short_rhyme() that prints a 2 line rhyme
def short_rhyme(line1, line2):
    return print(line1 + '\n' + line2)

l1 = input('Rhyme 1: '.lower())
l2 = input('Rhyme 2: '.lower())

short_rhyme(l1,l2)

print('########' + '\n------' + '\n########')

# [ ] define (def) a simple function: title_it() and call the function
# - has a string parameter: msg
# - prints msg in Title Case

def title_it(msg):
    return print(msg.title())

title_it(l1)
title_it(l2)

# [ ] get user input with prompt "what is the title?"
# [ ] call title_it() using input for the string argument

title = input('what is the title?: ')
title_it(title)

# [ ] define title_it_rtn() which returns a titled string instead of printing
# [ ] call title_it_rtn() using input for the string argument and print the result

def title_it_rtn(msg):
    return msg.title()

rtn = title_it_rtn(title)
print(rtn)

#########

def make_greeting(name, greeting = "Hello"):
    return (greeting + " " + name + "!")
    
def get_name():
    name_entry = input("enter a name: ")
    return name_entry

def get_greeting():
    greeting_entry = input("enter a greeting: ")
    return greeting_entry

# get name and greeting, send to make_greeting
print(make_greeting(get_name(), get_greeting()))
