from time import sleep
import re
import ipaddress
from colorama import Fore, init
init(autoreset=True)


def dns_configuration():
    option = int(input(Fore.BLUE + "DNS Configuration Version 1.0\n\n" + Fore.LIGHTBLACK_EX + "- Enter (1) to add a "
    "record to the DNS\n- Enter (2) to delete a record from the DNS\n- Enter (3) to update a record within the DNS\n"
    "- Enter (4) to print all the DNS records\n- Enter (5) to search for a record within the DNS\n\n"
    + Fore.BLACK + "Enter your selection: "))

    for i in range(5):
        while option == 0 or option > 5:
            option = int(input("Option " + str(option) + " is invalid. Enter an option between 1 to 5: "))
            break
    if option == 0 or option > 5:
        print(Fore.RED + "\nERROR: Maximum (5) tries exceeded. Next time enter an option between 1 to 5. Exiting...")
    if option == 1:
        add_dns()
    if option == 2:
        original_records = original_dns_records()
        dns_list(original_records)
        delete_dns()
    if option == 3:
        original_records = original_dns_records()
        dns_list(original_records)
        update_dns()
    if option == 4:
        original_records = original_dns_records()
        dns_list(original_records)
    if option == 5:
        search_dns()

def original_dns_records():
    original_records = {"google.com": "1.1.1.1", "amazon.com": "2.2.2.2", "ynet.co.il": "3.3.3.3",
                        "facebook.com": "4.4.4.4",
                        "aliexpress.com": "5.5.5.5"}
    return original_records

def add_dns():
    url = input(Fore.LIGHTBLUE_EX + "\nEnter URL to add: ")
    original_records = original_dns_records()
    if url in original_records:
        print(Fore.RED + "ERROR: The URL '" + url + "' already exists in the DNS.")
        quit_error()
    elif url not in original_records:
        if not re.search('[a-z]', url):
            print(Fore.RED + "ERROR: The URL can't consist of uppercase letter(s).")
            quit_error()
        if re.search('[a-z]', url) and re.search('[`?"\';:~!@#$%^&*()_+=/<>|,*]', url):
            print(Fore.RED + "ERROR: The URL can't contain one of the [`?\"';:~!@#$%^&*()_+=/<>|,*] characters.")
            quit_error()
            if url in original_records:
                print(Fore.RED + "ERROR: The URL '" + url + "' already exists in the DNS.")
                quit_error()
        else:
            ip = input("Enter " + str(url) + " IP address: ")
            if not bool(ipaddress.ip_address(ip)):
                pass
            else:
                original_records.update({url: ip})
            sleep_before_list()
            dns_list(original_records)

def delete_dns():
    original_records = original_dns_records()
    url = input(Fore.LIGHTBLUE_EX + "\nEnter URL to delete from the DNS: ")
    if url not in original_records:
        print(Fore.RED + "\nERROR: The URL '" + str(url) + "' is not found within the DNS. Exiting...")
        quit_error()
    else:
        del original_records[url]
        # validation that the record was really deleted from the DNS
        if url not in original_records:
            print(Fore.LIGHTBLUE_EX + "\n>>> Successfully deleted the URL '" + str(url) + "' from the DNS records <<<")
            sleep_before_list()
            dns_list(original_records)
        else:
            print(Fore.RED + "\n >>> ERROR: the record '" + str(url) + "' still exists in the DNS while it should have "
                                                                       "been deleted.")
            quit_error()

def update_dns():
    original_records = original_dns_records()
    url = input("\nEnter URL to update: ")
    if url not in original_records:
        print(Fore.RED + "ERROR: The URL '" + str(url) + "' doesn't exists in the DNS")
        quit_error()
    else:
        ip = input("Enter " + str(url) + " IP address: ")
        if not bool(ipaddress.ip_address(ip)):
            pass
        original_records.update({url: ip})
        sleep_before_list()
        dns_list(original_records)

def search_dns():
    original_records = original_dns_records()
    search_key = input("Enter the DNS record you wish to find: ")
    if any(key.startswith(search_key) for key in original_records):
        search_key = dict(filter(lambda list: list[0].startswith(search_key), original_records.items()))
        sleep_before_list()
        dns_list(search_key)
    else:
        print(Fore.RED + "ERROR: The string '" + str(search_key) + " is not found in the DNS")
        quit_error()

def dns_list(original_records):
    original_records = original_records
    print(Fore.GREEN + "\n>>> DNS Records <<<")
    for key, value in original_records.items():
        print(Fore.LIGHTBLACK_EX + key, value)

def sleep_before_list():
    print("Printing the updated DNS records. Hold on for a short while...")
    sleep(3)

def quit_error():
    quit(1)


dns_configuration()
