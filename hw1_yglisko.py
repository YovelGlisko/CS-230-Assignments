"""
Class: CS230--Section 3
Name: Yovel Glisko
Date: January 30th, 2020
Description: Homework #1: Working with a Calendar. A birthdate and current date are taken and related info is printed.
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

#This segment simply prints out some simple lines and assigns user input to variables
print("Assignment #1: Calculations Using a Birthday\n")
name = input("Enter your full name: ")
birthday = input("Enter your birthday in the form mm/dd/yyyy: ")
today = input("Enter today's date in the form mm/dd/yyyy: ")
print("\nWelcome " + name)

#This segment takes the first two digits of the birthdate and uses it to calculate the quarter of birth.
quarter = round((int(birthday[:2]) + 1) / 3)
print("You were born in quarter " + str(quarter))

#This segment takes the week value from the birthdate and uses it to calculate the week of birth.
week = round((int(birthday[3:5]) + 3) / 7)
print("You were born in week " + str(week))

#This segment prints the birth month by taking the first two values from the user input.
#It then takes the day and month inputted and adds the current year to find the next birthday.
print("You were born in month " + birthday[:2])
print("Your next birthday will be on " + birthday[:6] + today[-4:])

#This segment calculates the year where the person will be 100 and uses it to find the number of years until then.
#This is done with the year from the current date inputted.
hundredYear = str(int(birthday[-4:]) + 100)
numYears = int(hundredYear) - int(today[-4:])
print(name + " will turn 100 in " + str(numYears) + " years in " + hundredYear)

#This segment creates a graph of asterisks based on the day inputted in the birthday.
print("\nGraph for each day of your birth month")
print("*" * int(birthday[3:5]))
