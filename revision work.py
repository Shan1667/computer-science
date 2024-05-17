
numbers_of_list = []
for i in range (5):
    number = input("please enter a number:")
    numbers_of_list.append(number)
 
print(numbers_of_list)
list_of_number = []
for e in numbers_of_list:
    print(e)
    list_of_number.append(int(e))
print(list_of_number)

complete_list = []
for s in list_of_number:
    print(s+1)
    complete_list.append(s+1)
print(complete_list)
    

hours = [12, 7, 9, 9, 6, 8, 2]
milk = print()





leaf = []
for i in range (7):
    leafs = input("please enter todays rainfall in cm:")
    leaf.append(int(leafs))
print(leaf)
print("total rainfall is",sum(leaf))
average = sum(leaf)/len(leaf)
print("average rainfall is",round(average,2))
leaves = []
for r in leaf:
    print(r)
    leaves.append(r)
print(leaves)
    
