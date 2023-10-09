
numbers = input("please enter a number that is under 20:")
numbers = int(numbers)
if numbers < 20:
    print("Thank You!")
else:
    print("Too High!")
                
num = input("please enter a number between 10 and 20:")
num = int(num)
if num  <=20 and num >= 10:
    print("Thank you")
else:
    print("Incorrect answer")
    
colour = input("what is your favorite colour:")
if "red" in colour:
    print("I like red too!")
else:
    print("i dont like",colour,"I prefer red")

number = input("please add a number that is less than 50:")
number = int(number)
while  number < 50:
    print("please add more numbers")
    number = input("please add a number that is less than 50:")
    number = number+int(number)
else:
    print("Thank you!")
    
add = input("please add number:")
add = int(add)
while add < 5:
    print("please add another number")
    add = input("please add number")
    add = add+int(add)
else:
    print("the last number you entered was",add,)
    
adding = input("please add a number:")
adding = input("please add another number:")
adding = int(adding)
adding = print(adding + adding) 