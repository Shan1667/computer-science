name = input("please press 1 if want to convert a binary number to a decimal number or press 2 to enter a decimal number to a binary number:")
if "1" in name:
    names = input("please enter a 5 digit binary number:")
elif "2"in name:
    numb = input("please enter a 5 digit decimal number:")
        total = 0
    numbs = len(numb)
    for digit in numb:
        total = total+