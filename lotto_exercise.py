import random
from colorama import Fore, init
init(autoreset=True)


def start_the_lottery():
    option =  int(input(Fore.BLUE + "<<< The Big Lottery Game Version 1.0 >>>\n\n" + Fore.BLACK + "Select one of the following options:\n\n" + Fore.LIGHTBLACK_EX + "- Enter (1) to check the prizes\n- Enter (2) to run the manual lottery"
                        "\n- Enter (3) to run the manual double lottery\n- Enter (4) to run the automatic lottery\n- Enter (5) to run the automatic double lottery\n\n" + Fore.BLACK + "Enter you choice: "))
    while option == 0 or option > 5:
        option = int(input("Option " + str(option) + " is invalid. Choose option 1 to 5: "))
    if option == 1:
        check_prizes()
    if option == 2:
        manual_lotto()
    if option == 3:
        double_manual_lotto()
    if option == 4:
        automatic_lotto()
    if option == 5:
        double_automatic_lotto()

def lotto_columns():
    columns =  int(input("\nEach lottery column costs 3 ILS.\nHow many columns "
                         "would you like to purchases?: "))
    print(str(columns) + " columns will cost you " + Fore.MAGENTA + str(columns * 3) + " ILS.\n")
    return columns

def lotto_columns_double():
    columns =  int(input("\nEach lottery column costs 6 ILS.\nHow many "
                         "columns would you like to purchases?: "))
    print(str(columns) + " columns will cost you " + Fore.MAGENTA + str(columns * 6) + " ILS.\n")
    return columns

def decision():
    decision = input("Enter (Y) to continue or (N) to withdrew: ")
    while decision != ("y", "Y") and decision != ("n", "N"):
        if decision == "N" or decision == "n":
            print("You have chosen to withdrew. Kindly join us another time. Farewell.\n")
            quit()
        if decision == "Y" or decision == "y":
            print("You have chosen to continue. May luck be in your favor!\n")
            break
        else:
            decision = input("("+ str(decision) + ")" + " is not a valid option. Choose (Y) or (N): ")

def generate_column():
    gen = []
    while len(set(gen)) < 6:
        x = (random.randint(1, 37))
        if x not in gen:
            gen.append(x)
    print("\n*** LOTTERY WINNING NUMBERS: " + str(gen) + " ***")
    return gen

def enter_manual_numbers(a):
    list2 = []
    for i in range(a):
        print("\nPrint 6 numbers for column (" + str(i + 1) + ")\n")
        list1 = []
        for x in range(6):
            num = int(input("\tEnter a number between 1 and 37: "))
            while (num > 37) or (num < 1) or num in list1 :
                num = int(input("\tThe number " + str(num) + " is invalid or is already exists - Enter a new number: "))
            list1.append(num)
        list2.append(list1)
    print("Manual lottery columns: " + str(list2))
    return list2

def enter_automatic_numbers(a):
    automatic_list = []
    for i in range(a):
        gen = []
        for y in range(6):
            while len(set(gen)) < 6:
                x = (random.randint(1, 37))
                if x not in gen:
                    gen.append(x)
        automatic_list.append(gen)
    print("Generated " + str(a) + " column(s): " + str(automatic_list))
    return automatic_list

def manual_lotto():
    a=lotto_columns()
    decision()
    b=enter_manual_numbers(a)
    c=generate_column()
    win_loss_calc(a, b, c)

def double_manual_lotto():
    a=lotto_columns_double()
    b=enter_manual_numbers(a)
    c=generate_column()
    win_loss_calc_double(a, b, c)

def automatic_lotto():
    a=lotto_columns()
    decision()
    b=enter_automatic_numbers(a)
    c=generate_column()
    win_loss_calc(a, b, c)

def double_automatic_lotto():
    a=lotto_columns_double()
    decision()
    b=enter_automatic_numbers(a)
    c=generate_column()
    win_loss_calc_double(a, b, c)

