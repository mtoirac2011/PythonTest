from os import system

def welcomeMenu():
    system("cls")
    print("┌────────────────────────────────────────────────┐")
    print("│                                                │")
    print("│       Welcome to the Soccer Player View App    │")
    print("│                                                │")
    print("│       ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    │")
    print("│                                                │")
    print("│        This is the login menu. You will        │")
    print("│                                                │")
    print("│        need to type a valid email format       │")
    print("│                                                │")
    print("│           in order to access the App.          │")
    print("│                                                │")
    print("│        You will have 3 chances to log in.      │")
    print("│                                                │")
    print("│                   Good luck!                   │")
    print("└────────────────────────────────────────────────┘")
    input("     Press any key to continue...")
    
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
    print("│        x - Exit                                │")
    print("│                                                │")
    print("└────────────────────────────────────────────────┘")
    input("     Press any key to continue...")
    
def menuLiga():
    system("cls")
    print("┌────────────────────────────────────────────────┐")
    print("│                                                │")
    print("│           --  La Liga Menu --                  │")
    print("│                                                │")
    print("│        p - Positions table                     │")
    print("│                                                │")
    print("│        c - Teams with more corners             │")
    print("│                                                │")
    print("│        s - Teams with more shots               │")
    print("│                                                │")
    print("│        x - Exit                                │")
    print("└────────────────────────────────────────────────┘")
    input("")
    
def menuRM():
    system("cls")
    print("┌────────────────────────────────────────────────┐")
    print("│                                                │")
    print("│        --  Real Madrid Menu --                 │")
    print("│                                                │")
    print("│        p - List players                        │")
    print("│                                                │")
    print("│        b - Best soccer start leyend            │")
    print("│                                                │")
    print("│        o - Best soccer start leyend (by Name)  │")
    print("│                                                │")
    print("│        q - List soccer quotes                  │")
    print("│                                                │")
    print("│        x - Exit                                │")
    print("└────────────────────────────────────────────────┘")
    input("")