"""
Class: CS230--Section 3
Name: Yovel Glisko
Description: Supplemental Exercises on Dictionaries
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

#This exercise takes a user input string and turns it into a dictionary of lists which stores all the words by the starting letter and then prints it all
print("\nExercise #1: ")
from collections import defaultdict
string = input("Enter a string: ")
array = string.split(" ")
dictionary = defaultdict(list)
for word in array:
    dictionary[word[0]].append(word)
for x, y in dictionary.items():
    print(x, y)

#This exercises does essentially the same thing as Exercise #1, creating a dictionary of lists storing all the names with the corresponding age before printing it all
print("\nExercise #2: ")
names = ["Alice", "Bob", "Cathy", "Dan", "Ed", "Frank", "Gary", "Helen", "Irene", "Jack", "Kelly", "Larry"]
ages = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]
from collections import defaultdict
ageDict = defaultdict(list)
for x in range(0, len(names)):
    ageDict[ages[x]].append(names[x])
for x, y in ageDict.items():
    print(x, y)

#This exercise creates a list of senator names and sorts it to find the alphabetical order of the names and to find the longest name.
print("\nExercise #3: ")
senators = { "Alabama" : ["Shelby", "Jones"], "Alaska" : ["Murkowski", "Sullivan"], "Arizona": ["Sinema", "McSally"],"Arkansas": ["Boozman","CottonCotton"], "California": ["Feinstein","HarrisHarris"]}
senList = list()
for x in senators:
        for y in senators[x]:
            senList.append(y)
alphabeticalSens = sorted(senList)
print("In alphabetical order the senators' names are: ")
print(alphabeticalSens)
maxSens = sorted(senList, key=len)
print("The longest name of a senator is: " + maxSens[-1])

#This exercise sorts the dictionary from lowest to highest and reverses it to print it from highest to lowest.
print("\nExercise #4)")
scores = {'Math':81, 'Physics':83, 'Chemistry':87}
scores = sorted((value, key) for (key, value) in scores.items())
scores.reverse()
for x, y in scores:
    print(y, x)
