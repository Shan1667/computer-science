name = input("Hello there, what is your name?:")
print("so your name is", name,". alright then lets play a game")
score = 1
chances_left = 4
print("we will play hangman, the word will contain 10 words, you will aslo have 6 tries to get the correct word")
wrd = input("please guess your letter:")
word = "technology"
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
                wrd = input("please guess your letter:")
    else:
      print("try again")
      score = 1
      print(word_list)
      wrd = input("please guess your letter:")
      chances_left = chances_left - 1

