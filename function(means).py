def mean(i):
    
    total = 0
    for number in i:
        total = total+number
    return total/len(i)
        




data = [20, 21, 19, 22, 21, 20, 19, 20, 21, 20]
meanresult = mean(data)
print(meanresult)
lists = []
#now calcualte the diffrence from the mean
for numbers in data:
    numbs = numbers - meanresult
    lists.append(numbs)
#squares the values from the lsits
numbersofmean = []
for newnumbers in lists:
    resultsofmean = newnumbers*newnumbers
    numbersofmean.append(resultsofmean)
   # print(numbersofmean)
#add all of the square values
meanoflist = []  
for newmean in meanoflist:
    listsofmean = newmean+newmean
    meanoflist.append(listsofmean)
print(meanoflist)

data2 = [303, 299, 306, 298, 304, 307, 299, 302, 305, 299, 300]
result = mean(data2)
print(result)
listofmean = []
for number1 in data2:
    name = number1 - result
    listofmean.append(name)


data3 = [15.3, 14.9, 15.1, 15.2, 14.8, 14.7, 15.1, 14.8, 14.0, 15.0]
newresult = mean(data3)
print(newresult)
litsmean = []
for number2 in data3:
    names = number2 - newresult
    litsmean.append(names)


data4 = [87, 89, 84, 88, 89, 87, 86, 87, 86, 87]
result2 = mean(data4)
print(result2)
listsmeans = []
for number3 in data4:
    name3 = number3 - result2
    listsmeans.append(name3)