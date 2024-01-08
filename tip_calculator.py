#ask for total bill
bill = float(input("What is the total bill? GHC"))

#ask for tip percentage
tip = int(input("What is the tip you are giving? 10, 12, 15: "))

#ask how many people are to share bill
people = int(input("How many people are sharing the bill? "))

#Calculte tip percentage
tip_percent = tip / 100

# find tip amount
tip_amount = bill * tip_percent

# add tip to the total bill
total_bill = bill + tip_amount

# calculate price per person
each_amount = total_bill / people
each_amount = round(each_amount, 2)

# display total amount
print(f"Each person is to pay GHC{each_amount}")
