# Class 4.3

# String comparisons

# review and run code
"hello" < "Hello"

# review and run code
"Aardvark" > "Zebra"

# review and run code
'student' != 'Student'

# review and run code
print("'student' >= 'Student' is", 'student' >= 'Student')
print("'student' != 'Student' is", 'student' != 'Student')

# review and run code
"Hello " + "World!" == "Hello World!"

# [ ] review and run code
msg = "Save the notebook"

if msg.lower() == "save the notebook":
    print("message as expected")
else:
    print("message not as expected")

# [ ] review and run code
msg = "Save the notebook"
prediction = "save the notebook"

if msg.lower() == prediction.lower():
    print("message as expected")
else:
    print("message not as expected")


name = "Tobias"

print(name == "Alton")
