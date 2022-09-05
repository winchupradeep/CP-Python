print("Tips Calculated to 20'%' of food amount")

food_amount = int(input("Enter the food amount: "))
tip_percent = 20/100
tip_amount = (food_amount*tip_percent)
total_amount = food_amount+tip_amount
print("The total amount to be paid is : ",'$'+str(total_amount))