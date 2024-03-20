add1 = input("enter a number:")
add1 =int(add1)
add2 = input("please enter a second number:")
add2 =int(add2)

def name(a,b):
  totals = a + b
  return totals

num =name(add1,add2)
print(num)


word = input("please enter a word:")
un = "un"
def names(c,d):
  total1 = c + d
  return total1

numbs = names(un,word)
print(numbs)


words = input("please enter a palindrome word that means the same fowards and backwards:")

def string(A):
    b=A[::-1]
    return b

num = string(words)
if num==words:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
#program 4  
list2 = input("please enter numbers:(enter x to end)")
lists3 = []
while list2  != "x":
    if list2.isdigit():
         lists3.append(int(list2))
    list2 = input("please enter numbers:(enter x to end)")

print(lists3)

for item in lists3:
    print(list2)
if item %2 == 0:
    evencounter += 1
    eventotal += add
else:
    addcounter += 1
    addtotal += add
    
print(item)
