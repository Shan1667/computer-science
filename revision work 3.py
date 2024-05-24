# 
# numbers_of_list = []
# for i in range (5):
#     number = input("please enter a number:")
#     numbers_of_list.append(number)
#  
# print(numbers_of_list)
# list_of_number = []
# for e in numbers_of_list:
#     print(e)
#     list_of_number.append(int(e))
# print(list_of_number)
# 
# complete_list = []
# for s in list_of_number:
#     print(s+1)
#     complete_list.append(s+1)
# print(complete_list)
#     
# 
# hours = [12, 7, 9, 9, 6, 8, 2]
# milk = print()
# milks = 1.35
# 
# 
# 
# 
# 
# leaf = []
# for i in range (7):
#     leafs = input("please enter todays rainfall in cm:")
#     leaf.append(int(leafs))
# print(leaf)
# 
# print("total rainfall is",sum(leaf))
# average = sum(leaf)/len(leaf)
# print("average rainfall is",round(average,2))
# leaves = []
# counter = 0
# for r in leaf:
#     print(r)
#     if r > 3.5:
#         print("the rainfall has exceeded over 3.5cm")
#         if counter == 0:
#             print("day is monday")
#         elif counter == 1:
#             print("day is tuesday")
#         elif counter == 2:
#             print("day is wednesday")
#         elif counter == 3:
#             print("day is thursday")
#         elif counter == 4:
#             print("day is friday")
#         elif counter == 5:
#             print("day is saturday")
#         elif counter == 6:
#             print("day is sunday")
#     leaves.append(r)
#     counter = counter+1
# print(leaves)
# 

print("welcome")
print("please choose an option below")
print("1. enter sales data")
print("2. view total sales to date")
print("3. view maximum sales value of any staff member")
print("4. view maximum sales of any staff memeber")
print("5. view average sale value of any staff mumber")
salename = []
salevalue = []
while True:
    
    print("please choose an option below")
    print("1. enter sales data")
    print("2. view total sales to date")
    print("3. view maximum sales value of any staff member")
    print("4. view maximum sales of any staff memeber")
    print("5. view average sale value of any staff mumber")
    store = input("please choose an option:")
    if "one" in store:
        username = input("please enter the users name:")
        value = input("please enter the users value of sales:")
        value = float(value)
        salename.append(username)
        salevalue.append(value)
    elif "two" in store:
        
        totalsale = sum(salevalue)
        print("the total sales made to date is",totalsale)
    elif "three" in store:
        name = input("please enter the a staff memeber name:")
        for sale in   
        
        value = input("the maximum sale to date the person", name,"is:")
    elif "four" in store:
        input("please enter the staff member name:")
        value = input("please enter the muinimum value of thier sales to date:")
    elif "five" in store:
        input("please enter the staff memeber name:")
        value = input("please enter the staff member average sales to date:")
    

    
