"""
Class: CS230--Section 3
Name: Yovel Glisko
Description: Supplemental Exercises on Control Structures
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

#This exercise prints the first 10 odd numbers and the first 5 multiples of 10 through for loops.
print("Exercise #1:")
for x in range(1, 11):
    print("Odd number #" + str(x) + ": " + str(x * 2 - 1))
for y in range(1, 6):
    print("Multiple of 10 #" + str(y) + ": " + str(y * 10))

#This exercise takes a user input of a number and prints that number of stars and one less every line.
numStars = int(input("\nExercise #2: \nEnter an positive whole number to make an upside down triangle of *'s: "))
while numStars > 0:
    print("*" * numStars)
    numStars -= 1

#This exercise takes a user input of an animal name from a list and uses if statements to print the sound the animal makes.
animal = input("\nExercise #3: \nEnter one of the THREE following animals: dog, cat, pig, cow: ")
if animal.lower() == "dog":
    print("woof")
elif animal.lower() == "cat":
    print("meow")
elif animal.lower() == "pig":
    print("oink")
elif animal.lower() == "cow":
    print("moo")

#This exercise takes a user integer and checks if that number mod 2 is 0 to find it if is even. If it is not it is odd.
userNum = int(input("\nExercise #4: \nEnter an integer to be determined as even or odd: "))
if userNum % 2 == 0:
    print("Even")
else:
    print("Odd")

#This exercise uses a nested for loop to print consecutive lines adding more numbers from 1 to 5 until the last one reads 12345.
print("\nExercise #6: ")
for a in range(1, 6):
    line = ""
    for b in range (1, a+1):
        line = line + str(b)
    print(line)
