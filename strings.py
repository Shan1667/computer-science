pangram = "The quick brown fox jumps over the lazy dog!"
print(pangram[1:5])
print(pangram[17:19])
print(pangram[:19])
print(pangram[20:26])
print(pangram[26:])

word1 = " Leaving"
word2 = " Certificate"
word3 = " computer"
word4 = " Science"
subjectName = word1 + word2 + word3 + word4
print(subjectName)

pangram = "The quick brown fox jumps over the lazy dog!"
print(pangram[:3] + pangram[16:])

noun = input("Enter a singular noun: ")
print("The plural of "+noun+" is "+noun+"s")

print("2 + %d = 4"  %2)
print("2 + %d = %d"  %(2,  4))
print("%d + %d = %d" %(2, 2, 4))
print("%d + %d = %d" %(2, 2, 2+2))

print("%s" %3)
print("%d" %3.14)
print("%f" %3)
print("%s" %"Hi!")

msg = "Hi %s. How are you?"
name = "Hal"
print(msg%name)

import math
r = 5
print ("Radius: %d, Area: %.2f" % (r, 2*math.pi*r))

numLetter = input("write the name james:")
numletter = len(James)
James = [0:1]+numLetter[2:3]+numLetter[4:5]
print(numLetter)
print(James)
