from time import sleep
from colorama import Fore, init, Style
init(autoreset=True)
import tempfile
import json
import re
import random

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

def readlines_hotels():
    temp_directory = tempfile.gettempdir()
    for line in open(str(temp_directory) + "/hotels.txt", "r").readlines():
        file = line.replace("'", "\"")
        file = json.loads(file)

def max_guests_capacity():
    guest_capacity = 0
    temp_directory = tempfile.gettempdir()
    for line in open(str(temp_directory) + "/hotels.txt", "r").readlines():
        hotels = line.replace("'", "\"")
        hotels = json.loads(hotels)
        if not re.search("'day': \[]", line):
            guest_capacity = guest_capacity + list(hotels.values())[2]
    return guest_capacity

def decision(x):
    decision = int(input(Style.BRIGHT + Fore.GREEN + "\n\nEnter (1) purchase and reserve the cheapest " + str(x) + " room(s)\n" + Fore.RED + "Enter (2) to withdraw the reservation\n\n" + Style.NORMAL + Fore.BLACK + "Please enter your decision: "))
    while decision != 1 and decision != 2:
        decision = int(input(str(decision) + " is not a valid option. Please enter 1 or 2: "))
    if decision == 1:
        print(Style.BRIGHT + Fore.BLUE + "\n>>> Thank you for choosing our hotels network. We wish you the finest vacation. Please wait few moments while we handle your reservation...")
        sleep(5)
    if decision == 2:
        quit("Thank you for using our services. Good-Bye!")

