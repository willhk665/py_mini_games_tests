#Tip Calculator
#Bill Amount
bill = float(input("What is your total bill? $"))

#Tip %
tip_per = int(input("What percentage tip would you like to pay, 10, 12 or 15? "))
#Number of people
people = int(input("How many people to split the bill? "))
#Calculation per person
result = (bill + bill * (tip_per/100)) / people
result_rounded = "{:.2f}".format(result)
print(f"Each person should pay ${result_rounded}")