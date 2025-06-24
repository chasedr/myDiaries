import linecache
import random
import os

FileName = ".\English Word List.md"

os.system('cls')

linetext = linecache.getline('randomWord.settings', 1)
linetext = int(linetext)
wordcount = 0
if(linetext == 0):
    wordcount = input("input how many words do you want to generate:")
    wordcount = int(wordcount)
    print(wordcount)
else:
    wordcount = linetext

linecount = -1
for linecount, line in enumerate(open(FileName,'r', encoding='utf-8')):
    linecount+=1
print ("total lines:",linecount)

randomline=[0 for i in range(wordcount)]
for i in range(wordcount):
    randomline[i] = random.randint(1, linecount)
print("random line:",randomline)
print()
print("Now you can use these words to create your sentences.")
print()


for lineindex in randomline:
    linetext = linecache.getline(FileName, lineindex)
    print(linetext)