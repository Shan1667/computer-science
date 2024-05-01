import random
start = input("Hello. would you like to play the game mastermind. press yes if you want to start:")
if "yes" in start:
   rules = input("would you like to know the game rules:")
if "yes" in rules:
    print("here are the rules.1 you will need to guess 4 colours to win.2 you will need to guess the colour and need to make sure that it is in the correct place.3 you will see how many attmepts it took in the end.4 have fun")


colour = ["red","blue","green","yellow","orange","purple","white","black","pink"]
computerColourChoice = []
for i in range(4):
   computerColourChoice.append(random.choice(colour))
print(computerColourChoice)
for i in range(4):
    userColourChoice.append = input(("please enter 4 colour names:"))
if userColourChoice[i] == computerColourChoice[i]:
    correctcolour = correctcolour +1

