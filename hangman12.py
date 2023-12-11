["O",""]
figure = ["---------------- \n   o     |\n  /|\\    |\n  / \    |\n         |\n         |\n         |\n---------------\n","---------------- \n         |\n  /|\\    |\n  / \    |\n         |\n         |\n         |\n---------------\n"]


name = input("Hello there, what is your name?:")
print("so your name is", name,". alright then lets play a game")
score = 0
chances_left = 4
print("we will play hangman, the word will contain 10 words, you will aslo have 6 tries to get the correct word")
wrd = input("please guess your letter:")
word = "computer"
word_list = ['_']*len(word)
print(word_list)
time = word.count(word)
while chances_left >= 0:
    
    if wrd in word:
        for letter_position in range(len(word)):
            if word[letter_position] == wrd:
                word_list[letter_position] = wrd
                print("good job")
                print(word_list)
                print(wrd)
                score =score + 1
                print("score =",score )
       
                
                
    else:
      print("try again")
      print(word_list)
      print(wrd)
      print("score =", score,)
      chances_left = chances_left - 1
      print("You have", chances_left+1, "lives remaining")
      print(figure[1])
      
    if score == len(word):
        break
    if chances_left < 0:
        print("game over, the word was computer")
        break
    wrd = input("please guess your letter:")  