counts = {}
counts2 = dict({})
print(counts)
print(counts2)

menu = input("please enter frequency to see how many words come up or enter characters to see how many characters come up:")
if "frequency" in menu:
    sentence = input("please enter a sentence:")
    sentence = sentence.upper()
    print(sentence)
    words = sentence.split()
    print(words)
    for item in words:
        
        if item in counts:
            
            counts[item] = counts[item] + 1
        else:
            
             counts[item] = 1
    print(counts)

if "characters" in menu:
    letters = input("please enter a sentence to calculate each characters:")
    letters = letters.upper()
    print(letters)
    for item in letters:
        
        if item in counts:
            
            counts[item] = counts[item] + 1
        else:
            
             counts[item] = 1
    print(counts)
  

book = open("book.txt","r")
x = book.read()
print(x)

names = x.split()
print(names)
for number in names:
    if number in counts:
        counts[number] = counts[number] + 1
    else:
        counts[number] = 1
print(counts)


#sentence = sentence.upper()
#print(sentence)
#words = sentence.split()
#print(words)
#for item in words:
    #if item in counts:
        #counts[item] = counts[item] + 1
   # else:
        #counts[item] = 1
#print(counts)


