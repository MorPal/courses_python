# Class 2_4

# String formatting methods
# Formatting string input()
# Boolean in keyword

print("ms. Browing is In Rg".lower())
print("ms. Browing is In Rg".upper())
print("ms. Browing is In Rg".capitalize())
print("ms. Browing is In Rg".title())
print("ms. Browing is In Rg".swapcase())

# Input formatting

#fav_color = input('Insert favourite colour: ').lower()
#print(fav_color)

#fav_color = input('Insert favourite colour: ')
#print(fav_color.upper())

# Return a boolean

menu = "Salad pizza drinks"
print('pizza' in menu)

menu = "Salad pIzZa drinks"
print('Pizza'.lower() in menu.lower())

# [ ] fix the error
paint_colors = "red, blue, green, black, orange, pink"
print('Red in paint colors = ','red'.lower() in paint_colors.lower())

name = "SKYE HOMSI"
print("y" in name.lower())
