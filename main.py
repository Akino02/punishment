import os
from memory import *
import tkinter as tk

nav_menu = ["Add deaths", "Delete deaths", "Show users"]
nav_add_d = ["Existing user", "New user"]

users_deaths = {}

def user_i(data_type, text):
    try:
        user_input = data_type(input(text))
        return user_input
    except:
        return

def menu(data:dict):
    print("Menu: ")
    for i, text in enumerate(nav_menu):
        print(f"{i+1}) {text}")
    user_input = user_i(int, "Choose: ")
    print(" ")
    os.system("cls")
    if user_input == 1:
        add_d(data)
    elif len(data) <= 0:
        print("You must create at least one user\n")
    elif user_input == 2:
        del_d(data)
    elif user_input == 3:
        show_users(data)
    
def add_d(data:dict):
    data = data
    os.system("cls")
    try:
        for i, text in enumerate(nav_add_d):
            print(f"{i+1}) {text}")
        user_input = user_i(int, "Choose: ")
        print(" ")
        user_picked = ""
        if user_input == 1:
            if len(data) > 0:
                user_picked = pick_user(data)
            else:
                os.system("cls")
                print("You must create at least one user\n")
                return
        elif user_input == 2:
            user_picked = user_i(str, "Enter user name: ")
        data[user_picked] = data[user_picked] + user_i(int, "Append number of deaths: ") if user_input == 1 else user_i(int, "Enter number of another deaths: ")
        save_data(data)
    except:
        return

def pick_user(data:dict):
    users = []
    user_picked = ""
    show_users(data)
    try:
        for name in data:
            users.append(name)
        user_input = user_i(int, "Choose user: ")
        for index in range(len(users)):
            if index == user_input-1:
                user_picked = users[index]
        return user_picked
    except:
        return

def del_d(data:dict):
    os.system("cls")
    show_users(data)
    print(" ")
    user_picked = pick_user(data)
    try:
        if len(data) > 0:
            num_del_d = user_i(int, "Enter number of completed deaths: ")
            if data[user_picked] > 0 and data[user_picked]-num_del_d >=0:
                data[user_picked] = data[user_picked] - num_del_d
            else:
                print("You can't do more than you have")
            save_data(data)
    except:
        return

def show_users(data:dict):
    os.system("cls")
    print("Users: ")
    for index, name in enumerate(data):
        print(f"{index+1}] {name}: {data[name]} users deaths == {data[name]*10} kliku")
    print(" ")

if __name__ == "__main__":
    while True:
        users_deaths = load_data()
        menu(users_deaths)
