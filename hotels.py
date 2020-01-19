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
from colorama import Fore, init
init(autoreset=True)
from pathlib import Path
import tempfile


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
        check_available_rooms()
    if option == 2:
        reservation()
    if option == 3:
        cancel_reservation()
    if option == 4:
        add_night_room_to_resrvation()

def files():
    temp_directory = tempfile.gettempdir()
    print(temp_directory)
    # Path(%TEMP%'arik').touch()
    isrotel = open(str(temp_directory)+ "/isrotel.txt", "w+")
    isrotel.write("{} {} {} {}".format("{'room': 1,", "'people': 2,", "'breakfast': 'no',", "'cost': '100$'}"))
    isrotel = open(str(temp_directory) + "/isrotel.txt", "a+")
    isrotel.write("\n{} {} {} {}".format("{'room': 1,", "'people': 2,", "'breakfast': 'yes',", "'cost': '150$'}"))
    isrotel.write("\n{} {} {} {}".format("{'room': 2,", "'people': 2,", "'breakfast': 'no',", "'cost': '100$'}"))
    isrotel.write("\n{} {} {} {}".format("{'room': 2,", "'people': 2,", "'breakfast': 'yes',", "'cost': '150$'}"))
    isrotel.write("\n{} {} {} {}".format("{'room': 3,", "'people': 3,", "'breakfast': 'no',", "'cost': '200$'}"))
    isrotel.write("\n{} {} {} {}".format("{'room': 3,", "'people': 3,", "'breakfast': 'yes',", "'cost': '280$'}"))
    isrotel.write("\n{} {} {} {}".format("{'room': 4,", "'people': 3,", "'breakfast': 'no',", "'cost': '200$'}"))
    isrotel.write("\n{} {} {} {}".format("{'room': 4,", "'people': 3,", "'breakfast': 'yes',", "'cost': '280$'}"))
    # isrotel.write("{}    {}    {}    {}".format("room 1", "2 people", "with breakfast", "150$"))
    # isrotel.write("0,10,d", "room 1\t2 people\twithout breakfast\t100$\nroom 1\t2 people\twith breakfast\t150$"
    #                         "\nroom 2\t2 people\twithout breakfast\t100$\nroom 2\t2 people\twith breakfast\t150$\n"
    #                         "room 3\t3 people\twithout breakfast\t200$\nroom 3\t3 people\twith breakfast\t280$\n"
    #                         "room 4\t3 people\twithout breakfast\t200$\nroom 4\t3 people\twith breakfast\t280$".format())
    isrotel.close()
    # fattal_file = open("%TEMP%fattal", "w+")
    # reservation_file = open("%TEMP%reservation", "w+")
