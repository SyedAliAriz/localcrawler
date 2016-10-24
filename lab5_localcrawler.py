import os
import sys
import ntpath

#for path of txt files
from os.path import join


#to save the names of .txt files
Files = {}

#Var to store number of files
count = 0

#hashtable for saving words
wordDict = {}
wordCount = 0

#Setting Root Path for search of .txt files
myPath = '/Users/ali/desktop/5th semester/'#use your own computers path here

#Indexing the Files
for root, dirs, files in os.walk(myPath):
    for file in files:
        if file.endswith(".txt"):#Checking for .txt files only
            count = count + 1#increasing file count
            #inserting files into the file dictionary
            Files[str(count)] = join(root, file.title())



#Indexing the words
for x in range(1,count+1,1):
    #opening the files saved in file dict to save words in a separate word dict
    with open(Files[str(x)],"r") as f:
        for line in f:
            for word in line.split():#splits lines into words
                wordCount = wordCount + 1#increasing word count
                if word in wordDict.keys():
                        #print just for checking purpose of code
                        print("duplicate word found")
                        wordDict[word] = wordDict[word] + "," + str(x)
                else:
                    wordDict[word] = str(x)
                    #print just for checking purpose of code
                    print("new word found")


print ("\n"+"Files Found: " + str(count)+ "\n")
print ("Word Count: " + str(wordCount) + "\n")

#Infinite Search Loop
while(1):
    sTerm = str(raw_input("Enter term:"))
    sTerm=sTerm.lower()
    result = ""

    #Check for filenames
    for x in range(1, count + 1, 1):

        loc, fname = os.path.split(Files[str(x)])

        if sTerm.lower() in [f.lower() for f in fname.split(".")]:
            print ("Filename found: " + Files[str(x)] + "\n")

    if sTerm in wordDict.keys():
        result = wordDict[sTerm]
        result = result.split(",")
        tmp = ""

        for r in result:

            #To Avoid Repitition
            if tmp != r:
                print("Found In " + Files[str(r)] + "\n")
            tmp = r
    else:
        print("Search Term Not Found In File Contents!" + "\n")

