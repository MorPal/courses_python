# Class 3.2

# Exploring Functions with return values
# Creating Functions with multiple parameters

def msg_double(phrase):
    double = phrase + " " + phrase
    return double

msg_2x = msg_double("let's go")
print(msg_2x)

def half_value(value):
    return value/2

value = input("number to divide by 2: ")
print(half_value(float(value)))

# Multiple parameters

def make_schedule(period1, period2):
    schedule = ("[1st]" + period1.title() + ", [2nd]" + period2.title())
    return schedule

student_schedule = make_schedule("maths", "history")

print("Schedule: ", student_schedule)
