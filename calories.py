file = open("C:\\Users\\20SShahid.ACC\\Documents\\Exercise.csv", "r")
name = file.readline()
print(name)
count60 = 0
lists = []
for line in file:
    line = line.strip()
    line = line.split(",")
    lists.append(line)
_60minutesessions = 0.0
for item in lists:
    if(item[0] == "60"):
        if item[3] != "":
            _60minutesessions += float(item[3])
            count60 = count60 + 1
            
average = _60minutesessions/count60
print(average)

count60 = 0
_60minutesessions = 0.0
for item in lists:
    if(item[0] == "45"):
        if item[3] != "":
            _60minutesessions += float(item[3])
            count60 = count60 + 1

names = _60minutesessions/count60
print(names)
     
    
     
     
     
     
     
     
duration = input("please enter the duration of your excersie:")
calories = input("please enter the amount of calories you burned:")

     
#print(f'{item} --- {item[0]}')

    
#    # _60minutesessions = 0
#     for i in lists:
#         _60minutesessions = _60minutesessions + i
#     _60minutesessions = _60minutesessions /len(lists)
# _60minutesessions = round(_60minutesessions, 1)
# print(_60minutesessions)
