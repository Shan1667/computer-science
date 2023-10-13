number = input("please enter a number between 10 and 20:")
number = int(number)
if number <=20 and number >= 10:
    print("thank you")
else:
    print("try again")
bottles_left = 9
bottle = input("There are 10 green bottles hanging in the wall. 10 green bottles hagging from the wall and if one bottle should accidentally fall how many green bottles are there left?:")
while int(bottle) > 0:
    if int(bottle) == bottles_left:
        print("there will be ",bottles_left, "green bottles hanging on the wall")
       
        bottle = input("There are"+ str( bottles_left)+ "green bottles hanging in the wall 9 green bottles hagging from the wall and if one bottle should accidentally fall how many green bottles are there left?:")
        bottles_left = bottles_left -1
        #print("there will be ",bottles_left, "green bottles hanging on the wall")
      #  bottle = input("there are"+ str( bottles_left)+ "green bottles hanging in the wall 8 green bottles hanging from the wall and if one botlle should accidentally fall how many bottles are there left?")
        print("there are no more bottles hanging on the wall")
    else:
        print("no, try again")