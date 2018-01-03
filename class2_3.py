# Class 2.3

# Quotes inside strings / boolean string test methods

print("it's hammer time")

print("He said: 'oh la la'")

# boolean strings

"Python".isalpha()      #true // only letters of the alphabet
"Python! ".isalpha()    #false
"3rd".isalnum()         #true digit and alphabetics // alphanumeric
"3rd ".isalnum()        #false - space
"save".starswith('s')   #true
"HEY".itupper()         #true
"The End".istitle       #true - each word separate
"The end".istitle       #false
