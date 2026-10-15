bill = float(input("Enter total bill amount: "))
tip_percentage = float(input("Enter tip percentage: "))
people = int(input("Enter number of people: "))

tip = bill * tip_percentage / 100
total_bill = bill + tip
per_person = total_bill / people

print("Total Tip:", tip)
print("Total Bill Including Tip:", total_bill)
print("Amount Per Person:", per_person)