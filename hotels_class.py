import itertools
from time import sleep
import tempfile
import re
import random
from colorama import Fore, init, Style
import csv
import os
import pandas as pd
import json

init(autoreset=True)

temp_directory = tempfile.gettempdir()  # tempfile.gettempdir() allows to write/read a file to/from %TEMP%
rooms_csv_file = temp_directory + '/available_rooms.csv'
reservation_file = temp_directory + '/reservation.csv'
breakfast_price = 10
site_name = 'Drivago'


class Hotels:
    def __init__(self, check_in, check_out, hotel, guests, rooms, breakfast, name, phone_number, id_number,
                 credit_card_number, email):
        global selected_days_list
        selected_days_list = []
        full_dates_list = ['2.8.2020', '3.8.2020', '4.8.2020', '5.8.2020', '6.8.2020']
        full_days_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']

        available_dates_list = self.available_dates_list()
        if len(available_dates_list) == 0:
            quit("All rooms are fully booked. Please try again at another time.")
        print(Style.BRIGHT + "\nAvailable dates in august 2020:\n".title() + str(
            '-' * 30) + "\n" + Style.BRIGHT + Fore.LIGHTBLUE_EX +
              str(available_dates_list).replace("{", "").replace("}", "").replace("'", ""))

        self.check_in = input(
            '\nEnter check-in date from the following date(s) ' + str(available_dates_list[0:-1]) + ': ')
        while self.check_in not in str(available_dates_list[0:-1]):
            self.check_in = input(self.check_in + ' is not a valid check-in date. Enter a date from the following date'
                                                  '(s) ' + str(available_dates_list[0:-1]) + ': ')
        check_in_index = available_dates_list.index(self.check_in)
        for i in reversed(range(check_in_index + 1)):
            del available_dates_list[i]

        self.check_out = input(
            'Enter check-out date from the following date(s) ' + str(available_dates_list) + ': ')
        while self.check_out not in available_dates_list:
            self.check_out = input(self.check_out + ' is not a valid check-out date from the following date(s) ' + str(
                available_dates_list) + ': ')

        check_out_index = full_dates_list.index(self.check_out)

        self.hotel = int(input(Style.BRIGHT + Fore.RED +
                               "\nNote: " + Fore.BLACK + "In each hotel we can offer maximum of 4 rooms. To try and reserve"
                                                         " more than 4 rooms please enter 'isrotel and fattal'" +
                               Style.NORMAL + "\n- Enter (1) to search the cheapest available rooms in 'Isrotel'\n"
                                              "- Enter (2) to search the cheapest available rooms in 'Fattal'\n"
                                              "- Enter (3) to search the cheapest available rooms in both 'Isrotel' and"
                                              " 'Fattal'\n\nEnter your selection: "))
        while self.hotel != 1 and self.hotel != 2 and self.hotel != 3:
            self.hotel = int(input(Style.BRIGHT + str(self.hotel) + Style.NORMAL +
                                   " is not a valid input.\n- Enter (1) to search the cheapest available rooms in "
                                   "'Isrotel'\n- Enter (2) to search the cheapest available rooms in 'Fattal'\n"
                                   "- Enter (3) to search the cheapest available rooms in both 'Isrotel' and"
                                   " 'Fattal'\n\nEnter your selection: "))
        if self.hotel == 1:
            self.hotel = "isrotel"
        if self.hotel == 2:
            self.hotel = "fattal"
        if self.hotel == 3:
            self.hotel = "isrotel and fattal"
        print("\nYou have choose to search for available rooms in " + Style.BRIGHT + Fore.MAGENTA +
              str(self.hotel).title())

        available_guests_per_day = self.available_guests_per_day(self)

        if min_guests_value < 1:
            quit("\nNo available rooms in " + str(self.hotel) + " to host more guests. Please try again later or try "
                                                                "another hotel.")

        print(Style.BRIGHT + "\n\tNumber of people we can accommodate per day in " + str(
            self.hotel).title() + ":\n\t" + Fore.LIGHTBLUE_EX + Style.NORMAL +
              str(available_guests_per_day).title().replace("{", "").replace("}", "").replace("'", "") + Fore.BLACK +
              "\n\tThe maximum guests to accommodate between " + str(
            self.check_in) + " and " + str(self.check_out) + " is: " + Style.BRIGHT + Fore.RED + str(min_guests_value))

        self.guests = int(input('\nEnter how many people are you coming?: '))
        while self.guests > min_guests_value:
            self.guests = int(input("You have requested to accommodate " +
                                    str(self.guests) + " guests while we have available rooms for " + Fore.RED +
                                    str(min_guests_value) + Fore.BLACK + " or less guests. Please enter an acceptable "
                                                                         "number of guests: "))
        while self.guests < 1:
            self.guests = int(input("The number of guests cannot be lower than 1. Please enter an acceptable number "
                                    "of guests:"))

        selected_days_index_list = list(range(check_in_index, check_out_index + 1))

        for n in selected_days_index_list:
            selected_days_list.append(full_dates_list[n])
            while list(available_guests_per_day.values())[n] < self.guests:
                self.guests = int(input("On " + full_days_list[n] + " (" + full_dates_list[n] +
                                        ") we can only accommodate maximum of " + str(
                    list(available_guests_per_day.values())[n]) +
                                        " guests while you requested to host " + str(self.guests) +
                                        " guests.\nPlease change the amount of guests accordingly.\n"
                                        "Enter new number of guests: "))

        available_rooms_per_day = self.available_rooms_per_day(self)
        print(Style.BRIGHT + "\n\tNumber of available rooms per day in " + str(
            self.hotel).title() + ":\n\t" + Style.NORMAL + Fore.LIGHTBLUE_EX +
              str(available_rooms_per_day).title().replace("{", "").replace("}", "").replace("'", "") + Fore.BLACK +
              "\n\tThe maximum number of rooms that are available for you between " + str(
            self.check_in) + " and " + str(self.check_out) + " is: " + Style.BRIGHT + Fore.RED + str(min_rooms_value))

        self.rooms = int(input('\nEnter how many rooms you wish to reserve: '))
        while self.rooms > self.guests:
            self.guests = int(input("You requested " + str(self.rooms) + " rooms for " + str(self.guests) +
                                    " guests. Our policy claims that we can't provide more than 1 room to a single"
                                    " person.\nPlease enter number of rooms no higher than " + str(self.guests) + ": "))
        while self.rooms > min_rooms_value:
            self.rooms = int(input("We currently have " + str(min_rooms_value) + " available rooms while you requested "
                                   + str(self.rooms) + " rooms.\nPlease enter number of rooms that is equal or lower "
                                   + str(min_rooms_value) + " to : "))
        while self.rooms < 1:
            self.rooms = int(input("The number of rooms cannot be lower than 1. Please enter an acceptable number of "
                                   "rooms:"))
        while (self.guests / self.rooms) > 3:
            self.rooms = int(input("Can't have more than 3 people in 1 room. You will need to reserve more rooms. "
                                   "Please enter how many rooms you wish to reserve: "))

        for n in selected_days_index_list:
            while list(available_rooms_per_day.values())[n] < self.rooms:
                self.rooms = int(input("We offer " + str(list(available_rooms_per_day.values())[n]) +
                                       " rooms on " + full_days_list[n] + " (" + full_dates_list[n] + ") in " +
                                       str(self.hotel).title() + " while you requested " + str(self.guests) +
                                       " rooms.\nPlease change the amount of rooms accordingly.\n"
                                       "Enter new number of rooms: "))

        self.breakfast = input("You wish to include breakfast in exchange for an extra " + str(
            breakfast_price) + "$ a night for each room?. Enter" + Style.BRIGHT + " (Yes/No)" +
                               Style.NORMAL + ": ").lower()
        while self.breakfast != "yes" and self.breakfast != "no":
            self.breakfast = input(
                self.breakfast + " is not a valid input.\nPlease enter" + Style.BRIGHT + " (Yes/No)" +
                Style.NORMAL + ": ").lower()

        self.cheapest_rooms(self)

        self.accept_reject(self)

        self.name = input('Enter your Full Name: ')

        self.phone_number = input('Enter Phone Number: ')
        while len(str(self.phone_number)) != 10:
            self.phone_number = input("The phone number is expected to have 10 digits."
                                      " Please enter phone number (e.g. 0501234567): ")

        self.id_number = input('Enter Identification Number: ')
        while len(str(self.id_number)) != 9:
            self.id_number = input("The ID number is expected to be 9 digits. "
                                   "Please enter another phone number (e.g. 039954263): ")

        self.credit_card_number = input('Enter Credit Card Number: ')
        while len(str(self.credit_card_number)) < 16 or len(str(self.credit_card_number)) > 19:
            self.credit_card_number = input("The Credit Card number is expected to be between 16 and 19 digits."
                                            " Please enter a valid Credit Card number (e.g. 1234567890123456): ")

        self.email = input('Enter Email Address: ')
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if not re.search(regex, self.email):
            self.email = input(str(self.email) + " is not a valid Email address."
                               " Please enter a valid Email address (e.g. myname@gmail.co.il): ")

        self.order_acceptance(self)

    @staticmethod
    def loading(sec):
        for i in range(sec):
            print('.' * 10, end='')
            sleep(1)
        print("\n")

    @staticmethod
    def accept_reject(self):
        accept_reject = int(input(Style.BRIGHT + "\nWe are about to ask you for personal details." + Style.NORMAL +
                                  "\n- Enter (1) to accept and continue\n- Enter (2) to quit " + str(site_name) +
                                  "\n\nEnter your selection: "))
        while 2 < accept_reject < 1:
            accept_reject = int(input(Fore.LIGHTRED_EX + str(
                accept_reject) + "is not a valid input.\n- Enter (1) to accept and continue\n"
                                 "- Enter (2) to quit " + str(site_name) + "\n\n"
                                                                           "Enter your selection: "))
        if accept_reject == 2:
            quit("Thank you for using" + str(site_name) + ". Good-Bye.")

    @staticmethod
    def available_dates_list():
        sunday = 0
        monday = 0
        tuesday = 0
        wednesday = 0
        thursday = 0
        available_dates_list = []
        with open(rooms_csv_file, 'r') as f:
            file = csv.reader(f)
            i = next(file)
            for row in file:
                if 'available' in row[4]:
                    sunday = sunday + 1
                    if sunday > 0:
                        sunday_date = i[4]
                    available_dates_list.append(sunday_date)
                if 'available' in row[5]:
                    monday = monday + 1
                    if monday > 0:
                        monday_date = i[5]
                    available_dates_list.append(monday_date)
                if 'available' in row[6]:
                    tuesday = tuesday + 1
                    if tuesday > 0:
                        tuesday_date = i[6]
                    available_dates_list.append(tuesday_date)
                if 'available' in row[7]:
                    wednesday = wednesday + 1
                    if wednesday > 0:
                        wednesday_date = i[7]
                    available_dates_list.append(wednesday_date)
                if 'available' in row[8]:
                    thursday = thursday + 1
                    if thursday > 0:
                        thursday_date = i[8]
                    available_dates_list.append(thursday_date)
            available_dates_list = sorted(set(available_dates_list))
            return available_dates_list

    @staticmethod
    def rooms_file_write():
        # using the library os.path can check if a file exist or not
        if os.path.isfile(rooms_csv_file):
            # if entered the if condition, the file exists
            print(str(rooms_csv_file) + ' already exists')
            pass
        else:
            # if entered the else condition the file does not exists and will be created
            with open(rooms_csv_file, 'w', newline='') as csvfile:
                file = csv.DictWriter(csvfile,
                                      fieldnames=['Hotel', 'Room', 'Guests', 'Price', '2.8.2020', '3.8.2020',
                                                  '4.8.2020',
                                                  '5.8.2020', '6.8.2020'])
                file.writeheader()
                file.writerow({'Hotel': 'Isrotel', 'Room': 1, 'Guests': 2, 'Price': random.randrange(250, 450),
                               '2.8.2020': 'available', '3.8.2020': 'available', '4.8.2020': 'available',
                               '5.8.2020': 'available', '6.8.2020': 'available'})
                file.writerow({'Hotel': 'Isrotel', 'Room': 2, 'Guests': 2, 'Price': random.randrange(250, 450),
                               '2.8.2020': 'available', '3.8.2020': 'available', '4.8.2020': 'available',
                               '5.8.2020': 'available', '6.8.2020': 'available'})
                file.writerow({'Hotel': 'Isrotel', 'Room': 3, 'Guests': 3, 'Price': random.randrange(300, 500),
                               '2.8.2020': 'available', '3.8.2020': 'available', '4.8.2020': 'available',
                               '5.8.2020': 'available', '6.8.2020': 'available'})
                file.writerow({'Hotel': 'Isrotel', 'Room': 4, 'Guests': 3, 'Price': random.randrange(300, 500),
                               '2.8.2020': 'available', '3.8.2020': 'available', '4.8.2020': 'available',
                               '5.8.2020': 'available', '6.8.2020': 'available'})
                file.writerow({'Hotel': 'Fattal', 'Room': 1, 'Guests': 2, 'Price': random.randrange(350, 550),
                               '2.8.2020': 'available', '3.8.2020': 'available', '4.8.2020': 'available',
                               '5.8.2020': 'available', '6.8.2020': 'available'})
                file.writerow({'Hotel': 'Fattal', 'Room': 2, 'Guests': 2, 'Price': random.randrange(350, 550),
                               '2.8.2020': 'available', '3.8.2020': 'available', '4.8.2020': 'available',
                               '5.8.2020': 'available', '6.8.2020': 'available'})
                file.writerow({'Hotel': 'Fattal', 'Room': 3, 'Guests': 3, 'Price': random.randrange(400, 600),
                               '2.8.2020': 'available', '3.8.2020': 'available', '4.8.2020': 'available',
                               '5.8.2020': 'available', '6.8.2020': 'available'})
                file.writerow({'Hotel': 'Fattal', 'Room': 4, 'Guests': 3, 'Price': random.randrange(400, 600),
                               '2.8.2020': 'available', '3.8.2020': 'available', '4.8.2020': 'available',
                               '5.8.2020': 'available', '6.8.2020': 'available'})
                print(str(rooms_csv_file) + ' created')

        if os.path.isfile(reservation_file):
            # if entered the if condition, the file exists
            print(str(reservation_file) + ' already exists')
            pass
        else:
            with open(reservation_file, 'w', newline='') as csvfile:
                file = csv.DictWriter(csvfile,
                                      fieldnames=['Name', 'Phone', 'ID', 'Credit Card',
                                                  'Check In', 'Check Out', 'Hotel', 'Room',
                                                  'Price', 'Reservation ID', 'Email'])
                file.writeheader()
                print(str(reservation_file) + ' created')

    @staticmethod
    def available_rooms_per_day(self):
        global min_rooms_value
        sunday = 0
        monday = 0
        tuesday = 0
        wednesday = 0
        thursday = 0
        days_rooms_dict = {'sunday': 0, 'monday': 0, 'tuesday': 0, 'wednesday': 0, 'thursday': 0, }
        with open(rooms_csv_file, 'r') as f:
            file = csv.reader(f)
            next(file)
            for row in file:
                if self.hotel == 'isrotel':
                    if 'available' in row[4] and 'Isrotel' in row[0]:
                        sunday = sunday + 1
                if self.hotel == 'fattal':
                    if 'available' in row[4] and 'Fattal' in row[0]:
                        sunday = sunday + 1
                if self.hotel == 'isrotel and fattal':
                    if 'available' in row[4]:
                        sunday = sunday + 1

                if self.hotel == 'isrotel':
                    if 'available' in row[5] and 'Isrotel' in row[0]:
                        monday = monday + 1
                if self.hotel == 'fattal':
                    if 'available' in row[5] and 'Fattal' in row[0]:
                        monday = monday + 1
                if self.hotel == 'isrotel and fattal':
                    if 'available' in row[5]:
                        monday = monday + 1

                if self.hotel == 'isrotel':
                    if 'available' in row[6] and 'Isrotel' in row[0]:
                        tuesday = tuesday + 1
                if self.hotel == 'fattal':
                    if 'available' in row[6] and 'Fattal' in row[0]:
                        tuesday = tuesday + 1
                if self.hotel == 'isrotel and fattal':
                    if 'available' in row[6]:
                        tuesday = tuesday + 1

                if self.hotel == 'isrotel':
                    if 'available' in row[7] and 'Isrotel' in row[0]:
                        wednesday = wednesday + 1
                if self.hotel == 'fattal':
                    if 'available' in row[7] and 'Fattal' in row[0]:
                        wednesday = wednesday + 1
                if self.hotel == 'isrotel and fattal':
                    if 'available' in row[7]:
                        wednesday = wednesday + 1

                if self.hotel == 'isrotel':
                    if 'available' in row[8] and 'Isrotel' in row[0]:
                        thursday = thursday + 1
                if self.hotel == 'fattal':
                    if 'available' in row[8] and 'Fattal' in row[0]:
                        thursday = thursday + 1
                if self.hotel == 'isrotel and fattal':
                    if 'available' in row[8]:
                        thursday = thursday + 1

        days_rooms_dict['sunday'] = sunday
        days_rooms_dict['monday'] = monday
        days_rooms_dict['tuesday'] = tuesday
        days_rooms_dict['wednesday'] = wednesday
        days_rooms_dict['thursday'] = thursday
        min_rooms_value = min(days_rooms_dict.values())
        return days_rooms_dict

    @staticmethod
    def available_guests_per_day(self):
        global min_guests_value
        sunday = 0
        monday = 0
        tuesday = 0
        wednesday = 0
        thursday = 0
        days_guests_dict = {'sunday': 0, 'monday': 0, 'tuesday': 0, 'wednesday': 0, 'thursday': 0, }
        with open(rooms_csv_file, 'r') as f:
            file = csv.reader(f)
            next(file)
            for row in file:
                if self.hotel == 'isrotel':
                    if 'available' in row[4] and 'Isrotel' in row[0]:
                        sunday = sunday + int(row[2])
                if self.hotel == 'fattal':
                    if 'available' in row[4] and 'Fattal' in row[0]:
                        sunday = sunday + int(row[2])
                if self.hotel == 'isrotel and fattal':
                    if 'available' in row[4]:
                        sunday = sunday + int(row[2])

                if self.hotel == 'isrotel':
                    if 'available' in row[5] and 'Isrotel' in row[0]:
                        monday = monday + int(row[2])
                if self.hotel == 'fattal':
                    if 'available' in row[5] and 'Fattal' in row[0]:
                        monday = monday + int(row[2])
                if self.hotel == 'isrotel and fattal':
                    if 'available' in row[5]:
                        monday = monday + int(row[2])

                if self.hotel == 'isrotel':
                    if 'available' in row[6] and 'Isrotel' in row[0]:
                        tuesday = tuesday + int(row[2])
                if self.hotel == 'fattal':
                    if 'available' in row[6] and 'Fattal' in row[0]:
                        tuesday = tuesday + int(row[2])
                if self.hotel == 'isrotel and fattal':
                    if 'available' in row[6]:
                        tuesday = tuesday + int(row[2])

                if self.hotel == 'isrotel':
                    if 'available' in row[7] and 'Isrotel' in row[0]:
                        wednesday = wednesday + int(row[2])
                if self.hotel == 'fattal':
                    if 'available' in row[7] and 'Fattal' in row[0]:
                        wednesday = wednesday + int(row[2])
                if self.hotel == 'isrotel and fattal':
                    if 'available' in row[7]:
                        wednesday = wednesday + int(row[2])

                if self.hotel == 'isrotel':
                    if 'available' in row[8] and 'Isrotel' in row[0]:
                        thursday = thursday + int(row[2])
                if self.hotel == 'fattal':
                    if 'available' in row[8] and 'Fattal' in row[0]:
                        thursday = thursday + int(row[2])
                if self.hotel == 'isrotel and fattal':
                    if 'available' in row[8]:
                        thursday = thursday + int(row[2])

        days_guests_dict['sunday'] = sunday
        days_guests_dict['monday'] = monday
        days_guests_dict['tuesday'] = tuesday
        days_guests_dict['wednesday'] = wednesday
        days_guests_dict['thursday'] = thursday
        min_guests_value = min(days_guests_dict.values())
        return days_guests_dict

    @staticmethod
    def cheapest_rooms(self):
        global prices
        global room_number
        prices = []
        room_number = []
        repetition = 0
        with open(rooms_csv_file, 'r') as f:
            file = csv.reader(f)
            for row in file:
                if self.hotel == 'isrotel' or self.hotel == 'fattal':
                    if 'available' in row[4] and str(self.hotel).title() in row[0]:
                        prices.append(row[3])
                if self.hotel != 'isrotel' and self.hotel != 'fattal':
                    if 'available' in row[4]:
                        prices.append(row[3])
            prices = sorted(prices[:self.rooms])

            print("\nThe following are the cheapest " + str(
                self.rooms) + " rooms we could find in " + self.hotel.title() + ":\n" + str('-' * 64))

        for n in range(self.rooms):
            with open(rooms_csv_file, 'r') as f:
                file = csv.reader(f)
                for row in file:
                    if self.hotel == 'isrotel' or self.hotel == 'fattal':
                        if prices[n] in row[3] and 'available' in row[4] and str(self.hotel).title() in row[0]:
                            if self.breakfast == 'yes':
                                print(Fore.LIGHTBLUE_EX + "Hotel: " + row[0], " |  Room: " + row[1],
                                      " |  Room Guests Maximum Capacity: " + row[2], " |  Price: " +
                                      str(int(prices[n]) + breakfast_price) + "$")
                                room_number.append(row[1])
                            else:
                                print(Fore.LIGHTBLUE_EX + "Hotel: " + row[0], " |  Room: " + row[1],
                                      " |  Room Guests Maximum Capacity: " + row[2], " |  Price: " + prices[n] + "$")
                                room_number.append(row[1])


                    else:
                        if prices[n] in row[3] and 'available' in row[4]:
                            if self.breakfast == 'yes':
                                if repetition < self.rooms:
                                    print(Fore.LIGHTBLUE_EX + "Hotel: " + row[0], " |  Room: " + row[1],
                                          " |  Room Guests Maximum Capacity: " + row[2], " |  Price: " +
                                          str(int(prices[n]) + breakfast_price) + "$")
                                    repetition = repetition + 1
                                room_number.append(row[1])
                            else:
                                print(Fore.LIGHTBLUE_EX + "Hotel: " + row[0], " |  Room: " + row[1],
                                      " |  Room Guests Maximum Capacity: " + row[2], " |  Price: " + prices[n] + "$")
                                room_number.append(row[1])

        return prices, room_number

    @staticmethod
    def max_guests_capacity_per_day():
        f = csv.reader(open(rooms_csv_file))
        max_guests_capacity_per_day = []
        guests_capacity = 0
        n = 4
        for row in f:
            if 'available' in row[4]:
                n += 1
                x = row[2]
                try:
                    x = int(x)
                except ValueError:
                    x = 0
                guests_capacity += x
        max_guests_capacity_per_day.append(guests_capacity)

        f = csv.reader(open(rooms_csv_file))
        guests_capacity = 0
        n = 4
        for row in f:
            if 'available' in row[5]:
                n += 1
                x = row[2]
                try:
                    x = int(x)
                except ValueError:
                    x = 0
                guests_capacity += x
        max_guests_capacity_per_day.append(guests_capacity)

        f = csv.reader(open(rooms_csv_file))
        guests_capacity = 0
        n = 4
        for row in f:
            if 'available' in row[6]:
                n += 1
                x = row[2]
                try:
                    x = int(x)
                except ValueError:
                    x = 0
                guests_capacity += x
        max_guests_capacity_per_day.append(guests_capacity)

        f = csv.reader(open(rooms_csv_file))
        guests_capacity = 0
        n = 4
        for row in f:
            if 'available' in row[7]:
                n += 1
                x = row[2]
                try:
                    x = int(x)
                except ValueError:
                    x = 0
                guests_capacity += x
        max_guests_capacity_per_day.append(guests_capacity)

        f = csv.reader(open(rooms_csv_file))
        guests_capacity = 0
        n = 4
        for row in f:
            if 'available' in row[8]:
                n += 1
                x = row[2]
                try:
                    x = int(x)
                except ValueError:
                    x = 0
                guests_capacity += x
        max_guests_capacity_per_day.append(guests_capacity)
        print(max_guests_capacity_per_day)

    # def reservation():

    @staticmethod
    def order_acceptance(self):
        indexes = []
        repetition = 0
        order_acceptance = int(input(Fore.GREEN + Style.BRIGHT + "\nOrder Acceptance\n" + str(
            '-' * 16) + Fore.BLACK + Style.NORMAL + "\n- Enter (1) to finish the reservation\n"
                                                    "- Enter (2) to navigate back to the the initial reservation "
                                                    "section\n"
                                                    "\nEnter your selection: "))
        while order_acceptance != 1 and order_acceptance != 2:
            order_acceptance = int(input(Fore.LIGHTRED_EX + str(
                order_acceptance) + "is not a valid input.\n- Enter (1) to accept and continue with the reservation\n"
                                    "- Enter (2) to go back to the the initial input details section\n\n"
                                    "Enter your selection: "))
        if order_acceptance == 1:
            print("Thank you for choosing " + site_name + ". Please wait few seconds while we redirect you to the "
                                                          "reservation process")
            self.loading(sec=5)
            df = pd.read_csv(rooms_csv_file)

            if self.hotel == 'isrotel' or self.hotel == 'fattal':
                for i in range(self.rooms):
                    for row in df.itertuples():
                        if re.search("Hotel=" + "'" + self.hotel.title() + "'", str(row)):
                            if re.search("Room=" + str(room_number[i]), str(row)):
                                if re.search("Price=" + str(prices[i]), str(row)):
                                    if repetition < self.rooms:
                                        indexes.append(row[0])
                                        with open(reservation_file, 'a', newline='') as csvfile:
                                            file = csv.DictWriter(csvfile,
                                                                  fieldnames=['Name', 'Phone', 'ID', 'Credit Card',
                                                                              'Check In', 'Check Out', 'Hotel', 'Room',
                                                                              'Price', 'Reservation ID', 'Email'])
                                            file.writerow({'Name': str(self.name), 'Phone': str(self.phone_number),
                                                           'ID': str(self.id_number),
                                                           'Credit Card': str(
                                                               self.credit_card_number),
                                                           'Check In': str(self.check_in),
                                                           'Check Out': str(self.check_out),
                                                           'Hotel': str(row[1]).title(),
                                                           'Room': str(room_number[i]),
                                                           'Price': str(prices[i]),
                                                           'Reservation ID': str(
                                                               random.randint(0, 999999999999)),
                                                           'Email': str(self.email)})
                                        repetition = repetition + 1
            else:
                for i in range(self.rooms):
                    for row in df.itertuples():
                        if re.search("Room=" + str(room_number[i]), str(row)):
                            if re.search("Price=" + str(prices[i]), str(row)):
                                if repetition < self.rooms:
                                    indexes.append(row[0])
                                    with open(reservation_file, 'a', newline='') as csvfile:
                                        file = csv.DictWriter(csvfile,
                                                              fieldnames=['Name', 'Phone', 'ID', 'Credit Card',
                                                                          'Check In', 'Check Out', 'Hotel', 'Room',
                                                                          'Price', 'Reservation ID', 'Email'])
                                        file.writerow({'Name': str(self.name), 'Phone': str(self.phone_number),
                                                       'ID': str(self.id_number),
                                                       'Credit Card': str(
                                                           self.credit_card_number),
                                                       'Check In': str(self.check_in),
                                                       'Check Out': str(self.check_out),
                                                       'Hotel': str(row[1]).title(),
                                                       'Room': str(room_number[i]),
                                                       'Price': str(prices[i]),
                                                       'Reservation ID': str(
                                                           random.randint(0, 999999999999)),
                                                       'Email': str(self.email)})
                                    repetition = repetition + 1
            for index in (indexes):
                df.at[index, selected_days_list] = 'booked'
                df.to_csv(rooms_csv_file, index=False)  # index=False so index column will be added to the file which
                # could corrupt the test.
                total_cost = sum([int(i) for i in prices if type(i) == int or i.isdigit()])
                summary = {'Name': str(self.name), 'Phone': str(self.phone_number), 'ID': str(self.id_number),
                           'Credit Card': str(self.credit_card_number), 'Email': str(self.email),
                           'Check In': str(self.check_in),
                           'Check Out': str(self.check_out), 'Hotels': str(self.hotel), 'Rooms': str(self.rooms),
                           'Guests': str(self.guests), 'Price': str(total_cost) + "$"}
                print(json.dumps(summary, indent=4, sort_keys=True))

        else:
            user_input = Hotels('check_in', 'check_out', 'hotel', 'rooms', 'breakfast', 'guests', 'name', 'phone_number'
                                , 'id_number', 'credit_card_number', 'email')



