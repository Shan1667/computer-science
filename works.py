counts = {}
counts2 = dict({})
print(counts)
print(counts2)

menu = input("please enter frequency to see how many words come up or enter characters to see how many characters come up:")
if "frequency" in menu:
    sentence = input("please enter a sentence:")

elif "characters" in menu:
    print("HI")

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


