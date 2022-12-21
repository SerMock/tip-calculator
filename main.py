print("\033[1;34mTip calculator")
print("\033[1;34m--------------")
print()

#Enter total bill amount
total_bill = float(input("\033[0;34mWhat was the total bill?\033[0;35m\n$"))

print()

#Enter percentage of tip
percentage_sign = "%"
tip_percentage = int(input("\033[0;34mThe tip percentage you want to give\n\033[0;35m"))

#Mathmatical result of the tip amount
tip_amount = tip_percentage / 100 * total_bill
tip_amount_conversion = round(tip_amount, 2)

print()

#Enter the number of people splitting the bill
people_count = int(input("\033[0;34mThe number of people who will split the bill\n\033[0;35m"))

print()

#Mathmatical result of the final bill with the tip included.
bill_with_tip = tip_percentage / 100 * total_bill + total_bill
bill_with_tip_conversion = "{:.2f}".format(bill_with_tip)
tip_notification = print(f"\033[0;34mThe tip will be:\033[0;35m \n${tip_amount_conversion}")
print()
print(f"\033[0;34mThe final bill with tip:\n\033[0;35m${bill_with_tip_conversion}")

print()

#How much each person will pay
split_bill = bill_with_tip / people_count
final_amount = "{:.2f}".format(split_bill)
print(f"\033[0;34mEach person should pay:\n\033[0;35m${final_amount}")
