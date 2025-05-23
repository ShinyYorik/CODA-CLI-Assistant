import os
import time
import webbrowser
import random
from datetime import datetime

def Notepad():
    os.system("notepad")
    print("I opened your notebook!")
    Main_Menu()

def Calculator():
    os.system("calc")
    print("I opened your calculator!")
    Main_Menu()

def Reminders():
    reminder = input("Enter reminder text: ")
    time = input("When to remind (MONTH.DAY.YEAR HOUR:MINUTES): ")
    with open('reminders.txt', 'a') as f:
        f.write(f"{time}|{reminder}\n")
    print(f"The reminder '{reminder}' was created for a time {time}")
    Main_Menu()

def Text_Tools():
    print("Working with text")
    text = input("Enter the text: ")
    print("1. Upper case:", text.upper())
    print("2. Lower case:", text.lower())
    print("3. Text length:", len(text), "символов")
    print("4. Word count:", len(text.split()))
    Main_Menu()

def Web_Search():
    print("What to find on the Internet?")
    user_request = input(">>> ")
    webbrowser.open(f"https://www.google.com/search?q={user_request}")
    print("Opening search results...")
    Main_Menu()

def Guess_Number():
    number = random.randint(0, 100)
    print("I thought of a number between 0 and 100, can you guess it?")
    user_guess = int(input(">>> "))
    if number == user_guess:
        print("You won! Congratulations!")
        Main_Menu()
    elif number != user_guess:
        print("Sorry, but you lost, try next time.")
        Main_Menu()
    else:
        print("An error occurred! You may have entered something incorrectly. Returning to the menu")
        Main_Menu

def Rock_Papper_Scissors():
    items = ["rock", "scissors", "papper"]
    chosen_item = random.choice(items)
    print("Choose: rock, scissors или papper")
    user_item = str(input(">>> "))
    if chosen_item == user_item:
        print("Tie!")
        Main_Menu()
        
    elif chosen_item == "rock" and user_item == "scissors":
        print("I chose " + chosen_item)
        print("You won!")
        Main_Menu()
        
    elif chosen_item == "rock" and user_item == "papper":
        print("I chose " + chosen_item)
        print("You lost...")
        Main_Menu()

    elif chosen_item == "scissors" and user_item == "камень":
        print("I chose " + chosen_item)
        print("You won!")
        Main_Menu()

    elif chosen_item == "scissors" and user_item == "papper":
        print("I chose " + chosen_item)
        print("You lost...")
        Main_Menu()

    
    elif chosen_item == "papper" and user_item == "scissors":
        print("I chose " + chosen_item)
        print("You won!")
        Main_Menu()
        
    elif chosen_item == "papper" and user_item == "rock":
        print("I chose " + chosen_item)
        print("You lost...")
        Main_Menu()

    else:
        print("An error occurred! You may have entered something incorrectly. Returning to the menu")
        Main_Menu()

def Curent_Time():
    now = datetime.now()
    print("Current date and time")
    print(now.strftime('%m.%d.%Y %H:%M:%S'))
    Main_Menu()

def Clear_CMD():
    os.system("cls")
    Main_Menu()

def Main_Menu():
    print("        MAIN MENU        ")
    print("1. Open notepad")
    print("2. Open calculator")
    print("3. Set a reminder")
    print("4. Current date and time")
    print("5. Clear command prompt")
    print("6. Game 'Guess the number'")
    print("7. Game 'Rock, Paper, Scissors'")
    print("8. Find information on the Internet")
    print("9. Working with text")
    print("Enter the number of the desired function (1-9)")
    user_ask = input(">>> ")
    if user_ask == "1":
        Notepad()

    elif user_ask == "2":
        Calculator()

    elif user_ask == "3":
        Reminders()

    elif user_ask == "4":
        Curent_Time()

    elif user_ask == "5":
        Clear_CMD()

    elif user_ask == "6":
        Guess_Number()

    elif user_ask == "7":
        Rock_Papper_Scissors()

    elif user_ask == "8":
        Web_Search()

    elif user_ask == "9":
        Text_Tools()
        
    else:
        print("An error occurred! You may have entered something incorrectly. Returning to the menu")
        Main_Menu()

Main_Menu()
        




    
