def mean(i):
    
    total = 0
    for number in i:
        total = total+number
    return total/len(i)
        




data = [20, 21, 19, 22, 21, 20, 19, 20, 21, 20]
meanresult = mean(data)
print(meanresult)
lists = []
for numbers in data:
    numbs = numbers - meanresult
    lists.append(numbs)
    
for newnumbers in data:
    numbs = newnumbers*meanresult
    lists.append(numbs)
print(numbs)

data2 = [303, 299, 306, 298, 304, 307, 299, 302, 305, 299, 300]
result = mean(data2)
print(result)

    

data3 = [15.3, 14.9, 15.1, 15.2, 14.8, 14.7, 15.1, 14.8, 14.0, 15.0]
newresult = mean(data3)
print(newresult)



data4 = [87, 89, 84, 88, 89, 87, 86, 87, 86, 87]
result2 = mean(data4)
print(result2)