def win_loss_calc(a, b, c):
    prize = 0
    for z in range(a):
        loss_counter = 0
        win_counter = 0
        for y in range(6):
            if b[z][y] not in c:
                loss_counter = loss_counter + 1
            else:
                win_counter = win_counter + 1
        if win_counter < 3:
            pass
        if win_counter == 3:
            print("Column " + str(z + 1) + ": (WIN) - " + str(win_counter) + " match(s) found in column " + str(
                z + 1) + " " + str(b[z]) + " - you won >>>  {} ILS  <<<".format(10))
            prize = prize + 10
        if win_counter == 4:
            print("Column " + str(z + 1) + ": (WIN) - " + str(win_counter) + " match(s) found in column " + str(
                z + 1) + " " + str(b[z]) + " - you won >>> {} ILS <<<".format(250))
            prize = prize + 250
        if win_counter == 5:
            print("Column " + str(z + 1) + ": (WIN) - " + str(win_counter) + " match(s) found in column " + str(
                z + 1) + " " + str(b[z]) + " - you won >>> {} ILS <<<".format(500))
            prize = prize + 500
        if win_counter == 6:
            print("Column " + str(z + 1) + ": (WIN) - " + str(win_counter) + " match(s) found in column " + str(
                z + 1) + " " + str(b[z]) + " - you won >>> {} ILS <<<".format(1000000))
            prize = prize + 1000000
    print("\nYou wasted " + str(a * 3) + " ILS")
    print("You won " + str(prize) + " ILS")
    if int(prize) > int(a * 3):
        print(Fore.BLUE + "<<< You gained " + str(prize - a * 3) + " ILS >>>")
    else:
        print(Fore.RED + "<<< You overspend " + str(a * 3 - prize) + " ILS (" + str(prize - a * 3) + ") >>>")

def win_loss_calc_double(a, b, c):
    prize = 0
    for z in range(a):
        loss_counter = 0
        win_counter = 0
        for y in range(6):
            if b[z][y] not in c:
                loss_counter = loss_counter + 1
            else:
                win_counter = win_counter + 1
        if win_counter < 3:
            pass
        if win_counter == 3:
            print("Column " + str(z + 1) + ": (WIN) - " + str(win_counter) + " match(s) found in column " + str(
                z + 1) + " " + str(b[z]) + " - you won >>>  {} ILS  <<<".format(20))
            prize = prize + 20
        if win_counter == 4:
            print("Column " + str(z + 1) + ": (WIN) - " + str(win_counter) + " match(s) found in column " + str(
                z + 1) + " " + str(b[z]) + " - you won >>> {} ILS <<<".format(500))
            prize = prize + 500
        if win_counter == 5:
            print("Column " + str(z + 1) + ": (WIN) - " + str(win_counter) + " match(s) found in column " + str(
                z + 1) + " " + str(b[z]) + " - you won >>> {} ILS <<<".format(1000))
            prize = prize + 1000
        if win_counter == 6:
            print("Column " + str(z + 1) + ": (WIN) - " + str(win_counter) + " match(s) found in column " + str(
                z + 1) + " " + str(b[z]) + " - you won >>> {} ILS <<<".format(2000000))
            prize = prize + 2000000
    print("\nYou spent " + str(a * 6) + " ILS")
    print("You won " + str(prize) + " ILS")
    if int(prize) > int(a * 6):
        print(Fore.BLUE + "<<< You won " + str(prize - a * 6) + " ILS >>>")
    else:
        print(Fore.RED + "<<< You overspend " + str(a * 6 - prize) + " ILS (" + str(prize - a * 6) + ") >>>")

def check_prizes():
    print("\nThe Original Lotto Prizes:\n" + str("-"*26) + "\n- 1-3 match's wins 0 ILS\n- 4 match's wins 250 ILS\n- 5 match's wins 500 ILS\n" + Fore.LIGHTBLUE_EX + "- 6 match's wins 1000000 "
              "ILS (jackpot)")
    print("\nThe Double Lotto Prizes:\n" + str(
        "-" * 26) + "\n- 1-3 match's wins 0 ILS\n- 4 match's wins 500 ILS\n- 5 match's wins 1000 ILS\n" + Fore.LIGHTBLUE_EX + "- 6 match's wins 2000000 "
                    "ILS (jackpot)")


start_the_lottery()