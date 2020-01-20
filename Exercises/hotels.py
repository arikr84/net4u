# augost sunday - חמישי
# first week of augost
#
# trivago
#
# fattal - 4 rooms 200$- 1 room for couple 250$- 1 room for couple with breakfast 350$- 1 room for tree  - 1 room three + breakfast 420$
# isrotel - 1 room for 1 100$  -  1 room for couple 170$ / 200$ with breakfast  - 1 room for three 380$ - 1 room for 4 450$ / 550$ with BF
#
# we give the coustomer menu
# 1. check available rooms all hotels  - read files
# 2. reservation - which hotel?, how much rooms? how much people, nights, breakfast, if 2 rooms same hotel?  - return free rooms and cheapest price in SHEKELS (need to convert $ to ILS)
# 3. cancle reservation cost 75%
# 4. add nights / room for reservation
#
# file for each hotels with all the information
#
# fattal.txt
# isrotel.txt
# reservation.txt

from colorama import Fore, init, Style
init(autoreset=True)
import tempfile
import json

def menu():
    break_counter = 0
    option = int(input(Fore.MAGENTA + "Trivago\n" + Fore.BLUE + "The Best Rooms For the Best Prices.\n\n" + Fore.BLACK + ""
                                        "- Enter (1) to check available rooms\n"
                                                "- Enter (2) to reserve a room\n"
                                                        "- Enter (3) to cancel reservation\n"
                                                                "- Enter (4) to add night/room for a reservation\n\n"
                                                                        "Enter your selection: "))
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
        check_available_rooms_fattal()
        check_available_rooms_isrotel()
    if option == 2:
        reservation()
    if option == 3:
        cancel_reservation()
    if option == 4:
        add_night_room_to_resrvation()

def files_creation():
    temp_directory = tempfile.gettempdir()
    fattal = open(str(temp_directory) + "/fattal.txt", "w+")
    fattal.write("{} {} {} {} {} {}".format("{'hotel': 'Fattal',", "'room': 1,", "'guests': 2,", "'breakfast': ['no', 'yes'],", "'cost': ['200$', '280$'],","'day': ['sunday', 'monday', 'tuesday', 'wednesday']}"))
    fattal = open(str(temp_directory) + "/fattal.txt", "a+")
    fattal.write("\n{} {} {} {} {} {}".format("{'hotel': 'Fattal',", "'room': 2,", "'guests': 2,", "'breakfast': ['no', 'yes'],", "'cost': ['200$', '280$'],","'day': ['sunday', 'monday', 'tuesday', 'wednesday']}"))
    fattal = open(str(temp_directory) + "/fattal.txt", "a+")
    fattal.write("\n{} {} {} {} {} {}".format("{'hotel': 'Fattal',", "'room': 3,", "'guests': 3,", "'breakfast': ['no', 'yes'],", "'cost': ['400$', '500$'],","'day': ['sunday', 'monday', 'tuesday', 'wednesday']}"))
    fattal = open(str(temp_directory) + "/fattal.txt", "a+")
    fattal.write("\n{} {} {} {} {} {}".format("{'hotel': 'Fattal',", "'room': 4,", "'guests': 3,", "'breakfast': ['no', 'yes'],", "'cost': ['400$', '500$'],","'day': ['sunday', 'monday', 'tuesday', 'wednesday']}"))
    fattal.close()

    isrotel = open(str(temp_directory) + "/isrotel.txt", "w+")
    isrotel.write("{} {} {} {} {} {}".format("{'hotel': 'Isrotel',", "'room': 1,", "'guests': 2,", "'breakfast': ['no', 'yes'],", "'cost': ['100$', '150$'],","'day': ['sunday', 'monday', 'tuesday', 'wednesday']}"))
    isrotel = open(str(temp_directory) + "/isrotel.txt", "a+")
    isrotel.write("\n{} {} {} {} {} {}".format("{'hotel': 'Isrotel',", "'room': 2,", "'guests': 2,", "'breakfast': ['no', 'yes'],", "'cost': ['100$', '150$'],","'day': ['sunday', 'monday', 'tuesday', 'wednesday']}"))
    isrotel = open(str(temp_directory) + "/isrotel.txt", "a+")
    isrotel.write("\n{} {} {} {} {} {}".format("{'hotel': 'Isrotel',", "'room': 3,", "'guests': 3,", "'breakfast': ['no', 'yes'],", "'cost': ['200$', '280$'],","'day': ['sunday', 'monday', 'tuesday', 'wednesday']}"))
    isrotel = open(str(temp_directory) + "/isrotel.txt", "a+")
    isrotel.write("\n{} {} {} {} {} {}".format("{'hotel': 'Isrotel',", "'room': 4,", "'guests': 3,", "'breakfast': ['no', 'yes'],", "'cost': ['200$', '280$'],","'day': ['sunday', 'monday', 'tuesday', 'wednesday']}"))
    isrotel.close()

    reservation = open(str(temp_directory) + "/reservation.txt", "w+")
    reservation.close()

