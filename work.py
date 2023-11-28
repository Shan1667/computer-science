name = input("please enter your name:")
print("hello, your name is", name,)

numb = input("please enter two number")
numbs = input("lpease enter another number")
print("the answer is", numb + numbs,)

temperature = int(input("Enter the Temperature in Celsius :\n"))
temperature2 = (9.5 * temperature) + 32.
print("Temperature in Fahrenheit :", temperature2)

def intrest(numbs,numb,number):
    print('The principal is', numbs)
    print('The time period is', numb)
    print('The rate of interest is',number)
     
    si = (numbs * numb* number)/100
     
    print('The Simple Interest is', si)
     
numbs = int(input("Enter the principal amount :"))
numb = int(input("Enter the time period :"))
number = int(input("Enter the rate of interest :"))
intrest(numbs,numb,number)
 