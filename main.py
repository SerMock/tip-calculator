print("Tip calculator")

#Enter total bill amount
total_bill = float(input("What was the total bill? $"))

#Enter percentage of tip
tip_percentage = int(input("The tip percentage you want to give "))

#Mathmatical result of the tip amount
tip_amount = tip_percentage / 100 * total_bill
tip_amount_conversion = round(tip_amount, 2)
tip_notification = print(f"The tip will be ${tip_amount_conversion}")

#Enter the number of people splitting the bill
people_count = int(input("The number of people who will split the bill "))

#Mathmatical result of the final bill with the tip included.
bill_with_tip = tip_percentage / 100 * total_bill + total_bill
bill_with_tip_conversion = "{:.2f}".format(bill_with_tip)
print(f"The final bill with tip ${bill_with_tip_conversion}")

#How much each person will pay
split_bill = bill_with_tip / people_count
final_amount = "{:.2f}".format(split_bill)
print(f"Each person should pay: ${final_amount}")
