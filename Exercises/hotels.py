from time import sleep
from colorama import Fore, init, Style

init(autoreset=True)
import tempfile
import json
import re
import random


def welcome():
    print(Fore.MAGENTA + Style.BRIGHT + "Drivago - The Best Rooms For the Best Prices!")


def menu():
    break_counter = 0
    option = int(input("\n- Enter (1) to check available rooms\n- Enter (2) to reserve a room\n- Enter (3) to cancel"
                       " reservation\n- Enter (4) to add night/room for a reservation\n- Enter (5) to exit\n\nEnter your selection: "))
    while option == 0 or option > 5:
        break_counter = break_counter + 1
        if break_counter < 6:
            option = int(input("Option (" + str(option) + ") is not available. Enter an option between 1 to 5: "))
        else:
            print(Fore.RED + "\nYou exceeded the maximum invalid entries. Good-Bye.")
            quit()
    if option == 0 or option > 5:
        print(Fore.RED + "\nERROR: Maximum (5) tries exceeded. Next time enter an option between 1 to 5. Good-Bye.")
    if option == 1:
        check_available_rooms()
        continue_decision()
    if option == 2:
        terms_and_conditions()
        reservation()
    if option == 3:
        cancel_reservation()
    if option == 4:
        add_night_room_to_resrvation()
    if option == 5:
        quit("Thank you for using our services. Good-Bye.")


