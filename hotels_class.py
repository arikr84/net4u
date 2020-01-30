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


class Hotels:
    def __init__(self, check_in, check_out, guests, rooms, name, phone):
        check_in_dates_list = ['2.8.2020', '3.8.2020', '4.8.2020', '5.8.2020']
        full_dates_list = ['2.8.2020', '3.8.2020', '4.8.2020', '5.8.2020', '6.8.2020']
        full_days_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
        available_guests_per_day = self.available_guests_per_day()
        print("Guests allocation mapping per day\n".title() + str('-' * 33) + "\n0 == No more spots to host a "
              "guest\n20 == all the spots are available\n".title() + Style.BRIGHT + Fore.LIGHTBLUE_EX +
              str(available_guests_per_day).title().replace("{","").replace("}","").replace("'",""))
        available_rooms_per_day = self.available_rooms_per_day()
        print("\nRooms allocation mapping per day. 8 rooms is the maximum available rooms per day. \n".title() +
              str(available_rooms_per_day).title())
        self.check_in = input(
            '\nEnter check-in date from the following date(s) ' + str(check_in_dates_list) + ' (e.g. 2.8.2020): ')
        while self.check_in not in ['2.8.2020', '3.8.2020', '4.8.2020', '5.8.2020']:
            self.check_in = input(self.check_in + ' is not a valid check-in date. Enter a date between '
                                                  '2.8.2020 and 5.8.2020 (e.g. 2.8.2020): ')
        check_in_index = full_dates_list.index(self.check_in) + 1
        del check_in_dates_list[0:check_in_index]
        check_in_dates_list.append('6.8.2020')
        self.check_out = input(
            'Enter check-out date from the following date(s) ' + str(check_in_dates_list) + ' (e.g. 6.8.2020): ')
        while self.check_out not in check_in_dates_list:
            self.check_out = input(self.check_out + ' is not a valid check-out date from the following date(s) ' + str(
                check_in_dates_list) + ' (e.g. 6.8.2020): ')
        check_out_index = full_dates_list.index(self.check_out)
        print(check_in_index)
        print(check_out_index)

        self.guests = int(input('Number of Guests: '))
        while self.guests > 20:
            self.guests = int(input("We can't handle more than 20 guests per day. You have requested to accommodate " +
                                    str(self.guests) + " guests. Please enter 20 or below guests: "))

        selected_days_index_list = list(range(check_in_index - 1, check_out_index + 1))
        print(selected_days_index_list)
        for n in selected_days_index_list:
            while list(available_guests_per_day.values())[n] < self.guests:
                self.guests = int(input(full_days_list[n] + " has " + str(list(available_guests_per_day.values())[n]) +
                                        " available spots for new guests while you requested to host " +
                                        str(self.guests) + " guests.\nPlease change the amount of guests accordingly.\n"
                                                           "Enter new number of guests: "))

        self.rooms = int(input('Number of Rooms: '))

        available_rooms_per_day = self.available_rooms_per_day()
        print(available_rooms_per_day)

        while rooms > guests:
            self.guests = input("You requested " + str(self.rooms) + " while you are only " + str(self.guests) +
                                " guests. This is against our policy. Please select number of rooms no higher"
                                " than the number of guests ")

        self.name = input('Full Name: ')
        self.phone = input('Phone Number: ')

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
    def available_rooms_per_day():
        sunday = 0
        monday = 0
        tuesday = 0
        wednesday = 0
        thursday = 0
        days_rooms_dict = {'sunday': 0, 'monday': 0, 'tuesday': 0, 'wednesday': 0, 'thursday': 0, }
        with open(temp_directory + '/available_rooms.csv', 'r') as f:
            file = csv.reader(f)
            next(file)
            for row in file:
                if 'available' in row[4]:
                    sunday = sunday + 1
                if 'available' in row[5]:
                    monday = monday + 1
                if 'available' in row[6]:
                    tuesday = tuesday + 1
                if 'available' in row[7]:
                    wednesday = wednesday + 1
                if 'available' in row[8]:
                    thursday = thursday + 1
        days_rooms_dict['sunday'] = sunday
        days_rooms_dict['monday'] = monday
        days_rooms_dict['tuesday'] = tuesday
        days_rooms_dict['wednesday'] = wednesday
        days_rooms_dict['thursday'] = thursday
        return days_rooms_dict

    @staticmethod
    def available_guests_per_day():
        sunday = 0
        monday = 0
        tuesday = 0
        wednesday = 0
        thursday = 0
        days_guests_dict = {'sunday': 0, 'monday': 0, 'tuesday': 0, 'wednesday': 0, 'thursday': 0, }
        with open(temp_directory + '/available_rooms.csv', 'r') as f:
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
        return days_guests_dict

    @staticmethod
    def max_guests_capacity_per_day():
        f = csv.reader(open(temp_directory + '/available_rooms.csv'))
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

        f = csv.reader(open(temp_directory + '/available_rooms.csv'))
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

        f = csv.reader(open(temp_directory + '/available_rooms.csv'))
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

        f = csv.reader(open(temp_directory + '/available_rooms.csv'))
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

        f = csv.reader(open(temp_directory + '/available_rooms.csv'))
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
