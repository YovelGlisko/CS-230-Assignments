"""
Class: CS230--Section 3
Name: Yovel Glisko
Description: Supplemental Exercises on Functions
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

#This exercise takes a string inputted by the user and reverses it using a function. It does this by telling the
#string to start at the end of the string and go back in steps of -1 which effectively reverses it
print("Exercise #1: ")
word = input("Enter a string to be reversed: ")
def reverse(str):
    output = str[len(str)::-1]
    return output
print("The reverse of that string is " + reverse(word))

#This exercise takes a list that was hardcoded and prints the list without any of the duplicate numbers
print("\nExercise #2: ")
def uniqueNums(list):
    a = []
    for x in list:
        if x not in a:
            a.append(x)
    return a

print(uniqueNums([1,1,2,2,3,4,5,6,5]))

#This exercise takes a string inputted by a user and counts the number of uppercase and lowercase letters. It then prints this.
print("\nExercise #3: ")
def upperLower(userString):
    upperCount = 0
    for x in range(0, len(userString)):
        if userString[x].isupper():
            upperCount +=1
    print(f"The number of Uppercase Letters is: {upperCount}")
    lowerCount = 0
    for x in range(0, len(userString)):
        if userString[x].islower():
            lowerCount +=1
    print(f"The number of Lowercase Letters is: {lowerCount}")


upperLower(input("Enter a string to have the letter cases counted: "))

