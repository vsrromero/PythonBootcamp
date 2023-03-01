total_bill = float(input('What was the total bill?\n'))
tip_rate = float(input('How much tip would you like to give? 10, 12 or 15?\n'))
people = int(input('How many people to split the bill?\n'))

tip = round(total_bill * tip_rate / 100, 2)
bill_per_person = round((total_bill + tip) / people, 2)
print(bill_per_person)