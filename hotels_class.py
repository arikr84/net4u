from time import sleep
import tempfile
import json
import re
import random
from colorama import Fore, init, Style, Cursor
import csv
import os
import datetime
import itertools

init(autoreset=True)

# tempfile.gettempdir() allows to write/read a file to/from %TEMP%
temp_directory = tempfile.gettempdir()
rooms_csv_file = temp_directory + '/available_rooms.csv'
breakfast_price = 10
site_name = 'Trivago'


class Hotels:
    def __init__(self, check_in, check_out, hotel, guests, rooms, breakfast, name, phone):
        # check_in_dates_list = ['2.8.2020', '3.8.2020', '4.8.2020', '5.8.2020']
        full_dates_list = ['2.8.2020', '3.8.2020', '4.8.2020', '5.8.2020', '6.8.2020']
        full_days_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
        available_dates_list = self.available_dates_list()
        print(Style.BRIGHT + "\nAvailable dates in august 2020:\n".title() + str(
            '-' * 30) + "\n" + Style.BRIGHT + Fore.LIGHTBLUE_EX +
              str(available_dates_list).title().replace("{", "").replace("}", "").replace("'", ""))

        self.check_in = input(
            '\nEnter check-in date from the following date(s) ' + str(available_dates_list[0:-1]) + ': ')
        while self.check_in not in str(available_dates_list[0:-1]):
            self.check_in = input(self.check_in + ' is not a valid check-in date. Enter a date from the following date'
                                                  '(s) ' + str(available_dates_list[0:-1]) + ': ')
        check_in_index = available_dates_list.index(self.check_in)
        del available_dates_list[check_in_index]

        self.check_out = input(
            'Enter check-out date from the following date(s) ' + str(available_dates_list) + ': ')
        while self.check_out not in available_dates_list:
            self.check_out = input(self.check_out + ' is not a valid check-out date from the following date(s) ' + str(
                available_dates_list) + ': ')

        check_out_index = full_dates_list.index(self.check_out)

        self.hotel = input(Style.BRIGHT + Fore.RED +
                           "\nNote: " + Fore.BLACK + "In each hotel we can offer maximum of 4 rooms. To try and reserve"
                                                     " more than 4 rooms please enter 'isrotel and fattal'" +
                           Style.NORMAL + "\n- Enter 'Isrotel' to search for the cheapest rooms in Isrotel\n"
                                          "- Enter 'Fattal' to search for the cheapest rooms in Fattal\n"
                                          "- Enter 'Isrotel and Fattal' to search for the cheapest rooms from both"
                                          " Isrotel and Fattal\n\nEnter your selection: ").lower()
        while self.hotel != 'isrotel' and self.hotel != 'fattal' and self.hotel != 'isrotel and fattal':
            self.hotel = input(Style.BRIGHT + str(self.hotel) + Style.NORMAL +
                               " is not a valid input.\n- Enter 'Isrotel' to search for the cheapest rooms in Isrotel\n"
                               "- Enter 'Fattal' to search for the cheapest rooms in Fattal\n"
                               "- Enter 'Isrotel and Fattal' to search for the cheapest rooms from both"
                               " Isrotel and Fattal\n\nEnter your selection: ").lower()

        # available_rooms_per_day = self.available_rooms_per_day(self)
        # print(Style.BRIGHT + "\n\tNumber of available rooms per day in " + str(
        #     self.hotel).title() + ":\n\t" + Style.NORMAL + Fore.LIGHTBLUE_EX +
        #       str(available_rooms_per_day).title().replace("{", "").replace("}", "").replace("'", "") + Fore.BLACK +
        #       "\n\tThe maximum number of rooms that are available for you between " + str(
        #     self.check_in) + " and " + str(self.check_out) + " is: " + Style.BRIGHT + Fore.RED + str(min_rooms_value))

        available_guests_per_day = self.available_guests_per_day()
        print(Style.BRIGHT + "\n\tNumber of people we can accommodate per day in " + str(
            self.hotel).title() + ":\n\t" + Fore.LIGHTBLUE_EX + Style.NORMAL +
              str(available_guests_per_day).title().replace("{", "").replace("}", "").replace("'", "") + Fore.BLACK +
              "\n\tThe maximum guests to accommodate between " + str(
            self.check_in) + " and " + str(self.check_out) + " is: " + Style.BRIGHT + Fore.RED + str(min_guests_value))

        self.guests = int(input('\nEnter how many people are you coming?: '))
        while self.guests > 20:
            self.guests = int(input("We can't handle more than 20 guests per day. You have requested to accommodate " +
                                    str(self.guests) + " guests. Please enter 20 or below guests: "))

        selected_days_index_list = list(range(check_in_index, check_out_index + 1))

        for n in selected_days_index_list:
            while list(available_guests_per_day.values())[n] < self.guests:
                self.guests = int(input("On " + full_days_list[n] + " (" + full_dates_list[n] +
                                        ") we can only accommodate maximum of " + str(list(available_guests_per_day.values())[n]) +
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
            self.guests = input("You requested " + str(self.rooms) + " while you are only " + str(self.guests) +
                                " guests. This is against our policy. Please select number of rooms no higher"
                                " than the number of guests ")

        for n in selected_days_index_list:
            while list(available_rooms_per_day.values())[n] < self.rooms:
                self.rooms = int(input("We offer " + str(list(available_rooms_per_day.values())[n]) +
                                       " rooms on " + full_days_list[n] + " (" + full_dates_list[n] + ") in " +
                                       str(self.hotel).title() + " while you requested " + str(self.guests) +
                                       " rooms.\nPlease change the amount of rooms accordingly.\n"
                                       "Enter new number of rooms: "))

        self.breakfast = input("You wish to include breakfast in exchange for an extra " + str(
            breakfast_price) + "$ per night? enter 'Yes' or 'No': ").lower()
        while self.breakfast != "yes" and self.breakfast != "no":
            self.breakfast = input(self.breakfast + " is not a valid input.\nPlease enter 'Yes' or 'No': ").lower()

        self.cheapest_rooms(self)

        self.order_acceptance(self)

        self.name = input('Full Name: ')
        self.phone = int(input('Phone Number: (e.g. 0501234567)'))

    @staticmethod
    def loading(sec):
        for i in range(sec):
            print('.' * 5, end='')
            sleep(1)
        print("\n")

    @staticmethod
    def available_dates_list():
        sunday = 0
        monday = 0
        tuesday = 0
        wednesday = 0
        thursday = 0
        available_days_list = []
        with open(rooms_csv_file, 'r') as f:
            file = csv.reader(f)
            i = next(file)
            for row in file:
                if 'available' in row[4]:
                    sunday = sunday + 1
                    if sunday > 0:
                        sunday_date = i[4]
                    available_days_list.append(sunday_date)
                if 'available' in row[5]:
                    monday = monday + 1
                    if monday > 0:
                        monday_date = i[5]
                    available_days_list.append(monday_date)
                if 'available' in row[6]:
                    tuesday = tuesday + 1
                    if tuesday > 0:
                        tuesday_date = i[6]
                    available_days_list.append(tuesday_date)
                if 'available' in row[7]:
                    wednesday = wednesday + 1
                    if wednesday > 0:
                        wednesday_date = i[7]
                    available_days_list.append(wednesday_date)
                if 'available' in row[8]:
                    thursday = thursday + 1
                    if thursday > 0:
                        thursday_date = i[8]
                    available_days_list.append(thursday_date)
            available_days_list = sorted(set(available_days_list))
            return available_days_list

    @staticmethod
    def rooms_file_write():
        # using the library os.path can check if a file exist or not
        if os.path.isfile(rooms_csv_file):
            # if entered the if condition, the file exists
            print(temp_directory + '/available_rooms.csv already exists')
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

                print(temp_directory + '/available_rooms.csv created')

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
    def available_guests_per_day():
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
                if 'available' in row[4]:
                    sunday = sunday + int(row[2])
                if 'available' in row[5]:
                    monday = monday + int(row[2])
                if 'available' in row[6]:
                    tuesday = tuesday + int(row[2])
                if 'available' in row[7]:
                    wednesday = wednesday + int(row[2])
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
        prices = []
        with open(rooms_csv_file, 'r') as f:
            file = csv.reader(f)
            for row in file:
                if 'available' in row[4]:
                    prices.append(row[3])
            prices = sorted(prices)
        for n in range(self.rooms):
            with open(rooms_csv_file, 'r') as f:
                file = csv.reader(f)
                i = next(file)
                for row in file:
                    if prices[n] in row[3] and 'available' in row[4]:
                        if self.breakfast == 'yes':
                            print(i[4] + "  |  Hotel: " + row[0], " |  Room: " + row[1],
                                  " |  Maximum guests allowed: " + row[2], " |  Price: " + str(int(prices[n]) +
                                                                                               breakfast_price) + "$")
                        else:
                            print(i[4] + "  |  Hotel: " + row[0], " |  Room: " + row[1],
                                  " |  Maximum guests allowed: " + row[2], " |  Price: " + prices[n] + "$")

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

    @staticmethod
    def order_acceptance(self):
        order_acceptance = int(input(Fore.GREEN + Style.BRIGHT + "\nOrder Acceptance\n" + str(
            '-' * 16) + Fore.BLACK + Style.NORMAL + "\n- Enter (1) to accept and continue with the reservation\n- Enter (2) to go back to the the initial input details section\n\nEnter your selection: " + Style.NORMAL + ": ").lower())
        while order_acceptance != 1 and order_acceptance != 2:
            order_acceptance = int(input(Fore.LIGHTRED_EX + str(
                order_acceptance) + "is not a valid input.\n- Enter (1) to accept and continue with the reservation\n"
                                    "- Enter (2) to go back to the the initial input details section\n\n"
                                    "Enter your selection: " + Style.NORMAL + ": ").lower())
        if order_acceptance == 1:
            print("Thank you for choosing " + site_name + ". Please wait few seconds while we redirect you to the "
                                                          "reservation process")
            self.loading(sec=10)
        else:
            user_input = Hotels('check_in', 'check_out', 'hotel', 'rooms', 'breakfast', 'guests', 'name', 'phone')