def terms_and_conditions():
    print(Fore.RED + Style.BRIGHT + "\n  Terms, Conditions and Information\n  " + str("-" * 33) +
          Fore.LIGHTBLACK_EX + "\n- We offer rooms for 2 guests or 3 guests\n"
                               "- The rooms price does not include breakfast\n"
                               "- All prices are in USD\n- Breakfast can be included for an extra 50$ per night")
    terms = int(input("\n- Enter (1) if you accept the terms and conditions: \n- Enter (2) if you refuse the terms and"
                      " conditions: "))
    while terms != 1 and terms != 2:
        terms = int(input(Fore.LIGHTRED_EX + "  (" + str(terms) + ") In not a valid option. Please enter a number between 1 and 2: "))
    if terms == 1:
        print(Style.BRIGHT + "\n<<<<<  You have accepted our terms and conditions. Please continue with the reservation"
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

def presentation(a,b,c,d,e):
    print(Style.BRIGHT + Fore.BLUE + "\nYou have requested us to host " + str(a) + " guests in " + str(
        b) + " rooms for " + str(c) + " nights in " + str(d) + " | breakfast = " + str(e))
    print(Style.BRIGHT + "\nThe following room(s) are the cheapest rooms we could find for you:\n" + str("-") * 67)

def available_rooms_empty_file_creation():
    temp_directory = tempfile.gettempdir()
    available_rooms = open(str(temp_directory) + "/available_rooms.txt", "w+")
    available_rooms.write("")

def reservation():
    global hotels
    temp_directory = tempfile.gettempdir()
    available_rooms_counter = 0
    nights_counter = 0
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

    with open(str(temp_directory) + "/hotels.txt") as f:
        available_rooms_lines_count = len(f.readlines())
        if available_rooms_lines_count < rooms:
            quit("You have requested " + str(rooms) + " room(s). There are only " + str(available_rooms_lines_count) +
                 " room(s) available matching the requested " + str(nights) + " nights" )

    guests_per_room = guests / rooms
    if guests_per_room > 3.0:
        quit("To allocate " + str(guests) + " guests within " + str(rooms) + " room(s) means that we have to disperse " +
             "more than 3 guests per room while our biggest room can only accommodate maximum of 3 guests.")


    hotels_preferation = int(input("\n[Please select the hotels you wish to see available rooms from]\n\n- Enter (1) for 'Fattal'\n- Enter (2) for 'Isrotel'"
                                                                    "\n- Enter (3) for both 'Fattal' and 'Isrotel'\n\nPlease enter your selection: ").lower())
    while hotels_preferation != 1 and hotels_preferation != 2 and hotels_preferation != 3:
        hotels_preferation = int(input(Fore.RED + "[Please enter option 1 to 3]: ").lower())
    if hotels_preferation == 1:
        hotel_name = "Fattal"
    if hotels_preferation == 1 and rooms > 4:
        quit("You have requested " + str(rooms) + " room(s). The maximum number of rooms in Fattal is 4")
    if hotels_preferation == 2:
        hotel_name = "Isrotel"
    if hotels_preferation == 2 and rooms > 4:
        quit("You have requested " + str(rooms) + " room(s). The maximum number of rooms in Isrotel is 4")
    if hotels_preferation == 3:
        hotel_name = "Fattal and Isrotel"
    if hotels_preferation == 3 and rooms > 8:
        quit("You have requested " + str(rooms) + " room(s). The maximum number of rooms in both Fattal and Isrotel is 8")

    breakfast = input("[You wish to include breakfast in exchange for an extra " + Style.BRIGHT + Fore.GREEN + "50$" + Style.NORMAL + Fore.BLACK + " per night (Yes/No)]: ").lower()
    while breakfast != "yes" and breakfast != "no":
        breakfast = input(Fore.RED + "[Please enter 'Yes' or 'No']: ").lower()

    if breakfast == "yes":
        print(Style.BRIGHT + "\nPresenting all the rooms that are available for " + str(nights) + " nights with breakfast cost included:\n" + str("-") * 86)
        available_rooms_empty_file_creation()
        for line in open(str(temp_directory) + "/hotels.txt", "r").readlines():
            hotels = line.replace("'", "\"")
            hotels = json.loads(hotels)
            available_rooms = open(str(temp_directory) + "/available_rooms.txt", "a+")
            if int(len(list(hotels.values())[4])) > nights:
                hotels['cost'] = hotels['cost'] + 50
                print(Fore.LIGHTBLACK_EX + str(hotels).replace("{", "").replace("}", "").replace("'", ""))
                available_rooms.write("{}\n".format(str(hotels)))
                costs.append(list(hotels.values())[3])
                costs = sorted(costs)
        presentation(guests,rooms,nights,hotel_name,breakfast)
        for i in range(available_rooms_counter):
            for line in open(str(temp_directory) + "/available_rooms.txt", "r").readlines():
                available_rooms = line.replace("'", "\"")
                available_rooms = json.loads(available_rooms)
                if hotels_preferation == 1:
                    if re.search(str(costs[i]), str(available_rooms)):
                        if re.search("Fattal", str(available_rooms)):
                            print(Fore.LIGHTBLUE_EX + str(available_rooms).replace("{", "").replace("}", "").replace("'", ""))
                if hotels_preferation == 2:
                    if re.search("Isrotel", str(available_rooms)):
                        if re.search(str(costs[i]), str(available_rooms)):
                            print(Fore.LIGHTBLUE_EX + str(available_rooms).replace("{", "").replace("}", "").replace("'", ""))
                if hotels_preferation == 3:
                    if re.search(str(costs[i]), str(available_rooms)):
                        print(Fore.LIGHTBLUE_EX + str(available_rooms).replace("{", "").replace("}","").replace("'", ""))

    if breakfast == "no":
        print(Style.BRIGHT + "\nPresenting all the rooms that are available for " + str(nights) + " nights:\n" + (str("-") * 57))
        available_rooms_empty_file_creation()
        for line in open(str(temp_directory) + "/hotels.txt", "r").readlines():
            hotels = line.replace("'", "\"")
            hotels = json.loads(hotels)
            available_rooms = open(str(temp_directory) + "/available_rooms.txt", "a+")
            if int(len(list(hotels.values())[4])) > nights:
                print(Fore.LIGHTBLACK_EX + str(hotels).replace("{", "").replace("}", "").replace("'", ""))
                available_rooms.write("{}\n".format(str(hotels)))
                costs.append(list(hotels.values())[3])
                costs = sorted(costs)
                continue
        presentation(guests,rooms,nights,hotel_name,breakfast)
        for i in range(available_rooms_counter):
            for line in open(str(temp_directory) + "/available_rooms.txt", "r").readlines():
                available_rooms = line.replace("'", "\"")
                available_rooms = json.loads(available_rooms)
                if hotels_preferation == 1:
                    if re.search(str(costs[i]), str(available_rooms)):
                        if re.search("Fattal", str(available_rooms)):
                            print(Fore.LIGHTBLUE_EX + str(available_rooms).replace("{", "").replace("}", "").replace("'", ""))

                if hotels_preferation == 2:
                    if re.search("Isrotel", str(available_rooms)):
                        if re.search(str(costs[i]), str(available_rooms)):
                            print(Fore.LIGHTBLUE_EX + str(available_rooms).replace("{", "").replace("}", "").replace("'", ""))


                if hotels_preferation == 3:
                    if re.search(str(costs[i]), str(available_rooms)):
                        print(Fore.LIGHTBLUE_EX + str(available_rooms).replace("{", "").replace("}","").replace("'", ""))

        decision(rooms)


                    #         reservation = open(str(temp_directory) + "/reservation.txt", "a+")
                    #         reservation.write(str(available_rooms) + "\n")
                    #         print(Style.BRIGHT + Fore.GREEN + str(available_rooms))



welcome()
menu()


#1 Understand how many rooms there are available for 2 people
#2 Understand how many rooms there are available for 3 people
#3 calculate the amount of people // 2          -  add them people to the rooms for 2 people
#4 The calculation will yield number of requires rooms (X). check which 2 people rooms are the cheapers
#5 if leftovers people calcule the leftovers // 3           -  add them people to the rooms for 2 people
#6 The calculation will yield number of requires rooms (X). check which 2 people rooms are the cheapers

