"""
Class: CS230--Section 3
Name: Yovel Glisko
Description: Supplemental Exercises on Control Structures Exercise #5
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

#This exercise takes user input to start a game, print, or quit. The game counts the number of times the user says "duck"
#before they say "goose" which ends the game.
print("Exercise #5: ")
go = True
while go:
    choice = eval(input("""
    1 - Duck Duck Goose,
    2 - Option 2, 
    3 - Option 3, 
    4 - Quit
    Enter choice: """))
    if choice == 1:
            print ("You chose option 1 which is Duck Duck Goose.")
            play = True
            count = 0
            while play:
                userInput = input("Enter duck or goose: ")
                if userInput.lower() == "duck":
                    count += 1
                elif userInput.lower() == "goose":
                    print("The number of times you entered duck before goose is " + str(count))
                    play = False
                else:
                    print("That is not a valid option. Try again")

    elif choice == 2:
            print ("You chose option 2.")
    elif choice == 3:
            print ("You chose option 3.")
    elif choice == 4:
            print ("You chose option 4 which is to quit.")
            go = False
    else:
            print ("Error. Enter 1, 2, or 3.")
