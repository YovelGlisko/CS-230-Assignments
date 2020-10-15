"""
Class: CS230--Section 3
Name: Yovel Glisko
Description: Homework #3: Mortgage Calculations. A mortgage report is generated.
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

import math
print("{:^50}".format("---------- Mortgage Report ----------"))

price = float(input("Enter house purchase price: "))
downPayment = float(input("Enter down payment: "))
if downPayment > price:
    checkDP = 1
    while checkDP == 1:
        downPayment = float(input("Enter a down payment less than the house purchase price: "))
        if downPayment <= price:
            checkDP = 0
interest = float(input("Enter interest rate (without the % sign): "))
if interest < 0:
    checkIR = 1
    while checkIR == 1:
        interest = float(input("Enter a positive number for the interest rate (without the % sign): "))
        if interest >= 0:
            checkIR = 0
term = float(input("Enter term of mortgage in years: "))
tax = float(input("Enter tax rate on home (without the % sign): "))
insurance = float(input("Enter home insurance (per year): "))

months = term * 12
loanAmount = price - downPayment
principalInterest = (loanAmount * (interest / 1200))/(1 - (1 / (math.pow((1 + (interest / 1200)), (months)))))
monthlyTax = (((tax / 100) + 1) * price) / 1200
monthlyInsurance = insurance / 12
totalMonth = principalInterest + monthlyTax + monthlyInsurance


print("{:^50}".format("---------- Loan Summary ----------"))
print("{0:<25}${1:^,.2f}".format("House Purchase Price: ", price))
print("{0:<25}${1:^,.2f}{2:>3}".format("Down Payment: ", downPayment, "(" + str(round(100 * (downPayment / price))) + "% of purchase price)"))
print("{0:<25}${1:^,.2f}".format("Loan Amount: ", loanAmount))
print("{0:<25}{1:^20}".format("Loan Term: ", str(term) + " years (" + str(term * 12) + " months)"))
print("{0:<25}{1:^7}".format("Interest Rate: ", str(interest) + "%"))
print("{0:<25}{1:^8}".format("Tax Rate: ", str(tax) + "%/year"))
print("{0:<25}{1:^10}".format("Home Insurance: ", "$" + str(insurance) + "/year"))

print("{:^50}".format("---------- Monthly Payment Breakdown ----------"))
print("{0:<25}${1:^,.2f}{2:>1}".format("Principal and Interest: ", principalInterest, "/month"))
print("{0:<25}${1:^,.2f}{2:>1}".format("Monthly Tax: ", monthlyTax, "/month"))
print("{0:<25}${1:^,.2f}{2:>1}".format("Monthly Insurance: ", monthlyInsurance, "/month"))
print("{0:<25}${1:^,.2f}{2:>1}".format("Total: ", totalMonth, "/month"))

principalInterestTotal = principalInterest * term * 12
print("{:^50}".format("---------- Monthly Payment Breakdown ----------"))
print("{:}${:,.2f}".format("By the end of the " + str(term) + "-year period, you would pay ", (principalInterestTotal)))
print("{:}${:,.2f}{}".format("in total payments (", loanAmount, " would be for the original loan"))
print("{:}${:,.2f}{}".format("amount and ", (principalInterestTotal - loanAmount), " in interest)."))


totalInterest = 0
totalPrincipal = 0
grandTotalPrincipal = 0
currentPrincipal = loanAmount
count = 0
choice = input("Do you want a Detailed Payment Schedule or a Summary Payment Schedule (D or S): ")
if choice == 'D' or choice == 'd':
    print('Year'.rjust(10), ' ', 'Month'.ljust(10), ' ', 'Principal & Interest'.ljust(10), ' ', 'Principal'.ljust(10), ' ', 'Interest'.ljust(10), ' ', 'Principal Remaining'.ljust(10), 'Total Interest'.ljust(10), ' ')
    for x in range(0, term):
        for y in range (0, 12):
            monthlyInterest = (interest / 1200) * currentPrincipal
            monthlyPrincipal = principalInterest - monthlyInterest
            currentPrincipal -= monthlyPrincipal
            totalInterest += monthlyInterest
            count += 1
            print("{:8}{:8}${:20,.2f}${:18,.2f}${:13,.2f}${:16,.2f}${:18,.2f}".format((x + 1), count, principalInterest, monthlyPrincipal, monthlyInterest, currentPrincipal, totalInterest))
else:
    print("{:^50}".format("---------- Summary Payment Schedule ----------"))
    print("{:<20}{:^20}{:>20}".format("Year", "Total Principal", "Total Interest"))
    for a in range (0, term):
        for b in range (0, 12):
            monthlyInterest = (interest / 1200) * currentPrincipal
            monthlyPrincipal = principalInterest - monthlyInterest
            currentPrincipal -= monthlyPrincipal
            totalInterest += monthlyInterest
            totalPrincipal += monthlyPrincipal
        print("{:<20}${:^20,.2f}${:>15,.2f}".format((a + 1), totalPrincipal, totalInterest))
        grandTotalPrincipal += totalPrincipal
        totalPrincipal = 0
    print("{:<20}${:^20,.2f}${:>15,.2f}".format("Grand Totals: ", grandTotalPrincipal, totalInterest))



