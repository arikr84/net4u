from time import sleep
from colorama import Fore, init, Style
init(autoreset=True)
import tempfile
import json
import re
import random
import os

def welcome():
    print(Fore.MAGENTA + Style.BRIGHT + "Drivago - The Best Rooms For the Best Prices")

def menu():
    break_counter = 0
    option = int(input("\n- Enter (1) to check available rooms\n- Enter (2) to reserve a room\n- Enter (3) to cancel"
                       " reservation\n- Enter (4) to add night/room for a reservation\n- Enter (5) to exit\n\nEnter your selection: "))
    while option == 0 or option > 5:
        break_counter = break_counter + 1
        if break_counter < 6:
            option = int(input("Option (" + str(option) + ") is not available. Enter an option between 1 to 5: "))
        else:
            print(Fore.RED + "\nYou exceeded the maximum invalid entries. Good-Bye!")
            quit()
    if option == 0 or option > 5:
        print(Fore.RED + "\nERROR: Maximum (5) tries exceeded. Next time enter an option between 1 to 5. Good-Bye!")
    if option == 1:
        check_available_rooms()
    if option == 2:
        terms_and_conditions()
        reservation()
    if option == 3:
        cancel_reservation()
    if option == 4:
        add_night_room_to_resrvation()
    if option == 5:
        quit("Thank you for using our services. Good-Bye!")

