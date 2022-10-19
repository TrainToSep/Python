print ("Welcome to the tip calculator! \n")
total_bill = input ("What was the total bill $? \n")
total_bill = float (total_bill)
tip = input ("How much tip would you like to pay? 10, 12 or 15? \n")
tip = int (tip)
people = input ("How many people to split the bill? \n")
people = int (people)
tip_as_percent = tip / 100
tip_per_person = tip_as_percent * total_bill
total_bill = tip_per_person + total_bill
total_bill = round (total_bill, 2)
total_bill = "{:.2f}".format(total_bill)
print (f"Each people should pay ${total_bill}")