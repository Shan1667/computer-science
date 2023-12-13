#name = input("enter 4 numbers:")
list1=[100,2,3,4,5,6,7,8]
list2 = []
for i in list1:
    list2.append(i)
list1[1]=list1[2]
#print(len(list1))
for name in range(len(list1)-1):
    list1[name+1]=list1[name]
print(list1)