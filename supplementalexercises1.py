"""
Class: CS230--Section 3
Name: Yovel Glisko
Description: Supplemental Exercises on Numeric Data Types
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

#This exercise takes the input of one letter, turns it into a number with ord,
# adds one, and turns it back into a character with chr. It then prints the character.
letter = chr(ord(input("Exercise #1: Enter one letter from a to y: ")) + 1)
print(letter)

#This exercise takes the inputs of an hourly wage and overtime hours as floats.
#It then takes these and find the total pay. It rounds this to two decimal points and prints the result.
wage = float(input("Exercise #2: Enter the hourly wage: "))
overtime = float(input("Enter the number of overtime hours: "))
pay = round(wage * 40 + overtime * wage * 1.5,2)
print("The employee's weekly pay is $" + str(pay) + ".")

#This exercise takes the inputs of width and length as floats. It then multiplies
#each by 2 and adds it to make the perimeter. It rounds this and then prints the result.
width = float(input("Exercise #3: Enter the width of the field: "))
length = float(input("Enter the length of the field: "))
perimeter = round(width * 2 + length * 2)
print("The perimeter of the field is " + str(perimeter) + " feet")

#This exercise takes the input for the number of people at a party as an integer.
#It divides 32 by this number, takes the decimal portion, and uses that portion to find the remaining slices.
#It prints a rounded version of 32 divided by the number as well as the remainder and a non-rounded value.
party = int(input("Exercise #4: Enter a whole number for the number of people at the party: "))
leftovers = round((float(32 / party) - int(32 / party)) * party)
print(str(round(32 / party)) + " slices each " + str(leftovers) + " left over")
print(str(32 / party) + " slices each")

