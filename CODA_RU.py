import os
import time
import webbrowser
import random
from datetime import datetime

def Notepad():
    os.system("notepad")
    print("Блокнот открыт!")
    Main_Menu()

def Calculator():
    os.system("calc")
    print("Калькулятор открыт!")
    Main_Menu()

def Reminders():
    reminder = input("Введите текст напоминания: ")
    time = input("Когда напомнить (дд.мм.гггг чч:мм): ")
    with open('reminders.txt', 'a') as f:
        f.write(f"{time}|{reminder}\n")
    print(f"Напоминание '{reminder}' создано на {time}")
    Main_Menu()

def Text_Tools():
    print(" Работа с текстом ")
    text = input("Введите текст: ")
    print("1. Верхний регистр:", text.upper())
    print("2. Нижний регистр:", text.lower())
    print("3. Длина текста:", len(text), "символов")
    print("4. Количество слов:", len(text.split()))
    Main_Menu()

def Web_Search():
    print("Что найти в интернете?")
    user_request = input(">>> ")
    webbrowser.open(f"https://yandex.ru/search/?text={user_request}")
    print("Открываю результаты поиска...")
    Main_Menu()

def Guess_Number():
    number = random.randint(0, 100)
    print("Я загадал число от 0 до 100, сможешь угадать?")
    user_guess = int(input(">>> "))
    if number == user_guess:
        print("Ты выиграл! Поздравляю!")
        Main_Menu()
    elif number != user_guess:
        print("Извини, но ты проиграл, попробуй в следующий раз.")
        Main_Menu()
    else:
        print("Возникла ошибка! Возможно вы ввели что-то не то. Возвращаюсь в меню")
        Main_Menu

def Rock_Papper_Scissors():
    items = ["камень", "ножницы", "бумага"]
    chosen_item = random.choice(items)
    print("Выберите: камень, ножницы или бумага")
    user_item = str(input(">>> "))
    if chosen_item == user_item:
        print("Ничья!")
        Main_Menu()
        
    elif chosen_item == "камень" and user_item == "ножницы":
        print("Я выбрал " + chosen_item)
        print("Вы выиграли!")
        Main_Menu()
        
    elif chosen_item == "камень" and user_item == "бумага":
        print("Я выбрал " + chosen_item)
        print("Вы проиграли...")
        Main_Menu()

    elif chosen_item == "ножницы" and user_item == "камень":
        print("Я выбрал " + chosen_item)
        print("Вы выиграли!")
        Main_Menu()

    elif chosen_item == "ножницы" and user_item == "бумага":
        print("Я выбрал " + chosen_item)
        print("Вы проиграли...")
        Main_Menu()

    
    elif chosen_item == "бумага" and user_item == "ножницы":
        print("Я выбрал " + chosen_item)
        print("Вы выиграли!")
        Main_Menu()
        
    elif chosen_item == "бумага" and user_item == "камень":
        print("Я выбрал " + chosen_item)
        print("Вы проиграли")
        Main_Menu()

    else:
        print("Возникла ошибка! Возможно вы ввели что-то не то. Возвращаюсь в меню")
        Main_Menu()

def Curent_Time():
    now = datetime.now()
    print("Текущая дата и время")
    print(now.strftime('%d.%m.%Y %H:%M:%S'))
    Main_Menu()

def Clear_CMD():
    os.system("cls")
    Main_Menu()

def Main_Menu():
    print("        ГЛАВНОЕ МЕНЮ        ")
    print("1. Открыть блокнот")
    print("2. Открыть калькулятор")
    print("3. Сделать напоминание")
    print("4. Текущая дата и время")
    print("5. Очистить командную строку")
    print("6. Игра 'Угадай число'")
    print("7. Игра 'Камень, ножницы, бумага'")
    print("8. Найти в интернете информацию")
    print("9. Работа с текстом")
    print("Введите номер нужной функции (1-9)")
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
        print("Возникла ошибка! Возможно вы ввели что-то не то. Возвращаюсь в меню")
        Main_Menu()

Main_Menu()
        




    
