"""
Class: CS230--Section 3
Name: Yovel Glisko
Description: Homework #5: Starbucks Store Finder. A store finder app for Starbucks locations.
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""
import pandas as pd

FILTERS = ('Number', 'Name', 'Street Address', 'City', 'State', 'Zip','Latitude','Longitude','Features-Stations')
ZIP_SIZE_ONE = 3
ZIP_SIZE_TWO = 5
ZIP_SIZE_THREE = 10

def getData():
    dataCSV = pd.read_csv("All_Starbucks_Locations_in_the_US.csv").filter(FILTERS)
    return dataCSV

def displayStores(dfStores):
    for x in dfStores.index:
        print("\nName/Location\n"
              + str(dfStores["Name"][x]) + "\n"
              + str(dfStores["Street Address"][x]) + "\n"
              + str(dfStores["City"][x]) + ", " + str(dfStores["State"][x]) + " " + str(dfStores["Zip"][x]))

def findStoresByCityState(dfStores):
    print("\n===== City and State Finder =====")
    city = input("Enter a city: (enter to stop) ")
    state = input("Enter a state abbreviation: ").upper()
    data = getData()
    for x in dfStores.index:
        if dfStores["City"][x] != city:
            dfStores = dfStores.drop(x, axis=0)
    for y in dfStores.index:
        if dfStores["State"][y] != state:
            dfStores = dfStores.drop(y, axis=0)
    print("\nStarbucks Locations by City and State\n")
    num = len(dfStores.index)
    if num == 1:
        print("There is 1 location satisfying this criteria")
    else:
        print("There are " + str(num) + " locations satisfying this criteria")
    displayStores(dfStores)

def findStoresByZip(dfStores):
    print("\n===== Zip Code Finder =====")
    zipCode = input("Enter a zip code: (enter to stop) ")
    dfStores = zipStoreFinderHelp(dfStores, zipCode)
    print("\nStarbucks Locations by ZIP Code\n")
    num = len(dfStores.index)
    if num == 1:
        print("There is 1 location satisfying this criteria")
    else:
        print("There are " + str(num) + " locations satisfying this criteria")
    displayStores(dfStores)

def zipStoreFinderHelp(dfStores, zip):
    if len(zip) == ZIP_SIZE_ONE:
        for x in dfStores.index:
            if str(dfStores["Zip"][x])[0:3] != zip:
                dfStores = dfStores.drop(x, axis=0)
    elif len(zip) == ZIP_SIZE_TWO:
        for x in dfStores.index:
            if str(dfStores["Zip"][x])[0:5] != zip:
                dfStores = dfStores.drop(x, axis=0)
    elif len(zip) == ZIP_SIZE_THREE:
        for x in dfStores.index:
            if str(dfStores["Zip"][x]) != zip:
                dfStores = dfStores.drop(x, axis=0)
    return dfStores

def findStoresbyDriveThru(dfStores):
    print("\n===== Zip Code with Drive-Through Finder =====")
    zipCode = input("Enter a zip code: (enter to stop) ")
    dfStores = zipStoreFinderHelp(dfStores, zipCode)
    for x in dfStores.index:
        if "Drive-Through" not in str(dfStores["Features-Stations"][x]):
            dfStores = dfStores.drop(x, axis=0)
    print("\nStarbucks Locations by ZIP Code with Drive-Through\n")
    num = len(dfStores.index)
    if num == 1:
        print("There is 1 location satisfying this criteria")
    else:
        print("There are " + str(num) + " locations satisfying this criteria")
    displayStores(dfStores)

def main():
    print("*** Starbucks Store Finder ***\n\n"
          "\t1 - Find Stores by City and State\n"
          "\t2 - Find Stores by Zip Code\n"
          "\t3 - Find Stores by Zip Code and with Drive-Through\n"
          "\t4 - Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        findStoresByCityState(getData())
    elif choice == 2:
        findStoresByZip(getData())
    elif choice == 3:
        findStoresbyDriveThru(getData())
    elif choice == 4:
        quit()

if __name__=="__main__":
    main()
