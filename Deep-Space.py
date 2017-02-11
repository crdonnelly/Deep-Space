from levels import tutorial

"""
Deep-Space video game
By Cameron Donnelly 12/02/2017

Game module:
This module is designed for the user to be able to access the main
menu, start or continue a game and gives the option to quit.

this module is also the launch for the rest of the game.
"""

def menu():
    print("Welcome to Deep-Space\n1. Login to access command record")
    print("2. Login as new captain")
    print("q. Quit simulation")
    end_game = False
    while end_game == False:
        login = str(input("Please select an option: "))
        if login == "1":
            print("This feature has not been implemented yet")
        elif login == "2":
            tutorial.tutorial()
            end_game = True
        elif login == 'q':
            end_game = True
        else:
            print("Please select a valid option...")

menu()
