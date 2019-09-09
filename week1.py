#SWDV-660 – Applied DevOps
#Maryville University, 2019
#Week 1 Assignment:
#      Package Managed Projects
#week1.py
#Henrik Olsen (0913075)

#Run in command prompt or PowerShell - colorama NOT supported in Thonny


from random import randrange
from colorama import init, Fore, Back
from prettytable import PrettyTable


def printPrettyTable(rolls):
    table = PrettyTable()
    table.field_names = ["Roll", "Times", "Percentage"]
    table.align["Roll"] = "l"
    table.align["Times"] = "c"
    table.align["Percentage"] = "r"
    table.add_row([Fore.BLUE + "One", rolls[1], "{0:0.2f} %".format((rolls[1] / rolls[0]) * 100)])
    table.add_row([Fore.BLUE + "Two", rolls[2], "{0:0.2f} %".format((rolls[2] / rolls[0]) * 100)])
    table.add_row([Fore.BLUE + "Three", rolls[3], "{0:0.2f} %".format((rolls[3] / rolls[0]) * 100)])
    table.add_row([Fore.BLUE + "Four", rolls[4], "{0:0.2f} %".format((rolls[4] / rolls[0]) * 100)])
    table.add_row([Fore.BLUE + "Five", rolls[5], "{0:0.2f} %".format((rolls[5] / rolls[0]) * 100)])
    table.add_row([Fore.BLUE + "Six", rolls[6], "{0:0.2f} %".format((rolls[6] / rolls[0]) * 100)])
    print("A 6-sided die was rolled {0} times, here's the result: ".format(rolls[0]))
    print(Back.WHITE + Fore.BLACK + "")
    print(table)


def main():
    init()
    table = [0, 0, 0, 0, 0, 0, 0]
    one = two = three = four = five = six = 0
    answer = input("How many times do you wish to roll the die? ")
    if answer.isdigit():
        table[0] = int(answer)
        for loop in range(table[0]):
            table[randrange(6) + 1] += 1
        printPrettyTable(table)
    else:
        print("Invalid input! '{0}' is not a whole number...".format(answer))
    print(Back.BLACK + Fore.WHITE + "Press enter to exit!")
    input()


main()
