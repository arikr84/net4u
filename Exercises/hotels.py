from colorama import Fore, init, Style
init(autoreset=True)
import tempfile
import json
import re
import random

def menu():
    break_counter = 0
    option = int(input(Fore.MAGENTA + "Trivago\n" + Fore.BLUE + "The Best Rooms For the Best Prices.\n\n" + Fore.BLACK +
                       "- Enter (1) to check available rooms\n- Enter (2) to reserve a room\n- Enter (3) to cancel"
                       " reservation\n- Enter (4) to add night/room for a reservation\n\nEnter your selection: "))
    while option == 0 or option > 4:
        break_counter = break_counter + 1
        if break_counter < 6:
            option = int(input("Option (" + str(option) + ") is not available. Enter an option between 1 to 4: "))
        else:
            print(Fore.RED + "\nYou exceeded the maximum invalid entries. Exiting...")
            quit()
    if option == 0 or option > 4:
        print(Fore.RED + "\nERROR: Maximum (5) tries exceeded. Next time enter an option between 1 to 5. Exiting...")
    if option == 1:
        check_available_rooms()
    if option == 2:
        reservation()
    if option == 3:
        cancel_reservation()
    if option == 4:
        add_night_room_to_resrvation()

def files_creation():
    temp_directory = tempfile.gettempdir()
    hotels = open(str(temp_directory) + "/hotels.txt", "w+")
    hotels.write("{} {} {} {} {}".format("{'hotel': 'Fattal',", "'room': 1,", "'guests': 2,", "'cost': " + str(random.randrange(200, 500)) + ",", "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels = open(str(temp_directory) + "/hotels.txt", "a+")
    hotels.write("\n{} {} {} {} {}".format("{'hotel': 'Fattal',", "'room': 2,", "'guests': 2,", "'cost': " + str(random.randrange(200, 500)) + ",", "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels.write("\n{} {} {} {} {}".format("{'hotel': 'Fattal',", "'room': 3,", "'guests': 3,", "'cost': " + str(random.randrange(200, 500)) + ",", "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels.write("\n{} {} {} {} {}".format("{'hotel': 'Fattal',", "'room': 4,", "'guests': 3,", "'cost': " + str(random.randrange(200, 500)) + ",", "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels.write("\n{} {} {} {} {}".format("{'hotel': 'Isrotel',", "'room': 1,", "'guests': 2,", "'cost': " + str(random.randrange(200, 500)) + ",", "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels.write("\n{} {} {} {} {}".format("{'hotel': 'Isrotel',", "'room': 2,", "'guests': 2,", "'cost': " + str(random.randrange(200, 500)) + ",", "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels.write("\n{} {} {} {} {}".format("{'hotel': 'Isrotel',", "'room': 3,", "'guests': 3,", "'cost': " + str(random.randrange(200, 500)) + ",", "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels.write("\n{} {} {} {} {}".format("{'hotel': 'Isrotel',", "'room': 4,", "'guests': 3,", "'cost': " + str(random.randrange(200, 500)) + ",", "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels.close()

    reservation = open(str(temp_directory) + "/reservation.txt", "w+")
    reservation.close()

def check_available_rooms():
    temp_directory = tempfile.gettempdir()
    for line in open(str(temp_directory) + "/hotels.txt", "r").readlines():
        hotels = line.replace("'", "\"")
        hotels = json.loads(hotels)
        print(Fore.LIGHTBLUE_EX + str(hotels))

def max_guests_capacity():
    guest_capacity = 0
    temp_directory = tempfile.gettempdir()
    for line in open(str(temp_directory) + "/hotels.txt", "r").readlines():
        hotels = line.replace("'", "\"")
        hotels = json.loads(hotels)
        if not re.search("'day': \[]", line):
            guest_capacity = guest_capacity + list(hotels.values())[2]
    return guest_capacity // 2

def reservation():
    temp_directory = tempfile.gettempdir()
    available_rooms_counter = 0
    nights_counter = 0
    guest_capacity = max_guests_capacity()

    guests = int(input(Style.BRIGHT + "[Please enter guests number]: "))
    if guests > guest_capacity:
        quit("You have requested to host " + str(guests) + " guests which is more than our maximum capacity (" + str
        (guest_capacity) + ")")

    rooms = int(input(Style.BRIGHT + "[Please enter how many room you wish to acquire]: "))
    if rooms > guests:
        quit("The number of requested rooms (" + str(rooms) + ") can't be lower than the number of guests (" +
             str(guests) + ").")

    for line in open(str(temp_directory) + "/hotels.txt", "r").readlines():
        if not re.search("'day': \[]", line):
            available_rooms_counter = available_rooms_counter + 1
    available_rooms_counter = available_rooms_counter // 2
    if rooms > available_rooms_counter:
        quit("You requested more rooms (" + str(rooms) + ") than our maximum available rooms (" +
             str(available_rooms_counter) + ").")

    nights = int(input(Style.BRIGHT + "[Please enter how many nights you wish to stay]: "))
    for line in open(str(temp_directory) + "/hotels.txt", "r").readlines():
        file = line.replace("'", "\"")
        file = json.loads(file)
        if nights > len(list(file.values())[4]) - 1:
            nights_counter = nights_counter + 1
    nights_counter = nights_counter // 2
    if nights_counter == 8:
        quit("Couldn't find a single room that is available for " + str(nights) + " night(s)")

    breakfast = input(Style.BRIGHT + "[You wish to enjoy our breakfast in exchange for 50$ per night (Yes/No)]: ").lower()
    while breakfast != "yes" and breakfast != "no":
        breakfast = input(Style.BRIGHT + "[Please enter 'Yes' or 'No']: ").lower()

    reservation = open(str(temp_directory) + "/reservation.txt", "w+")

menu()
#
# guests / rooms == how many people inside 1 room.  if return > 3 it's not possible since max room size is 3
# if == 3 need to check if there are available rooms for 3 people ---- for example if 6 guests want 2 rooms I need to find 2 rooms that can fill each 3 people
# if == 2 or less than 2 need to find any available rooms to fill these people

#1 Understand how many rooms there are available for 2 people
#2 Understand how many rooms there are available for 3 people
#3 calculate the amount of people // 2          -  add them people to the rooms for 2 people
#4 The calculation will yield number of requires rooms (X). check which 2 people rooms are the cheapers
#5 if leftovers people calcule the leftovers // 3           -  add them people to the rooms for 2 people
#6 The calculation will yield number of requires rooms (X). check which 2 people rooms are the cheapers