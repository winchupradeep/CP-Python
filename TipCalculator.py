print('\n\n\n')
print("-------Tips Calculator -------")
print('\n')
food_amount = float(input("Enter the food amount 💰: "))
tip = float(input("Enter the tip percentage % : "))
tip_percent = tip/100
tip_amount = float(food_amount*tip_percent)
total_amount = float(food_amount+tip_amount)
print(f"The total amount to be paid is 💸: ${total_amount}"
print('\n')
print("-------Thank You------")