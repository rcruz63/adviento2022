from adv2022.dia1.dia1_1 import main as dia1
from adv2022.dia2.dia2_1 import main as dia2_1
from adv2022.dia2.dia2_2 import main as dia2_2
from adv2022.dia3.dia3_1 import main as dia3_1
from adv2022.dia3.dia3_2 import main as dia3_2

def run():
    # Use a loop to keep representing a menu until the user chooses to exit
    while True:
        # Print the menu
        print("Welcome to the menu")
        print("1. Dia 1")
        print("2. Dia 2")
        print("3. Dia 3")
        print("4. Exit")
        # Ask the user for a choice
        choice = input("What would you like to do? ")
        # If the user chooses option 1, call option1()
        if choice == "1":
            dia1()
        # If the user chooses option 2, call option2()
        elif choice == "2":
            dia2_1()
            dia2_2()
        # If the user chooses option 3, call option3()
        elif choice == "3":
            dia3_1()
            dia3_2()
        # If the user chooses option 4, exit the program
        elif choice == "4":
            break
        # If the user chooses anything else, print an error
        else:
            print("That is not a valid option")
    