nameZ = ["computer", "science"]
nameZ = ["computer", "science",12,15,4]
nameZ = ["computer", "science", 12,15,4,["inner","list"]]
nameZ = ["computer","science",12,15,4,["inner","list"],"computer","science"]
print(nameZ)
    
b = ["Hello"," world", "I", "need","some","other","words",21,35,789]
first_item = b[0]
third_item = b[2]
Num_items_in_lst = len(b)
last_item = b[Num_items_in_lst -1]
last_item = b[-1]

thislist = ["Apple", "Banana", "Cherry", "Orange", "Kiwi", "Melon", "Mango"]
print(thislist[-4:-1])

b = "Hello world!"
print(b[2:10:3])

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 =list1 + list2
print(list3)

b = ["hello"]
output_list = b*2
print(output_list)

My_string = "Hello"
My_string_upper = My_string.upper()
print(My_string_upper)
My_string = My_string.upper()
print(My_string)

thislist = ["Apple", "banana", "Cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple","Banana", "Cherry", "Orange", "Kiwi", "Mango"]
thislist[1:3] = ("blackcurrant", "watermelon")
print(thislist)

txt = "The best things in life are free!"
if 'free' in txt:
    print("yes, 'free' is present.\n")
    
    lst = [ 1, 6, 3, 5, 3, 4 ]
    if 7 in lst:
        print("7 is in the lst")
else:
            print("7 is not in the lst")
            
txt = "The best things in life are free!"
if 'expensive' not in txt:
    print("no, 'expensive' is NOT present.\n")
    
    lst = [ 1, 6, 3, 5, 3, 4 ]
    if 7 not in lst:
        print("7 is not in the lst")
else:
            print("7 is in the lst") 