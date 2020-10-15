"""
Class: CS230--Section 3
Name: Yovel Glisko
Description: Supplemental Exercises on String Data Types
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

#This exercise takes the string orange and prints it in reverse with splicing.
#It does this by telling it to start at the end of the string and go to the beginning in steps of -1.
print("Exercise #1:")
reverse = "orange"
print(reverse[len(reverse)::-1])

#This exercise takes a user input string and counts the number of vowels. It does this by taking the count for
#the standard vowels AEIOU. If this count is at 0, 'y' becomes a vowel so the count is set to the count of 'y'.
print("Exercise #2:")
userString = input("Input a string: ")
vowel = userString.count('a') + userString.count('e') + userString.count('i') + userString.count('o') + userString.count('u')
if vowel == 0:
    vowel = userString.count('y')
print("The number of vowels is "+str(vowel))



#This exercise takes the string "Programming in Python" and prints out various related strings and numbers
print("Exercise #3:")
pip = "Programming in Python"
print('#1 Print the length of the string: ' + str(len(pip)))
print('#2 Print the position where "in" appears the first time is: ' + str(pip.index('in')))
print('#3 Print the number of times "n" appears is: ' + str(pip.count('n')))
print('#4 Print the number of spaces is: ' + str(pip.count(' ')))
print('#5 Print the substring "Pro": ' + pip[:3])
print('#6 Print the substring "thon": ' + pip[-4:])
print('#7 Print the substring "Programming in Py": ' + pip[:17])
print('#8 Split the string at the spaces: ' + str(pip.split()))
print('#9 Print the substring "a": ' + pip[5:6])
print('#10 Print the string in uppercase: ' + pip.upper())
print('#11 Print the string in lowercase: ' + pip.lower())
print('#12 Print the string but replace " in " with " with ": ' + pip[:12] + "with" + pip[-7:])


#This exercise takes a user inputted string and word and it finds the count of that word in the string.
print("Exercise #4:")
userSentence = input("Enter a string: ")
userWord = input("Enter a word to be counted from that string: ")
print(str(userSentence.count(userWord)))


#Takes a string six characters or higher and an inputted integer and it takes away the character at the location of the integer
print("Exercise #5:")
userInput = input("Enter a six character or higher string: ")
userIndex = int(input("Enter an index: "))
print("The original string is: " + userInput)
print("The new string is: " + userInput[:userIndex] + userInput[-userIndex+1:])

#Takes a string and replaces all of one user inputted character with a separate user inputted character.
print("Exercise #6:")
userInString = input("Enter a string with the same letter occurring twice or more: ")
userInChar = input("Enter a character to replace: ")
userReChar = input("Enter a character to replace it with: ")
print("The new string is: "+userInString.replace(userInChar,userReChar))

