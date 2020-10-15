"""
Class: CS230--Section 3
Name: Yovel Glisko
Description: Supplemental Exercises on Lists
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

#This exercise continues to take positive numbers which it adds to a list that is averaged when a negative number is inputted
print("Exercise #1: ")
go = 1
list = []
while go == 1:
    num = float(input("Enter a positive number to add or a negative number to end: "))
    if num >= 0:
        list.append(num)
    else:
        go = 0
avg = sum(list) / len(list)
print(f"The average of this list is {avg}")

#This exercise gets the user to keep adding numbers to a list before printing out the highest value from the list
print("\nExercise #2: ")
length = int(input("Enter the number of elements for the list: "))
maxList = []
for x in range(0, length):
    maxList.append(float(input("Enter a number for the list: ")))
print("The highest number in this list is " + str(max(maxList)))

#This exercise prints the difference for each set of values from the hardcoded lists and it squares and sums each of these.
print("\nExercise #3: ")
listOne = [1, 8, 13, 18, 25]
listTwo = [4, 2, 8, 1, 4]
difSq = 0
for x in range(0, len(listOne)):
    print(f"The difference between {listOne[x]} and {listTwo[x]} is {listOne[x]-listTwo[x]}")
    difSq += (listOne[x]-listTwo[x])**2
print(f"The sum of all of the differences of squares is {difSq}")


#This exercise gets the user to play a game where they have to guess 7 items in a row from a list with less than 3 errors.
#It does this with some if statements and a while loop to run the game as needed
print("\nExercise #4: ")
gameNum = int(input("Enter 1 to select question 1 or 2 to select question 2: "))
if gameNum == 1:
    list = ["sneezy", "doc", "dopey", "bashful", "sleepy", "grumpy", "happy"]
else:
    list = ["red", 'orange', "yellow", "green", "blue", "indigo", "violet"]
game = 1
score = 0
strikes = 3
while game == 1:
    num = input("Enter element number " + str(score + 1) + ": ")
    if num == list[score]:
        score += 1
        if score == 7:
            print("You win!")
            game = 0
    else:
        strikes -= 1
        if strikes == 0:
            print("You lose with a score of " + str(score))
            print("The remaining answers were ")
            print(list[((score + 1) * -1):])
            game = 0


#This exercise takes numbers given by a user and calculates the letter grades on a curved system by making an integer list
print("\nExercise #5: ")
strList = input("Enter multiple integers separated by spaces: ").split()
intList = []
for n in range(0, len(strList)):
    intList.append(int(strList[n]))
best = max(intList)
for m in range(0, len(intList)):
    if intList[m] >= best - 10:
        print(f"Student {m} score is {intList[m]} and grade is A")
    elif intList[m] >= best - 20:
        print(f"Student {m} score is {intList[m]} and grade is B")
    elif intList[m] >= best - 30:
        print(f"Student {m} score is {intList[m]} and grade is C")
    elif intList[m] >= best - 40:
        print(f"Student {m} score is {intList[m]} and grade is D")






