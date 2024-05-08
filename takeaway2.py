takeaway_menu = ["1. Pad Thai","2. Chicken Tikka Masala","3. Pepperoni Pizza","4. Veggie Burger with Fries","5. Burrito Bowl"]
takeaway_prices = [12.99, 14.50,  9.99,  15.99,  11.50]

delivery_fee = 5.00
free_delivery_price = 30.00
fee = [30.00]

name = input("please enter your name before you can enter the takeaway:")
print("Welcome to the takeaway delivery service.")
print("Here's our menu.")

for item in takeaway_menu:
    print(item)

quantity = int(input("How many items would you like to purchase?"))
order = []
for i in range(quantity):
    choice = int(input("Enter the menu number of the item you wish to add to your order: "))
    order.append(choice)
print("Thank you", name,"your order is as follows")
for item in order:
    print(takeaway_menu[item-1])
    
print(quantity)
print(order)

takeaway_prices2 = 0
for quantity in order:
    print(takeaway_prices[quantity -1])
    takeaway_prices2 = takeaway_prices2+takeaway_prices[quantity -1]
  
  # print(quantity)

print("your total is",takeaway_prices2,)
if takeaway_prices2 > fee:
    print("since your order costs more than €30 you will get free delivery!")
    
#
#When the user enters:
#1 -> 0
#2 -> 1
#3 -> 2

#1. Read throught the program, then run it to make sure you understand what it is doing.
#2. Ask the user for their name and save it in an appropriately named variable.
#3. Include the user's given name in the print statement where they are thanked for their order.
#4. Write a loop that calculates the total value of the order and prints this number to the screen with an appropriate description.
#5. Alter the program so the delivery_fee is added to the total price of the order unless the
    #total value of the food is greater than value of free_delivery_price. Print this new value to the screen with appropriate text.
#6. Create a function called get_bill_total that combines the code added in step 4 and 5. Have the program call this function. 