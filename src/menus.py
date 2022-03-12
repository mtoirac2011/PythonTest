from os import system

def welcomeMenu():
    system("cls")
    print("┌────────────────────────────────────────────────┐")
    print("│                                                │")
    print("│       Welcome to the Spain Soccer League       │")
    print("│                                                │")
    print("│       ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    │")
    print("│                                                │")
    print("│        This is the welcome menu. In this app   │")
    print("│                                                │")
    print("│        you will find data for Spain soccer     │")
    print("│                                                │")
    print("│        and Real Madrid soccer team as well.    │")
    print("│                                                │")
    print("│                                                │")
    print("│                   Good luck!                   │")
    print("└────────────────────────────────────────────────┘")
    
def mainMenu():
    system("cls")
    print("┌────────────────────────────────────────────────┐")
    print("│                                                │")
    print("│       La Liga (The Spain Soccer Teams)         │")
    print("│                                                │")
    print("│      ─────────────────────────────────         │")
    print("│                                                │")
    print("│        l - La Liga Menu                        │")
    print("│                                                │")
    print("│        r - Real Madrid Menu                    │")
    print("│                                                │")
    print("│        c - Convert Menu                        │")
    print("│                                                │")
    print("│        x - Exit                                │")
    print("│                                                │")
    print("└────────────────────────────────────────────────┘")
    print("")
    
def menuLiga():
    system("cls")
    print("┌────────────────────────────────────────────────┐")
    print("│                                                │")
    print("│           --  La Liga Menu --                  │")
    print("│                                                │")
    print("│        p - Positions table                     │")
    print("│                                                │")
    print("│        s - Teams with more shots               │")
    print("│                                                │")
    print("│        x - Exit                                │")
    print("└────────────────────────────────────────────────┘")
    print("")
    
def menuRM():
    system("cls")
    print("┌────────────────────────────────────────────────┐")
    print("│                                                │")
    print("│        --  Real Madrid Menu --                 │")
    print("│                                                │")
    print("│        p - List of players                     │")
    print("│                                                │")
    print("│        o - Oldest players                      │")
    print("│                                                │")
    print("│        n - Players by nation                   │")
    print("│                                                │")
    print("│        x - Exit                                │")
    print("└────────────────────────────────────────────────┘")
    print("")
    
def menuGoodBye():
    system("cls")
    print("┌────────────────────────────────────────────────┐")
    print("│                                                │")
    print("│                                                │")
    print("│              Good bye...!                      │")
    print("│                                                │")
    print("│                                                │")
    print("└────────────────────────────────────────────────┘")
    print("")
    
def positionsTableHeader():
    system("cls")
    print("                  Spain League Teams")
    print("┌─────────────────────────────────────────────────────┐")
    print("│Position Team            Matches Wins Draws Loses Pts│")
    print("└─────────────────────────────────────────────────────┘")    

def moreShotsHeader():
    system("cls")
    print("Teams with more shots")
    print("┌─────────────────────┐")
    print("│Team            Shots│")
    print("└─────────────────────┘")    

def listPlayersHeader():
    system("cls")
    print("     Real Madrid players")
    print("┌────────────────────────────┐")
    print("│Player            Nation Age│")
    print("└────────────────────────────┘")    

def sortByAgeHeader():
    system("cls")
    print("    Oldest players")
    print("┌─────────────────────┐")
    print("│Player            Age│")
    print("└─────────────────────┘")    

def groupNationHeader():
    system("cls")
    print("Group by nations")
    print("┌───────────────┐")
    print("│Nation    Count│")
    print("└───────────────┘")    

def convertMenu():
    system("cls")
    print("┌────────────────────────────────────────────────┐")
    print("│              From a number to type,            │")
    print("│        the converter will show you the         │")
    print("│            corresponding values:               │")
    print("│                                                │")
    print("│            * Fahrenheit to celsius             │")
    print("│            * Miles to kilometers               │")
    print("│            * Feet to meters                    │")
    print("│            * Meters to centimeters             │")
    print("│                                                │")
    print("│                                   X to Exit    │")
    print("└────────────────────────────────────────────────┘")
    
def doConvertPrintHeader():
    system("cls")
    print(" These are the convertions for your number")
    print("───────────────────────────────────────────")
    print("")