def files_creation():
    temp_directory = tempfile.gettempdir()
    hotels = open(str(temp_directory) + "/hotels.txt", "w+")
    hotels.write("{} {} {} {} {}".format("{'hotel': 'Fattal',", "'room': 1,", "'maximum guests capacity': 2,", "'cost': " + str(random.randrange(200, 450)) + ",", "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels = open(str(temp_directory) + "/hotels.txt", "a+")
    hotels.write("\n{} {} {} {} {}".format("{'hotel': 'Fattal',", "'room': 2,", "'maximum guests capacity': 2,", "'cost': " + str(random.randrange(200, 450)) + ",", "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels.write("\n{} {} {} {} {}".format("{'hotel': 'Fattal',", "'room': 3,", "'maximum guests capacity': 3,", "'cost': " + str(random.randrange(200, 450)) + ",", "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels.write("\n{} {} {} {} {}".format("{'hotel': 'Fattal',", "'room': 4,", "'maximum guests capacity': 3,", "'cost': " + str(random.randrange(200, 450)) + ",", "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels.write("\n{} {} {} {} {}".format("{'hotel': 'Isrotel',", "'room': 1,", "'maximum guests capacity': 2,", "'cost': " + str(random.randrange(300, 550)) + ",", "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels.write("\n{} {} {} {} {}".format("{'hotel': 'Isrotel',", "'room': 2,", "'maximum guests capacity': 2,", "'cost': " + str(random.randrange(300, 550)) + ",", "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels.write("\n{} {} {} {} {}".format("{'hotel': 'Isrotel',", "'room': 3,", "'maximum guests capacity': 3,", "'cost': " + str(random.randrange(300, 550)) + ",", "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels.write("\n{} {} {} {} {}".format("{'hotel': 'Isrotel',", "'room': 4,", "'maximum guests capacity': 3,", "'cost': " + str(random.randrange(300, 550)) + ",", "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels.close()

    reservation = open(str(temp_directory) + "/reservation.txt", "w+")
    reservation.close()

def check_available_rooms():
    print(Style.BRIGHT + "\nAvailable Rooms:")
    temp_directory = tempfile.gettempdir()
    for line in open(str(temp_directory) + "/hotels.txt", "r").readlines():
        hotels = line.replace("'", "\"")
        hotels = json.loads(hotels)
        print(Fore.LIGHTBLUE_EX + str(hotels).replace("{","").replace("}","").replace("'",""))

def max_guests_capacity():
    guest_capacity = 0
    temp_directory = tempfile.gettempdir()
    for line in open(str(temp_directory) + "/hotels.txt", "r").readlines():
        hotels = line.replace("'", "\"")
        hotels = json.loads(hotels)
        if not re.search("'day': \[]", line):
            guest_capacity = guest_capacity + list(hotels.values())[2]
    return guest_capacity

def decision():
    decision = input("\nEnter '1' to continue with the suggested offer\nEnter '2' to get a new offer from 1 hotel only"
                     "\nEnter '3' to chose which hotel to reside in\nEnter '4' to withdraw the reservation\n\nPlease enter you decision: ")
    while decision != 1 and decision != 2 and decision != 3:
        decision = input(str(decision) + " In not a valid option. Please enter a number between 1 and 3: ")
    if decision == 1:
        print("Thank you for counting on us to supply the best and cheapest rooms for you.")
        pass
    if decision == 2:
        print()
    if decision == 3:
        print()
    if decision == 4:
        quit("Thank you for using our services. Good-Bye!")

def terms_and_conditions():
    print(Fore.RED + Style.BRIGHT + "\n  Terms and Conditions\n  " + str("-" * 20) +
          Fore.LIGHTBLACK_EX + "\n- we offer rooms for 2 guests 3 guests only\n"
                               "- the rooms price does not include breakfast\n"
                               "- breakfast can be included for an extra 50$ per night")
    terms = int(input("\n- Enter (1) if you accept the terms and conditions: \n- Enter (2) if you refuse the terms and"
                      " conditions: "))
    while terms != 1 and terms != 2:
        terms = int(input(Fore.LIGHTRED_EX + "  (" + str(terms) + ") In not a valid option. Please enter a number between 1 and 2: "))
    if terms == 1:
        print(Fore.GREEN + Style.BRIGHT + "\n<<<<<  You have accepted our terms and conditions. Please continue with the reservation"
                                  " process. >>>>>\n")
    if terms == 2:
        agree = input("\n  We apologise that you refused our terms and conditions. Can we get a manager to discuss our terms and"
             " conditions with you? [Yes/No]: ").lower()
        while agree != "yes" and agree != "no":
            agree = input(Fore.LIGHTRED_EX + "  (" + str(agree) + ") In not a valid option. Please enter [Yes/No]: ").lower()
        if agree == "yes":
            print(Fore.LIGHTBLUE_EX + "Please wait a few moments until we reach the hotels manager...")
            sleep(10)
            quit("We are sorry, the manager is sick today and can't be reached. Good-bye..")
        else:
            quit("Thank you for using our services. Good-Bye!")

def reservation():
    global hotels
    temp_directory = tempfile.gettempdir()
    available_rooms_counter = 0
    nights_counter = 0
    rooms_counter = 0
    costs = []
    guest_capacity = max_guests_capacity()

    guests = int(input("[Please enter number of guests]: "))
    if guests > guest_capacity:
        quit("You have requested to host " + str(guests) + " guests which is more than our maximum capacity (" + str
        (guest_capacity) + ")")

    nights = int(input("[Please enter how many nights you wish to stay]: "))
    for line in open(str(temp_directory) + "/hotels.txt", "r").readlines():
        file = line.replace("'", "\"")
        file = json.loads(file)
        if nights > len(list(file.values())[4]) - 1:
            nights_counter = nights_counter + 1
    nights_counter = nights_counter
    if nights_counter == 8:
        quit("Couldn't find a single room that is available for " + str(nights) + " night(s)")

    rooms = int(input("[Please enter how many rooms you wish to reserve]: "))
    if rooms > guests:
        quit("The number of requested rooms (" + str(rooms) + ") can't be higher than the number of guests (" +
             str(guests) + "). This is a strict policy in our hotels network.")

    for line in open(str(temp_directory) + "/hotels.txt", "r").readlines():
        if not re.search("'day': \[]", line):
            available_rooms_counter = available_rooms_counter + 1
    available_rooms_counter = available_rooms_counter
    if rooms > available_rooms_counter:
        quit("You requested more rooms (" + str(rooms) + ") than our maximum available rooms (" +
             str(available_rooms_counter) + ").")

    with open(str(temp_directory) + "/available_rooms.txt") as f:
        available_rooms_lines_count = len(f.readlines())
        if available_rooms_lines_count < rooms:
            quit("You have requested " + str(rooms) + " rooms. There are only " + str(available_rooms_lines_count) +
                 " rooms available matching the requested " + str(nights) + " nights" )

    guests_per_room = guests / rooms
    if guests_per_room > 3.0:
        quit("To allocate " + str(guests) + " guests within " + str(rooms) + " rooms means that we have to disperse " +
             "more than 3 guests per room while our biggest room can only accommodate maximum of 3 guests.")

    if guests > 2:
        same_hotel = input("[Would you agree to disperse the guests to separate hotels if it results in lower prices? (Yes/No)]: ").lower()
        while same_hotel != "yes" and same_hotel != "no":
            same_hotel = input(Fore.RED + "[Please enter 'Yes' or 'No']: ").lower()

    breakfast = input("[You wish to enjoy our breakfast in exchange for an extra " + Fore.MAGENTA + "50$" + Fore.BLACK + " per night (Yes/No)]: ").lower()
    while breakfast != "yes" and breakfast != "no":
        breakfast = input(Fore.RED + "[Please enter 'Yes' or 'No']: ").lower()

    if breakfast == "yes":
        print(Style.BRIGHT + "\nPresenting all the rooms that are available for " + str(nights) + " nights with breakfast cost included:\n" + str("-") * 86)
        available_rooms = open(str(temp_directory) + "/available_rooms.txt", "w+")
        available_rooms.write("")
        for line in open(str(temp_directory) + "/hotels.txt", "r").readlines():
            hotels = line.replace("'", "\"")
            hotels = json.loads(hotels)
            available_rooms = open(str(temp_directory) + "/available_rooms.txt", "a+")
            if int(len(list(hotels.values())[4])) > nights:
                hotels['cost'] = hotels['cost'] + 50
                print(Fore.LIGHTBLACK_EX + str(hotels))
                available_rooms.write("{}\n".format(str(hotels)))
                costs.append(list(hotels.values())[3])
                costs = sorted(costs)
                continue
        print(Style.BRIGHT + Fore.BLUE + "\n\nYou requested to host " + str(guests) + " guests in " + str(rooms) + " rooms for " + str(nights) + " nights with breakfast included." + Fore.BLACK + "\nThe following " + str(rooms) + " room(s) are the cheapest rooms we could find for you with breakfast cost included:\n" + Fore.RED + "Notice:" + Fore.BLACK +
              " some rooms can reside in " + Fore.MAGENTA + "Fattal " + Fore.BLACK + "and others in " + Fore.MAGENTA +
              "Isrotel\n" + Fore.BLACK +  str("-") * 98)
        for i in range(rooms):
            for line in open(str(temp_directory) + "/available_rooms.txt", "r").readlines():
                available_rooms = line.replace("'", "\"")
                available_rooms = json.loads(available_rooms)
                if re.search(str(costs[i]), str(available_rooms)):
                    print(Style.BRIGHT + Fore.GREEN + str(available_rooms))
    if breakfast == "no":
        print(Style.BRIGHT + "\nPresenting all the rooms that are available for " + str(
            nights) + " nights:\n" + str("-") * 57)
        available_rooms = open(str(temp_directory) + "/available_rooms.txt", "w+")
        available_rooms.write("")
        for line in open(str(temp_directory) + "/hotels.txt", "r").readlines():
            hotels = line.replace("'", "\"")
            hotels = json.loads(hotels)
            available_rooms = open(str(temp_directory) + "/available_rooms.txt", "a+")
            if int(len(list(hotels.values())[4])) > nights:
                print(Fore.LIGHTBLACK_EX + str(hotels))
                available_rooms.write("{}\n".format(str(hotels)))
                costs.append(list(hotels.values())[3])
                costs = sorted(costs)
                continue
        print(Style.BRIGHT + "\n\nThe following " + str(
            rooms) + " room(s) are the cheapest rooms we could find for you:\n" + Fore.RED + "Notice:" + Fore.BLACK +
              " some rooms can reside in " + Fore.MAGENTA + "Fattal " + Fore.BLACK + "and others in " + Fore.MAGENTA +
              "Isrotel\n" + Fore.BLACK + str("-") * 69)
        for i in range(rooms):
            for line in open(str(temp_directory) + "/available_rooms.txt", "r").readlines():
                available_rooms = line.replace("'", "\"")
                available_rooms = json.loads(available_rooms)
                if re.search(str(costs[i]), str(available_rooms)):
                    print(Style.BRIGHT + Fore.GREEN + str(available_rooms))

    reservation = open(str(temp_directory) + "/reservation.txt", "w+")


welcome()
menu()


#1 Understand how many rooms there are available for 2 people
#2 Understand how many rooms there are available for 3 people
#3 calculate the amount of people // 2          -  add them people to the rooms for 2 people
#4 The calculation will yield number of requires rooms (X). check which 2 people rooms are the cheapers
#5 if leftovers people calcule the leftovers // 3           -  add them people to the rooms for 2 people
#6 The calculation will yield number of requires rooms (X). check which 2 people rooms are the cheapers

