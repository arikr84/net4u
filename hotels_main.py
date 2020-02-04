from hotels_class import Hotels

from time import sleep
import tempfile
import json
import re
import random
from colorama import Fore, init, Style, Cursor
import csv
import os.path

Hotels.rooms_file_write()
# Hotels.available_rooms_per_day()
# Hotels.available_guests_per_day()
# Hotels.max_guests_capacity_per_day()
# Hotels.available_days_list()
Hotels.available_dates_list()

user_input = Hotels('check_in', 'check_out', 'hotel', 'rooms', 'breakfast', 'guests', 'name', 'phone_number'
                                , 'id_number', 'credit_card_number', 'email')
# Hotels.cheapest_rooms()


# user_input = Hotels(check_in='')
# check-in syntax and date validation
# while user_input.check_in not in ['2.8.2020', '3.8.2020', '4.8.2020', '5.8.2020']:
#     user_input.check_in = user_input.check_in


# if user_input.check_in != 2:
#     print(check_in)
# else:
#     user_input.check_in = Hotels.from_input()

# 2-6
