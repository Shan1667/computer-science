menu = input("please choose one of these option to run. Mean, Median, Mode, Frequency, Top 5 Numbers, Last 5 Numbersif mean in menu:")
if "mean" in menu:
    add = input("you have choosen mean. please enter 20 numbers")
# elif "median" in menu:
#     input("you have choosen median. please enter 20 numbers")
#     
# elif "mode" in menu:
#     input("you have choosen mode. please enter 20 numbers:")
# elif "frequency" in menu:
#     input("you have choosen frequency. please enter 20 numbers:")
# elif "top 5 numbers" in menu:
#     input("you have choosen top 5 numbers. please enter 20 numbers:")
# elif "last 5 numbers" in menu:
#     less = input("you have choosen :")
uservalue = []    
name = input("please enter the amount of times you would like to enter a number:")
number = int(name)
for i in range(number):
    e = input("please enter a number:")
    uservalue.append((float(e)))
print(uservalue)

save = input("please enter number 1 to calculate the mean:")
save = int(save)
if 1 == save:
    print("you have choosen mean")
    mean = 0
    for i in uservalue:
        mean = mean + i
    mean = mean /len(uservalue)
    