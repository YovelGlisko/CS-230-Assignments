"""
Class: CS230--Section 3
Name: Yovel Glisko
Description: Homework #2: Laptop Configurator. A customer makes an order.
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""
print("Welcome to LaptopConfig.Com")
price = 0

model = input("\nWhich model do you want?"
              "\n\tA - Low-End"
              "\n\tB - Productivity"
              "\n\tC - UltraThin"
              "\n\t Enter your choice: ")
if model == 'a' or model == 'A':
    modelChange = 599.99
    modelName = "Low-End Laptop"
elif model == 'b' or model == 'B':
    modelChange = 699.99
    modelName = "Productivity Laptop"
elif model == 'c' or model == 'C':
    modelChange = 899.99
    modelName = "UltraThin Laptop"
else:
    print("You entered an incorrect value. The program will end.")
    quit()

os = input("\nWhich operating system?"
              "\n\tA - None (subtract $50)"
              "\n\tB - Windows (included)"
              "\n\tC - Enterprise (add $120)"
              "\n\t Enter your choice: ")
if os == 'a' or os == 'A':
    osChange = -50
    osName = "None"
elif os == 'b' or os == 'B':
    osChange = 0
    osName = "Windows 10"
elif os == 'c' or os == 'C':
    osChange = 120
    osName = "Windows Enterprise"
else:
    print("You entered an incorrect value. The program will end.")
    quit()

storage = input("\nWhich storage option?"
              "\n\tA - 128 GB SSD (subtract $50)"
              "\n\tB - 256 GB SSD (standard)"
              "\n\tC - 512 GB SSD (add $100)"
              "\n\t Enter your choice: ")
if storage == 'a' or storage == 'A':
    storageChange = -50
    storageName = "128 GB SSD"
elif storage == 'b' or storage == 'B':
    storageChange = 0
    storageName = "256 GB SSD"
elif storage == 'c' or storage == 'C':
    storageChange = 100
    storageName = "512 GB SSD"
else:
    print("You entered an incorrect value. The program will end.")
    quit()

processor = input("\nWhich processor?"
              "\n\tA - Core I3 (subtract $60)"
              "\n\tB - Core I5 (standard)"
              "\n\tC - Core I7 (add $120)"
              "\n\t Enter your choice: ")
if processor == 'a' or processor == 'A':
    processorChange = -60
    processorName = "Core I3"
elif processor == 'b' or processor == 'B':
    processorChange = 0
    processorName = "Core I5"
elif processor == 'c' or processor == 'C':
    processorChange = 120
    processorName = "Core I7"
else:
    print("You entered an incorrect value. The program will end.")
    quit()

ram = input("\nHow much RAM?"
              "\n\tA - 8 GB RAM (subtract $30)"
              "\n\tB - 16 GB RAM (included)"
              "\n\tC - 32 GB RAM (add $72)"
              "\n\t Enter your choice: ")
if storage == 'a' or storage == 'A':
    ramChange = -30
    ramName = "8 GB RAM"
elif storage == 'b' or storage == 'B':
    ramChange = 0
    ramName = "16 GB RAM"
elif storage == 'c' or storage == 'C':
    ramChange = 72
    ramName = "32 GB RAM"
else:
    print("You entered an incorrect value. The program will end.")
    quit()

total = modelChange+osChange+processorChange+storageChange+ramChange
tab="\t"
print('*'*51)
print(f'{"Your Order from LaptopConfig.Com":^51}')
print(f'{"Laptop Model:":<17}{tab+modelName+tab:^17}${modelChange:>,.2f}')
print(f'{"Operating System:":<17}{tab+osName+tab:^17}${osChange:>,.2f}')
print(f'{"Processor:":<17}{tab+processorName+tab+tab:^17}${processorChange:>,.2f}')
print(f'{"Storage:":<17}{tab+storageName+tab:^17}${storageChange:>,.2f}')
print(f'{"RAM:":<17}{tab+ramName+tab:^17}${ramChange:>,.2f}')
print('='*51)
print(f'{"Total Price: ":<25}{tab:>15}${total:,.2f}')


