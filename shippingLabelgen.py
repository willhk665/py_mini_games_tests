#Shipping Label Generator

print("Welcome to Shipping Label generator!")

#Shipping address variables
name = input("What is your name?\n")
address = input("What is your street address?\n")
city = input("What city are you from?\n")
province = input("What is your province?\n")
postal_code = input("What is your postal code?\n")
country = input("What's your country?\n")

#Label test function
shipping_label = "\n"+ name + " your shipping label is" + "\n" + address + "\n" + city + ", " + province + " " + postal_code + "\n" + country + "\n"
print(shipping_label)

#Number of characters in the label
print("The number of characters in you label is:")
print(len(shipping_label))