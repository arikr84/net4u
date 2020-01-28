from time import sleep
from colorama import Fore, init, Style

init(autoreset=True)
import tempfile
import json
import re
import random
import os

temp_directory = tempfile.gettempdir()
breakfast_price = 20
costs = []
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
rooms_dictionary = {0: {'Hotel': 'Isrotel', 'Room': 1, 'Guests': 2, 'Cost': random.randrange(250, 450), 'Days': days},
                    1: {'Hotel': 'Isrotel', 'Room': 2, 'Guests': 2, 'Cost': random.randrange(250, 450), 'Days': days},
                    2: {'Hotel': 'Isrotel', 'Room': 3, 'Guests': 3, 'Cost': random.randrange(300, 500), 'Days': days},
                    3: {'Hotel': 'Isrotel', 'Room': 4, 'Guests': 3, 'Cost': random.randrange(300, 500), 'Days': days},
                    4: {'Hotel': 'Fattal', 'Room': 1, 'Guests': 2, 'Cost': random.randrange(350, 550), 'Days': days},
                    5: {'Hotel': 'Fattal', 'Room': 2, 'Guests': 2, 'Cost': random.randrange(350, 550), 'Days': days},
                    6: {'Hotel': 'Fattal', 'Room': 3, 'Guests': 3, 'Cost': random.randrange(400, 600), 'Days': days},
                    7: {'Hotel': 'Fattal', 'Room': 4, 'Guests': 3, 'Cost': random.randrange(400, 600), 'Days': days}}


def welcome():
    print(Fore.MAGENTA + Style.BRIGHT + "hotels2go.co.il - The Best Rooms For the Best Prices!")


def terms_and_conditions():
    print(Fore.RED + Style.BRIGHT + "\n  Terms, Conditions and Information\n  " + str("-" * 33) +
          "\n- The only available rooms are from August 2 till August 6 2020 (Sunday till Thursday).\n"
          "- All prices are in USD.\n- Breakfast can be included for an extra " + str(breakfast_price) +
          "$ fee per night.")
    terms = int(input(
        "\n- Enter (" + Fore.GREEN + "1" + Fore.BLACK + ") if you accept the terms and conditions. \n- Enter (" +
        Fore.RED + "2" + Fore.BLACK + ") if you refuse the terms and conditions.\n\nPlease enter your selection: "))
    while terms != 1 and terms != 2:
        terms = int(input(
            Fore.LIGHTRED_EX + "  (" + str(terms) + ") In not a valid option. Please enter a number between 1 and 2: "))
    if terms == 1:
        print(Style.BRIGHT + Fore.GREEN + "\n<<<<<  You have accepted our terms and conditions."
                                          " Please continue with the reservation process. >>>>>\n")
    if terms == 2:
        agree = input(
            "\nYou have chosen to refuse our terms and conditions. Can we get a manager to discuss our terms and"
            " conditions with you?" + Style.BRIGHT + " (Yes/No)" + Style.NORMAL + ": ").lower()
        while agree != "yes" and agree != "no":
            agree = input(Fore.LIGHTRED_EX + "  (" + str(
                agree) + ") In not a valid option. Please enter" + Style.BRIGHT + " [Yes/No]" + Style.NORMAL +
                          ": ").lower()
        if agree == "yes":
            print("Please wait few seconds until we reach the hotels manager...")
            loading(x=10)
            quit("We are sorry, the manager is sick today and can't be reached.")
        else:
            quit("Thank you for using our services.")


def menu():
    n = int(input("\n- Enter (1) to check available rooms\n- Enter (2) to reserve a room\n- Enter (3) to cancel"
                  " reservation\n- Enter (4) to add a night to an existing reservation\n- Enter (5)"
                  " to add a room to an existing reservation\n- Enter (6) to exit\n\nEnter your selection: "))
    while n == 0 or n > 6:
        quit("Option " + str(n) + " is not available.")
    if n == 1:
        check_available_rooms()
        continue_decision()
    if n == 2:
        terms_and_conditions()
        reservation()
    if n == 3:
        cancel_reservation()
    if n == 4:
        add_night_room_to_resrvation()
    if n == 5:
        print()
    if n == 6:
        quit("Thank you for visiting us. Have a great day!")


def write_hotels_file(rooms_dictionary):
    with open(temp_directory + '/hotels.txt', 'w') as f:
        f.write(json.dumps(rooms_dictionary))


def read_hotels_file():
    with open(temp_directory + '/hotels.txt', 'r') as f:
        return json.load(f)


def hotels_file_creation():
    write_hotels_file(rooms_dictionary)


def loading(x):
    for i in range(x):
        print('.' * 5, end='')
        sleep(1)
    print("\n")


def check_available_rooms():
    available_rooms = read_hotels_file()
    for key, value in available_rooms.items():
        print("\nRoom", key)
        for key in value:
            print(key + ':', value[key])


