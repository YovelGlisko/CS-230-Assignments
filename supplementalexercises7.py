"""
Class: CS230--Section 3
Name: Yovel Glisko
Description: Supplemental Exercises on Files
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

#This exercise takes user input for a file name and counts the words in the file by creating a list containing every word.
print("\nExercise #1: ")
fileName = input("Enter a file name to count the words for: ")
file = open(fileName, "r")
fileText = file.read()
textList = fileText.split(" ")
file.close()
print("The number of words in the file is " + str(len(textList)))


#This exercise takes the file Alice.txt and splits it into a list with every word. It goes through each word and whichever ones are five letters long are added to a new file called fiveletters.txt
print("\nExercise #2: ")

alice = open("Alice.txt")
aliceText = alice.read()
alice.close()
aliceList = aliceText.split(" ")
fiveLetter = open("fiveletters.txt", "w")
for x in aliceList:
    if len(x) == 5:
        fiveLetter.write(x)
        fiveLetter.write(" ")
print("File fiveletters.txt created and filled!")

#This exercise takes in a user input file and puts it in a string where each character is checked if it is a number. A system using a variable named count is used to split each number with a space when it is all printed.
print("\nExercise #3: ")
inputName = input("Enter a file name to find all the numbers in: ")
fileNumbers = open(inputName, "r")
fileText = fileNumbers.read()
fileNumbers.close()
allNums = ""
count = 1
for a in fileText:
    if a.isnumeric():
        if count == 0:
            allNums = allNums + " " + str(a)
            count = 1
        else:
            allNums = allNums + str(a)
    else:
        count = 0
print(allNums)


#This exercise compares two files by using a function which compares each line with a for loop that breaks at the different line. The function assumes the first list is the longer one and this is done by calling the function in the correct order with an if statement.
print("\nExercise #4: ")
inputOne = input("Enter the first file name: ")
inputTwo = input("Enter the second file name: ")
fileOne = open(inputOne, "r")
fileOneText = fileOne.read()
fileOneList = fileOneText.split("\n")
fileOne.close()
fileTwo = open(inputTwo, "r")
fileTwoText = fileTwo.read()
fileTwoList = fileTwoText.split("\n")
fileTwo.close()
def compare(listOne, listTwo):
    lineNum = 0
    for x in range(0, len(listOne)-1):
        if x > len(listTwo):
            lineNum = x+1
            break
        elif listOne[x] == listTwo[x]:
            continue
        else:
            lineNum = x+1
            break
    return lineNum
if len(fileOneList) >= len(fileTwoList):
    lineNum = compare(fileOneList, fileTwoList)
else:
    lineNum = compare(fileTwoList, fileOneList)
if lineNum == 0:
    print("The two files are identical")
else:
    lineNum -=1
    print("The different line is at index " + str(lineNum))
    print("The first line is: ")
    print(fileOneList[lineNum])
    print("The second line is: ")
    print(fileTwoList[lineNum])

