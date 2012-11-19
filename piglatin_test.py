import os

word = raw_input("Word = ")
str(word)
print word
end = ""
end = word[0]
if word[0] == "a":
	newword = word + "way"
if word[0] == "e":
	newword = word + "way"
if word[0] == "i":
	newword = word + "way"
if word[0] == "o":
	newword = word + "way"
if word[0] == "u":
	newword = word + "way"
else:
        newword = word[1 : len(word)] + "ay"
print newword
os.system('pause')