def details_gathering_validation_and_presentation():
    details = read_hotels_file()
    # hotel selection, validation and string manipulation (for the presentation)
    selected_hotel = int(input(
        "[Please chose preferred hotel]\n- Enter (1) for 'Fattal'\n- Enter (2) for 'Isrotel'\n"
        "Enter your selection: ").lower())
    while selected_hotel != 1 and selected_hotel != 2:
        selected_hotel = int(input(Fore.RED + "[Please enter a valid option]: ").lower())
    if selected_hotel == 1:
        selected_hotel = "Fattal"
    if selected_hotel == 2:
        selected_hotel = "Isrotel"
    # arrival day and departure day selection and validation
    print(Fore.LIGHTRED_EX + "Attention: " + Fore.BLACK + Style.BRIGHT + "Can't order rooms on Friday and Saturday")
    arrival_day = input("- Please enter day of arrival between Sunday and Thursday: ").lower()
    while arrival_day != "sunday" and arrival_day != "monday" and arrival_day != "tuesday" and arrival_day != "wednesday":
        arrival_day = input(str(arrival_day) + " is not a valid arrival day. Please enter arrival day: ").lower()
    departure_day = input("- Please enter day of departure: ").lower()
    while departure_day != "monday" and departure_day != "tuesday" and departure_day != "wednesday" and departure_day != "thursday":
        departure_day = input(
            str(departure_day) + " is not a valid departure day. Please enter departure day: ").lower()
    # calculating the number of nights by subtracting the index of the departure day with the index of the arrival day
    index_arrival_day = details['1']['Days'].index(str(arrival_day).title())
    index_departure_day = details['1']['Days'].index(str(departure_day).title())
    nights_count = index_departure_day - index_arrival_day
    # number of guests selection and validation
    guests_capacity = sum(d['Guests'] for d in details.values() if d)
    guests = int(input("- Please enter number of guests: "))
    if guests > guests_capacity:
        quit("You have requested to host " + str(guests) +
             " guests which is more than our maximum (" + str(guests_capacity) + ") guests capacity.")
    # number of rooms selection and validation
    rooms = int(input("- Please enter number of rooms: "))
    if rooms > guests:
        quit("The number of requested rooms (" + str(rooms) + ") can't be higher than the number of guests (" +
             str(guests) + ").")
    # breakfast selection and validation
    breakfast = input("- You wish to include breakfast in exchange for an extra " + str(
        breakfast_price) + "$ per night? Enter [Yes/No]: ").lower()
    while breakfast != "yes" and breakfast != "no":
        breakfast = input(Fore.RED + "[Please enter 'Yes' or 'No']: ").lower()
    # personal details
    full_name = input("- Please Enter your full name: ")
    phone_number = int(input("- Enter" + str(full_name) + " phone number (e.g. 0501234567): "))
    # calculating the number of nights by subtracting the index of the departure day with the index of the arrival day
    index_arrival_day = details['1']['Days'].index(str(arrival_day).title())
    index_departure_day = details['1']['Days'].index(str(departure_day).title())
    nights_count = index_departure_day - index_arrival_day
    # presenting all the gathered information in a nice manner
    presentation(guests, nights_count, selected_hotel, breakfast, rooms, full_name, phone_number, breakfast_price)

    return selected_hotel, arrival_day, departure_day, guests, rooms, breakfast, full_name, phone_number, nights_count


def presentation(guests, nights_count, selected_hotel, breakfast, rooms, full_name, phone_number, breakfast_price):
    if breakfast == "yes":
        breakfast = "Breakfast is included in exchange for " + str(breakfast_price) + "$ per night."
    if breakfast == "no":
        breakfast = "Breakfast is not included."
    print(Style.BRIGHT + Fore.LIGHTBLUE_EX + "\nDear " + str(
        full_name) + ",\nThe phone-number you have entered is '" + str(
        phone_number) + "'.\nYou have searched for " + str(
        rooms) + " room(s) in " + str(selected_hotel) + " for " + str(
        guests) + " guests over " + str(nights_count) + " night(s).\n" + str(breakfast))
    reservation_validation = input("\n[The above reservation details are correct? Enter (Yes/No)]: ").lower()
    if reservation_validation == "yes":
        print(
            Style.BRIGHT + "\nSearching for the cheapest rooms by your demands. The rooms prices are final.")
        loading(x=10)
    if reservation_validation == "no":
        print("Please wait few seconds while restarting the reservation process.")
        loading(x=5)
        details_gathering_validation_and_presentation()


def cheapest_room():
    details = read_hotels_file()
    for i in range(8):
        costs.append(details[str(i)]['Cost'])
    low_to_high_costs_list = sorted(costs)
    for n in low_to_high_costs_list[0:3]:
        if re.search(str(n), str(details[str(1)])):
            print(details)


# def cheapest_room():
#     x = 0
#     details = read_hotels_file()
#     for i in range(8):
#         costs.append(details[str(i)]['Cost'])
#     low_to_high_costs_list = sorted(costs)
#     for n in low_to_high_costs_list[0:rooms]:
#         while not re.search(str(n), str(details[str(x)])) and x < 8:
#             x = x + 1
#         else:
#             print(details[str(x)])






# main
# welcome()
# terms_and_conditions()
# menu()

# write_hotels_file(rooms_dictionary)
# read_hotels_file()
# loading()
# check_available_rooms()
# max_guests_capacity()
# nights()
# guests_number()
# breakfast()
# hotel_selection()
# rooms_number()
# presentation(guests=guests_number(), nights_count=nights(), selected_hotel=hotel_selection(), bf=breakfast(), rooms=rooms_number(), full_name, phone_number, identification_number,
#              breakfast_price)
# nights()
# details_gathering()
# details_validation()
# details_gathering_validation_and_presentation()
cheapest_room()
