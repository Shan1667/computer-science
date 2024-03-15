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
    
lists2 = input("please enter 6 numbers:")
lists = int(lists2)
for "lists2" in range