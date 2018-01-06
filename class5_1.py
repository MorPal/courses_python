# Class 5.1

# Conditionals: elif
# Casting

# WHAT TO WEAR
weather = input("Enter weather (sunny, rainy, snowy): ")

if weather.lower() == "sunny":
    print("Wear a t-shirt")
elif weather.lower() == "rainy":
    print("Bring an umbrella and boots")
elif weather.lower() == "snowy":
    print("Wear a warm coat and hat")
else:
    print("Sorry, not sure what to suggest for", weather)

# [ ] review the code then run testing different inputs
# SECRET NUMBER GUESS
secret_num = "2"

guess = input("Enter a guess for the secret number (1-3): ")

if guess.isdigit() == False:
    print("Invalid: guess should only use digits")
elif guess == "1":
    print("Guess is too low")
elif guess == secret_num:
    print("Guess is right")
elif guess == "3":
    print("Guess is too high")
else:
    print(guess, "is not a valid guess (1-3)")

# Casting
# int()
# str()
# float()

weight1 = '60' # a string
weight2 = 170 # an integer
# add 2 integers
total_weight = int(weight1) + weight2
print(total_weight)