def files_creation():
    temp_directory = tempfile.gettempdir()
    hotels = open(str(temp_directory) + "/hotels.txt", "w+")
    hotels.write("{} {} {} {} {}".format("{'hotel': 'Isrotel',", "'room': 1,", "'maximum guests capacity': 2,",
                                         "'cost': " + str(random.randrange(250, 450)) + ",",
                                         "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels = open(str(temp_directory) + "/hotels.txt", "a+")
    hotels.write("\n{} {} {} {} {}".format("{'hotel': 'Isrotel',", "'room': 2,", "'maximum guests capacity': 2,",
                                           "'cost': " + str(random.randrange(250, 450)) + ",",
                                           "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels.write("\n{} {} {} {} {}".format("{'hotel': 'Isrotel',", "'room': 3,", "'maximum guests capacity': 3,",
                                           "'cost': " + str(random.randrange(300, 500)) + ",",
                                           "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels.write("\n{} {} {} {} {}".format("{'hotel': 'Isrotel',", "'room': 4,", "'maximum guests capacity': 3,",
                                           "'cost': " + str(random.randrange(300, 500)) + ",",
                                           "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels.write("\n{} {} {} {} {}".format("{'hotel': 'Fattal',", "'room': 1,", "'maximum guests capacity': 2,",
                                           "'cost': " + str(random.randrange(350, 550)) + ",",
                                           "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels.write("\n{} {} {} {} {}".format("{'hotel': 'Fattal',", "'room': 2,", "'maximum guests capacity': 2,",
                                           "'cost': " + str(random.randrange(350, 550)) + ",",
                                           "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels.write("\n{} {} {} {} {}".format("{'hotel': 'Fattal',", "'room': 3,", "'maximum guests capacity': 3,",
                                           "'cost': " + str(random.randrange(350, 550)) + ",",
                                           "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels.write("\n{} {} {} {} {}".format("{'hotel': 'Fattal',", "'room': 4,", "'maximum guests capacity': 3,",
                                           "'cost': " + str(random.randrange(350, 550)) + ",",
                                           "'day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']}"))
    hotels.close()

    reservation = open(str(temp_directory) + "/reservation.txt", "w+")
    reservation.close()


def check_available_rooms():
    print(Style.BRIGHT + "\nAvailable Rooms:")
    temp_directory = tempfile.gettempdir()
    for line in open(str(temp_directory) + "/hotels.txt", "r").readlines():
        hotels = line.replace("'", "\"")
        hotels = json.loads(hotels)
        print(Fore.LIGHTBLUE_EX + str(hotels).replace("{", "").replace("}", "").replace("'", "").title())


def sleep_loading(x):
    for i in range(x):
        print('.' * 5, end='')
        sleep(1)
    print("\n")


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
    finish = int(input(
        Style.BRIGHT + "\nEnter (" + Fore.GREEN + "1" + Fore.BLACK + ") to purchase and reserve the cheapest room\nEnter (" + Fore.RED + "2" + Fore.BLACK + ") to withdraw the reservation\n\nPlease enter your decision: "))
    while finish != 1 and finish != 2:
        finish = int(input(str(finish) + " is not a valid option. Please enter 1 or 2: "))
    if finish == 1:
        print(
            Style.BRIGHT + "\n>>> Thank you for choosing our hotels network. We wish you the finest vacation. Please wait few seconds while we handle your reservation...")
        sleep_loading(x=5)
    if finish == 2:
        quit("Thank you for using our services. Good-Bye.")
    return finish


def select_arrival_day(nights):
    if nights == 1:
        arrival_day = input(
            "[Please choose day of arrival between Sunday and Wednesday]: ").lower()
    if nights == 2:
        arrival_day = input(
            "[Please choose day of arrival between Sunday and Tuesday]: ").lower()
    if nights == 3:
        arrival_day = input(
            "[Please choose day of arrival between Sunday and Monday]: ").lower()
    if nights == 4:
        arrival_day = "sunday"
        print("Sunday was selected automatically as the arrival day. The hotels rooms are available from Sunday to "
              "Thursday. The only option to fulfill 4 nights is by arriving on Sunday")
    while arrival_day != "sunday" and arrival_day != "monday" and arrival_day != "tuesday" and arrival_day != "wednesday" and arrival_day != "thursday" and arrival_day != "friday" and arrival_day != "saturday":
        arrival_day = input(Fore.RED + str(arrival_day) + " is not a valid day. Enter day of arrival: ").lower()
    if arrival_day == "friday":
        quit("We do not offer rooms in Friday. Good-Bye.")
    if arrival_day == "saturday":
        quit("We do not offer rooms in Saturday. Good-Bye.")
    arrival_day = arrival_day.title()
    return arrival_day


def select_departure_day(arrival_day, nights):
    x = arrival_day.lower()
    if x == "sunday":
        if nights == 1:
            departure_day = "Monday"
            print("You have chosen to stay 1 night from " + str(arrival_day).title() + " till " + str(departure_day))
        if nights == 2:
            departure_day = "Tuesday"
            print("You have chosen to stay 2 nights from " + str(arrival_day).title() + " till " + str(departure_day))
        if nights == 3:
            departure_day = "Wednesday"
            print("You have chosen to stay 3 nights from " + str(arrival_day).title() + " till " + str(departure_day))
        if nights == 4:
            departure_day = "Thursday"
            print("You have chosen to stay 4 nights from " + str(arrival_day).title() + " till " + str(departure_day))
        if nights > 4:
            quit("Apologies, we offer maximum of " + str(nights) + " nights from" + str(arrival_day) + ". Good-Bye.")
    if x == "monday":
        if nights == 1:
            departure_day = "Tuesday"
            print("You have chosen to stay 1 night from " + str(arrival_day).title() + " till " + str(departure_day))
        if nights == 2:
            departure_day = "Wednesday"
            print("You have chosen to stay 2 nights from " + str(arrival_day).title() + " till " + str(departure_day))
        if nights == 3:
            departure_day = "Thursday"
            print("You have chosen to stay 3 nights from " + str(arrival_day).title() + " till " + str(departure_day))
        if nights > 3:
            quit("Apologies, we offer maximum of " + str(nights) + " nights from" + str(arrival_day) + ". Good-Bye.")
    if x == "tuesday":
        if nights == 1:
            departure_day = "Wednesday"
            print("You have chosen to stay 1 night from " + str(arrival_day).title() + " till " + str(departure_day))
        if nights == 2:
            departure_day = "Thursday"
            print("You have chosen to stay 2 nights from " + str(arrival_day).title() + " till " + str(departure_day))
        if nights > 2:
            quit("Apologies, we offer maximum of " + str(nights) + " nights from" + str(arrival_day) + ". Good-Bye.")
    if x == "wednesday":
        if nights == 1:
            departure_day = "Thursday"
            print("You have chosen to stay 1 night from " + str(arrival_day).title() + " till " + str(departure_day))
        if nights > 1:
            quit("Apologies, we can only offer 1 night from " + str(arrival_day) + ". Good-Bye.")
    if x == "thursday":
        quit("you have chosen to arrive at " + str(arrival_day).title() + " and stay for " + str(
            nights) + " nights. Sadly, " + str(
            arrival_day).title() + " can't be booked since all our hotels are out-of-service in Friday and Saturday")
    arrival_day = arrival_day.lower()
    departure_day = departure_day.title()
    temp_directory = tempfile.gettempdir()
    with open(str(temp_directory) + "/hotels.txt") as f:
        line = f.readline()
        line = line.replace("'", "\"")
        line = json.loads(line)
        index_arrival_day = line['day'].index(str(arrival_day).title())
        index_departure_day = line['day'].index(str(departure_day).title())
        departure_minus_arrival_nights_count = index_departure_day - index_arrival_day
        days_list = str(line['day'][index_arrival_day:index_departure_day + 1])
        days_list = days_list.replace("[", "").replace("]", "")
        if index_arrival_day >= index_departure_day:
            quit("You have requested to arrive on " + str(arrival_day).title() + " and depart on " +
                 str(departure_day).title() + ". This is impossible due to the fact that " + str(arrival_day).title() +
                 " comes after " + str(
                departure_day).title() + " and we aren't in the time traveling business. Good-Bye.")
        if departure_minus_arrival_nights_count < nights:
            quit("You have requested to arrive on " + str(arrival_day).title() + " and depart on " +
                 str(departure_day).title() + " which are " + str(departure_minus_arrival_nights_count) +
                 " nights and less than your initial request to stay " + str(nights) + " nights. Good-Bye.")
        if departure_minus_arrival_nights_count > nights:
            quit("You have requested to arrive on " + str(arrival_day).title() + " and depart on " +
                 str(departure_day).title() + " which are " + str(departure_minus_arrival_nights_count) +
                 " nights and more than your initial request to stay " + str(nights) + " nights. Good-Bye.")
    return days_list


def continue_decision():
    continue_decision = int(input(
        "\n- Enter (1) to continue with the rooms reservation process\n- Enter (2) to quit\n\nPlease enter your decision: "))
    while continue_decision != 1 and continue_decision != 2:
        continue_decision = int(input(str(continue_decision) + " is not a valid option. Please enter 1 or 2: "))
    if continue_decision == 1:
        print("Please wait few seconds while we redirect you to the reservations interface...\n")
        sleep_loading(x=3)
        print("<<< Welcome to our reservations interface >>>")
        reservation()
    if continue_decision == 2:
        quit("Thank you for using our services. Good-Bye.")


def terms_and_conditions():
    print(Fore.RED + Style.BRIGHT + "\n  Terms, Conditions and Information\n  " + str("-" * 33) +
          Fore.LIGHTBLACK_EX + "\n- The only available rooms are from August 2 till August 6 2020 (Sunday till Thursday).\n- We offer rooms for 2 guests or 3 guests.\n"
                               "- All prices are in USD.\n- Breakfast can be included for an extra fee per night.")
    terms = int(input(
        "\n- Enter (" + Fore.GREEN + "1" + Fore.BLACK + ") if you accept the terms and conditions: \n- Enter (" + Fore.RED + "2" + Fore.BLACK + ") if you refuse the terms and"
                                                                                                                                                " conditions: "))
    while terms != 1 and terms != 2:
        terms = int(input(
            Fore.LIGHTRED_EX + "  (" + str(terms) + ") In not a valid option. Please enter a number between 1 and 2: "))
    if terms == 1:
        print(Style.BRIGHT + "\n<<<<<  You have accepted our terms and conditions. Please continue with the reservation"
                             " process. >>>>>\n")
    if terms == 2:
        agree = input(
            "\n  We apologise that you refused our terms and conditions. Can we get a manager to discuss our terms and"
            " conditions with you?" + Style.BRIGHT + " [Yes/No]" + Style.NORMAL + ": ").lower()
        while agree != "yes" and agree != "no":
            agree = input(Fore.LIGHTRED_EX + "  (" + str(
                agree) + ") In not a valid option. Please enter" + Style.BRIGHT + " [Yes/No]" + Style.NORMAL + ": ").lower()
        if agree == "yes":
            print(Fore.LIGHTBLUE_EX + "Please wait few seconds until we reach the hotels manager...")
            sleep_loading(x=10)
            quit("We are sorry, the manager is sick today and can't be reached. Good-bye.")
        else:
            quit("Thank you for using our services. Good-Bye.")


def presentation(a, b, c, d, e, f, g):
    if e == "yes":
        e = "The deal includes breakfast"
    if e == "no":
        e = "The deal does not includes breakfast"
    print(Style.BRIGHT + Fore.LIGHTBLUE_EX + "\nDear " + str(g) + ", you have searched for " + str(
        f) + " room(s) in " + str(d) + " for " + str(
        a) + " guests over " + str(c) + " night(s) (" + str(b).replace("'", "") + "). " + str(e))
    reservation_validation = input("[The above reservation details are correct? Enter (Yes/No)]: ").lower()
    if reservation_validation == "yes":
        print(
            Style.BRIGHT + "Searching for the cheapest rooms by your demands. The rooms prices are final.")
        # sleep_loading(x=10)
    if reservation_validation == "no":
        print("Please wait few seconds while restarting the reservation process...")
        sleep_loading(x=5)
        reservation()


def available_rooms_empty_file_creation():
    temp_directory = tempfile.gettempdir()
    available_rooms = open(str(temp_directory) + "/available_rooms.txt", "w+")
    available_rooms.write("")
    available_rooms.close()
    available_rooms = open(str(temp_directory) + "/available_rooms_isrotel.txt", "w+")
    available_rooms.write("")
    available_rooms.close()
    available_rooms = open(str(temp_directory) + "/available_rooms_fattal.txt", "w+")
    available_rooms.write("")
    available_rooms.close()


def reservation():
    # global hotels
    breakfast_price = 20
    temp_directory = tempfile.gettempdir()
    nights_counter = 0
    costs = []
    costs_fattal = []
    costs_isrotel = []
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

    arrival_day = select_arrival_day(nights)
    days_list = select_departure_day(arrival_day, nights)
    departure_day = list(days_list.split(","))
    departure_day = departure_day[-1].replace("'","").replace(" ","")

    rooms = int(input("[Please enter how many rooms you wish to reserve]: "))
    if rooms > guests:
        quit("The number of requested rooms (" + str(rooms) + ") can't be higher than the number of guests (" +
             str(guests) + "). This is a strict policy in our hotels network.")

    with open(str(temp_directory) + "/hotels.txt") as f:
        available_rooms_lines_count = len(f.readlines())
        if available_rooms_lines_count < rooms:
            quit("You have requested " + str(rooms) + " room(s). There are only " + str(available_rooms_lines_count) +
                 " room(s) available matching the requested " + str(nights) + " nights")

    guests_per_room = guests / rooms
    if guests_per_room > 3.0:
        quit(
            "To allocate " + str(guests) + " guests within " + str(rooms) + " room(s) means that we have to disperse " +
            "more than 3 guests per room while our biggest room can only accommodate maximum of 3 guests.")

    hotels_preferation = int(input(
        "[Please select on which hotels to reserve the room(s)]:\n- Enter (1) for 'Fattal'\n- Enter (2) for 'Isrotel'"
        "\n- Enter (3) for both 'Fattal' and 'Isrotel'\nEnter your selection: ").lower())
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
        quit("You have requested " + str(
            rooms) + " room(s). The maximum number of rooms in both Fattal and Isrotel is 8")

    breakfast = input("[You wish to include breakfast in exchange for an extra " + str(
        breakfast_price) + "$ per night?. Enter (Yes/No)]: ").lower()
    while breakfast != "yes" and breakfast != "no":
        breakfast = input(Fore.RED + "[Please enter 'Yes' or 'No']: ").lower()

    available_rooms_empty_file_creation()

    for line in open(str(temp_directory) + "/hotels.txt", "r").readlines():
        hotels = line.replace("'", "\"")
        hotels = json.loads(hotels)
        available_rooms = open(str(temp_directory) + "/available_rooms.txt", "a+")
        if int(len(list(hotels.values())[4])) > nights:
            if breakfast == "yes":
                hotels['cost'] = hotels['cost'] + breakfast_price * nights
            if breakfast == "no":
                hotels['cost'] = hotels['cost']
            available_rooms.write("{}\n".format(str(hotels)))
            costs.append(list(hotels.values())[3])
            costs = sorted(costs)
        available_rooms.close()

    for line in open(str(temp_directory) + "/available_rooms.txt", "r").readlines():
        hotels = line.replace("'", "\"")
        hotels = json.loads(hotels)
        available_rooms_fattal = open(str(temp_directory) + "/available_rooms_fattal.txt", "a+")
        if breakfast == "yes":
            hotels['cost'] = hotels['cost'] + breakfast_price * nights
        if breakfast == "no":
            hotels['cost'] = hotels['cost']
        if re.search("Fattal", str(hotels)):
            available_rooms_fattal.write("{}\n".format(str(hotels)))
            costs_fattal.append(list(hotels.values())[3])
            costs_fattal = sorted(costs_fattal)
        available_rooms_fattal.close()

    for line in open(str(temp_directory) + "/available_rooms.txt", "r").readlines():
        hotels = line.replace("'", "\"")
        hotels = json.loads(hotels)
        available_rooms_isrotel = open(str(temp_directory) + "/available_rooms_isrotel.txt", "a+")
        if breakfast == "yes":
            hotels['cost'] = hotels['cost'] + breakfast_price * nights
        if breakfast == "no":
            hotels['cost'] = hotels['cost']
        if re.search("Isrotel", str(hotels)):
            available_rooms_isrotel.write("{}\n".format(str(hotels)))
            costs_isrotel.append(list(hotels.values())[3])
            costs_isrotel = sorted(costs_isrotel)
        available_rooms_isrotel.close()

    full_name = input("Please Enter your full name: ")
    identification_number = int(input("Please Enter your identification number: "))
    phone_number = int(input("Please Enter your phone number (e.g. 0501223334): "))

    presentation(guests, days_list, nights, hotel_name, breakfast, rooms, full_name)

    for i in range(4):
        if hotels_preferation == 1:
            for line in open(str(temp_directory) + "/available_rooms_fattal.txt", "r").readlines():
                available_rooms_fattal = line.replace("'", "\"")
                available_rooms_fattal = json.loads(available_rooms_fattal)
                if re.search("Fattal", str(available_rooms_fattal)):
                    if re.search(str(costs_fattal[i]), str(available_rooms_fattal)):
                        if re.search(str(days_list), str(available_rooms_fattal)):
                            reservation_file = open(str(temp_directory) + "/reservation.txt", "a+")
                            if i < rooms:
                                reservation_file.write(str("Full Name: " + str(full_name) + ", ID number: " + str(
                                    identification_number) + ", Phone Number: " + str(phone_number) + ", Hotel: " +
                                                           available_rooms_fattal['hotel'] + ", Room: " + str(
                                    available_rooms_fattal['room']) + ", Nights: " + str(
                                    nights) + ", Breakfast: " + str(breakfast) + ", Price: " + str(
                                    available_rooms_fattal['cost'] * nights + breakfast_price * nights) + "$\n"))
                                print(Fore.LIGHTBLUE_EX + "Room: " + str(available_rooms_fattal['room']) + ", Hotel: " +
                                      available_rooms_fattal['hotel'] + ", Nights: " + str(
                                    nights) + ", Price: " + str(
                                    available_rooms_fattal['cost'] * nights + breakfast_price * nights) + "$")
        if hotels_preferation == 2:
            for line in open(str(temp_directory) + "/available_rooms_isrotel.txt", "r").readlines():
                available_rooms_isrotel = line.replace("'", "\"")
                available_rooms_isrotel = json.loads(available_rooms_isrotel)
                if re.search("Isrotel", str(available_rooms_isrotel)):
                    if re.search(str(costs_isrotel[i]), str(available_rooms_isrotel)):
                        if re.search(str(days_list), str(available_rooms_isrotel)):
                            reservation_file = open(str(temp_directory) + "/reservation.txt", "a+")
                            if i < rooms:
                                reservation_file.write(str("Full Name: " + str(full_name) + ", ID number: " + str(
                                    identification_number) + ", Phone Number: " + str(phone_number) + ", Hotel: " +
                                                           available_rooms_isrotel['hotel'] + ", Room: " + str(
                                    available_rooms_isrotel['room']) + ", Nights: " + str(
                                    nights) + ", Breakfast: " + str(breakfast) + ", Price: " + str(
                                    available_rooms_isrotel['cost'] * nights + breakfast_price * nights) + "$\n"))
                                print(
                                    Fore.LIGHTBLUE_EX + "Room: " + str(available_rooms_isrotel['room']) + ", Hotel: " +
                                    available_rooms_isrotel['hotel'] + ", Nights: " + str(
                                        nights) + ", Price: " + str(
                                        available_rooms_isrotel['cost'] * nights + breakfast_price * nights) + "$")
    for i in range(8):
        if hotels_preferation == 3:
            for line in open(str(temp_directory) + "/available_rooms.txt", "r").readlines():
                available_rooms = line.replace("'", "\"")
                available_rooms = json.loads(available_rooms)
                if re.search(str(costs[i]), str(available_rooms)):
                    if re.search(str(days_list), str(available_rooms)):
                        reservation_file = open(str(temp_directory) + "/reservation.txt", "a+")
                        if i < rooms:
                            reservation_file.write(str("Full Name: " + str(full_name) + ", ID number: " + str(
                                identification_number) + ", Phone Number: " + str(phone_number) + ", Hotel: " +
                                                       available_rooms['hotel'] + ", Room: " + str(
                                available_rooms['room']) + ", Nights: " + str(
                                nights) + ", Breakfast: " + str(breakfast) + ", Price: " + str(
                                available_rooms['cost'] * nights + breakfast_price * nights) + "$\n"))
                            print(Fore.LIGHTBLUE_EX + "Room: " + str(available_rooms['room']) + ", Hotel: " +
                                  available_rooms['hotel'] + ", Nights: " + str(
                                nights) + ", Price: " + str(
                                available_rooms['cost'] * nights + breakfast_price * nights) + "$")

    delete_reservation_from_main_hotels_file(arrival_day, departure_day, hotel_name, rooms)


def delete_reservation_from_main_hotels_file(a,b,c,d):
    temp_directory = tempfile.gettempdir()
    for line in open(str(temp_directory) + "/hotels.txt", "r").readlines():
        hotels = line.replace("'", "\"")
        hotels = json.loads(hotels)
        index_arrival_day = hotels['day'].index(str(a).title())
        index_departure_day = hotels['day'].index(str(b).title())
        if c == "Isrotel" or c == "Fattal":
            if re.search(str(c), str(hotels)):
                if re.search(str(d), str(hotels)):
                    del hotels['day'][index_arrival_day:index_departure_day]
                    print(hotels)
        else:
            del hotels['day'][index_arrival_day:index_departure_day]
            print(hotels)

    # finish = decision()
    # if finish == 1:
    #     reservation = open(str(temp_directory) + "/reservation.txt", "r+")


# def cancel_reservation():


files_creation()
welcome()
menu()

# reservation file is not deleted but can change when adding/removong reservations
# hotels file changes and not created again once it's created.
# The filed creation only running if hotels file doesn't exist