def check_available_rooms_fattal():
    temp_directory = tempfile.gettempdir()
    for line in open(str(temp_directory) + "/fattal.txt", "r").readlines():
        fattal = line.replace("'", "\"")
        fattal = json.loads(fattal)
        if len(list(fattal.values())[5]) == 4:
            print(Style.BRIGHT + Fore.BLUE + "hotel: " + str(list(fattal.values())[0]) + Style.NORMAL + Fore.BLACK + " | room: " + str(list(fattal.values())[1]) + " | guests: " + str(list(fattal.values())[2]) +
                  " | breakfast not included: " + str(list(fattal.values())[4][0]) + " | breakfast included: " +
                  str(list(fattal.values())[4][1]) + " | available for " + str(
                len(list(fattal.values())[5])) + " days: " + str(list(fattal.values())[5]))
        else:
            print(Fore.RED + str(temp_directory) + "/fattal.txt doesn't contain 4 lines (line for each room)"
                                                   " as expected.")
            quit()

def check_available_rooms_isrotel():
    temp_directory = tempfile.gettempdir()
    for line in open(str(temp_directory) + "/isrotel.txt", "r").readlines():
        isrotel = line.replace("'", "\"")
        isrotel = json.loads(isrotel)
        if len(list(isrotel.values())[5]) == 4:
            print(Style.BRIGHT + Fore.GREEN + "hotel: " + str(list(isrotel.values())[0]) + Style.NORMAL + Fore.BLACK +
                  " | room: " + str(list(isrotel.values())[1]) + " | guests: " + str(list(isrotel.values())[2]) +
                  " | breakfast not included: " + str(list(isrotel.values())[4][0]) + " | breakfast included: " +
                  str(list(isrotel.values())[4][1]) + " | available for " + str(
                len(list(isrotel.values())[5])) + " days: " + str(list(isrotel.values())[5]))
        else:
            print(Fore.RED + str(temp_directory) + "/isrotel.txt doesn't contain 4 lines (line for each room)"
                                                   " as expected.")
            quit()

