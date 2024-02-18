name = input("please press 1 if want to convert a binary number to a decimal number or press 2 to enter a decimal number to a binary number:")
#if "1" in name:

   # names = input("please enter a 5 digit binary number:")
if "2"in name:
    total = 0
    numb = input("please enter a 5 digit decimal number:")
    numbs = len(numb)-1
    for digit in numb:
        total = total+ int(digit) * 2** numbs
        numbs = numbs -1 
#for number in names:
print(total)


name = input("please press 1 if want to convert a binary number to a decimal number or press 2 to enter a decimal number to a binary number:")
if "1" in name:
    total = 0
    names = input("please enter a 5 digit binary number:")
#elif "2"in name:
  #  numb = input("please enter a 5 digit decimal number:")
    numbs = len(names)-1
    for digit in names:
        total = total+ int(digit) * 2** numbs
        numbs = numbs -1 
#for number in names:
print(total)
