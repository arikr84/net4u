from time import sleep
from colorama import Fore, init, Style

init(autoreset=True)
import tempfile
import json
import re
import random


def menu():
    counter = 0
    main_menu = int(input("\n- Enter (1) to show the Dr's schedule\n- Enter (2) to schedule an appointment\n\nEnter your selection: "))
    while main_menu == 0 or main_menu > 2:
        counter = counter + 1
        if counter < 2:
            main_menu = int(input(Fore.RED + str(main_menu) + " is not a valid selection. Enter an option between 1 and 2: "))
        else:
            quit(Fore.RED + "\nMaximum tries exceeded. Good-Bye.")
    if main_menu == 1:
        dr_selection()
        if
        dr_idan_menu()
    if main_menu == 2:
        print()


def dr_selection():
    counter = 0
    dr = int(input("\n- Enter (1) to show Dr Idan schedule\n- Enter (1) to show Dr Hakim schedule\n\nEnter your selection: "))
    while dr == 0 or dr > 2:
        counter = counter + 1
        if counter < 2:
            dr = int(input(Fore.RED + str(dr) + " is not a valid selection. Enter an option between 1 and 2: "))
        else:
            quit(Fore.RED + "\nMaximum tries exceeded. Good-Bye.")
    return dr


def dr_idan_menu():
    counter = 0
    idan_menu = int(
        input("\n- Enter (1) to show Dr Idan schedule\n- Enter (2) to schedule an appointment for Dr Idan\n\nEnter your selection: "))
    while idan_menu == 0 or idan_menu > 2:
        counter = counter + 1
        if counter < 2:
            idan_menu = int(input(Fore.RED + str(idan_menu) + " is not a valid selection. Enter an option between 1 and 2: "))
        else:
            quit(Fore.RED + "\nMaximum tries exceeded. Good-Bye.")
    return idan_menu

def dr_hakim_menu():
    counter = 0
    hakim_menu = int(
        input("\n- Enter (1) to show Dr Hakim schedule\n- Enter (2) to schedule an appointment for Dr Hakim\n\nEnter your selection: "))
    while hakim_menu == 0 or hakim_menu > 2:
        counter = counter + 1
        if counter < 2:
            hakim_menu = int(Fore.RED + input(str(hakim_menu) + " is not a valid selection. Enter an option between 1 and 2: "))
        else:
            quit(Fore.RED + "\nMaximum tries exceeded. Good-Bye.")
    return hakim_menu


menu()