def max_guests_capacity():
    isrotel_max_guests = 0
    fattal_max_guests = 0
    temp_directory = tempfile.gettempdir()
    for line in open(str(temp_directory) + "/isrotel.txt", "r").readlines():
        isrotel = line.replace("'", "\"")
        isrotel = json.loads(isrotel)
        isrotel_max_guests = isrotel_max_guests + list(isrotel.values())[2]
    for line in open(str(temp_directory) + "/fattal.txt", "r").readlines():
        fattal = line.replace("'", "\"")
        fattal = json.loads(fattal)
        fattal_max_guests = fattal_max_guests + list(fattal.values())[2]
    max_guests = isrotel_max_guests + fattal_max_guests
    return max_guests


        # if len(list(isrotel.values())[5]) == 4:
        #     print(Style.BRIGHT + Fore.GREEN + "hotel: " + str(list(isrotel.values())[0]) + Style.NORMAL + Fore.BLACK +
        #           " | room: " + str(list(isrotel.values())[1]) + " | guests: " + str(list(isrotel.values())[2]) +
        #           " | breakfast not included: " + str(list(isrotel.values())[4][0]) + " | breakfast included: " +
        #           str(list(isrotel.values())[4][1]) + " | available for " + str(
        #         len(list(isrotel.values())[5])) + " days: " + str(list(isrotel.values())[5]))
        # else:
        #     print(Fore.RED + str(temp_directory) + "/isrotel.txt doesn't contain 4 lines (line for each room)"
        #                                            " as expected.")
        #     quit()



def reservation():
    max_guests = max_guests_capacity()
    temp_directory = tempfile.gettempdir()
    guests = int(input(Style.BRIGHT + "Number of guests on the reservation?: "))
    if guests > max_guests:
        quit("Both Fattal and Isrotel hotels can host maximum of " + str(max_guests) +
             " guests while you have requested to host " + str(guests) + " guests")
    if guests < max_guests:
        for line in open(str(temp_directory) + "/fattal.txt", "r").readlines():
            fattal = line.replace("'", "\"")
            fattal = json.loads(fattal)
            if len(list(fattal.values())[5]) > 0:
                print("- Room " + str(list(fattal.values())[1]) + " in " + Fore.GREEN + Style.BRIGHT +
                      str(list(fattal.values())[0]) + Fore.BLACK + Style.NORMAL + " hotel can hosts " +
                      str(list(fattal.values())[2]) + " guests and is available in the following " +
                      str(len(list(fattal.values())[5])) + " days of the first week of August: " +
                      str(list(fattal.values())[5]))
            else:
                print(Fore.RED + "- Room " + str(list(fattal.values())[1]) + " in " + str(list(fattal.values())[0]) +
                      " hotel is already taken")
        for line in open(str(temp_directory) + "/isrotel.txt", "r").readlines():
            isrotel = line.replace("'", "\"")
            isrotel = json.loads(isrotel)
            if len(list(isrotel.values())[5]) > 0:
                print("- Room " + str(list(isrotel.values())[1]) + " in " + Fore.BLUE + Style.BRIGHT +
                      str(list(isrotel.values())[0]) + Fore.BLACK + Style.NORMAL + " hotel can hosts " +
                      str(list(isrotel.values())[2]) + " guests and is available in the following " +
                      str(len(list(isrotel.values())[5])) + " days of the first week of August: " +
                      str(list(isrotel.values())[5]))
            else:
                print(Fore.RED + "- Room " + str(list(isrotel.values())[1]) + " in " + str(list(isrotel.values())[0]) +
                      " hotel is already taken")
                quit()

    print(Fore.MAGENTA + Style.BRIGHT +"\nReservation for " + str(guests) + " guest(s) accepted")
    rooms = guests/2
    print(rooms)




    # yes = {'yes', 'y', 'ye', ''}
    # no = {'no', 'n'}
    # breakfast = input("Breakfast included?. Please respond with 'yes' or 'no': ").lower()
    # if breakfast in yes:
    #     print("Breakfast included")
    # elif breakfast in no:
    #     print("Breakfast is not included")
    # else:
    #     sys.stdout.write("Please respond with 'yes' or 'no'")

reservation()




#1 Understand how many rooms there are available for 2 people
#2 Understand how many rooms there are available for 3 people
#3 calculate the amount of people // 2          -  add them people to the rooms for 2 people
#4 The calculation will yield number of requires rooms (X). check which 2 people rooms are the cheapers
#5 if leftovers people calcule the leftovers // 3           -  add them people to the rooms for 2 people
#6 The calculation will yield number of requires rooms (X). check which 2 people rooms are the cheapers