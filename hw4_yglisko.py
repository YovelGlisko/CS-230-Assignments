"""
Class: CS230--Section 3
Name: Yovel Glisko
Description: Homework #4: Stock Pricing and Graphing. Data is read in from files and statistics are calculated. Data is plotted.
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

companies = open("companies.txt")
companiesText = companies.read()
companies.close()
companyList = companiesText.split("\n")
companyDict = {}
for x in companyList:
    temp = x.split(", ")
    companyDict[temp[0]] = temp[1]

def menu(dict):
    print("---- Welcome to Stock Pricing and Graphing ----\nAvailable Companies to Analyze:")
    boolean = False
    for x in dict:
        print("\t" + x)
    while boolean == False:
        user = input("Enter the name of a company: ")
        for x in dict:
            if user.lower()==x.lower():
                return x
            else:
                continue
        print("Company not found. Please try again.")

company = menu(companyDict)

import matplotlib.pyplot as plt
import pandas as pd
import statistics
import numpy as np
import math

dataCSV = pd.read_csv(companyDict.get(company))

def column(letter):
    if letter == "O":
        return "Open"
    elif letter == "H":
        return "High"
    elif letter == "L":
        return "Low"
    elif letter == "C":
        return "Close"
    elif letter == "V":
        return "Volume"

def stats(letter, data):
    col = column(letter)
    print("Descriptive Statistics for " + str(col))
    print("="*34)
    print(f"{'Count':30}{str(data[col].count()):15}")
    print(f"{'Mean':30}{str(data[col].mean()):15}")
    print(f"{'Min':30}{str(data[col].min()):15}")
    print(f"{'STD':30}{str(data[col].std()):15}")
    print(f"{'Max':30}{str(data[col].max()):15}")

def graph(data, type, letter):
    col = column(letter)
    if type == 1:
        print("1")
        data.plot(x = 'Date', y = col, kind = 'line', color = 'c')
    elif type == 2:
        print("2")
        data.plot(x = 'Date', y = col, kind = 'bar', color = 'c')
    plt.xlabel("Years: 2000 to Current Day")
    plt.ylabel("Price")
    plt.title(str(col) + " Stock Prices of " + str(company))
    plt.xticks(np.arange(0, data[col].count(), step=12), np.arange(2000, 2021, step=1))
    plt.show()

def scatter(data):
    plt.scatter(x = data['Date'], y = data["Open"], marker = '.', s = 20, color = 'g')
    plt.scatter(x = data['Date'], y = data["Close"], marker = '.', s = 20, color = 'r')
    plt.xlabel("Years: 2000 to Current Day")
    plt.ylabel("Price")
    plt.title("Open vs Close Stock Prices of " + str(company))
    plt.xticks(np.arange(0, data["Open"].count(), step=12), np.arange(2000, 2021, step=1))
    plt.show()

def histogram(data):
    plt.hist(x = data['Volume'], bins = range(0, int(data['Volume'].max()), int((int(data['Volume'].max()) - int(data['Volume'].min()))/4)), color = 'm')
    plt.ylabel("Volume")
    plt.title("Stock Volume of " + str(company))
    plt.show()

choice = input("\nEnter type of data to calculate (O for open, H for high, L for low, C for close, V for volume) or Q to quit: ").upper()
if choice == "Q":
    print("\t\tGraphing Type and Data Set\nGraph Selection:\n\t\t1 - Line\n\t\t2 - Bar\n")
    lineBar = int(input("Enter your choice: "))
    print("\nData selection:\n\t\tH - High\n\t\tL - Low\n\t\tO - Open\n\t\tC - Close\n\t\tV - Volume\n")
    dataSelect = input("Enter your choice: ").upper()
    graph(dataCSV, lineBar, dataSelect)
    scatter(dataCSV)
    histogram(dataCSV)
else:
    stats(choice, dataCSV)
