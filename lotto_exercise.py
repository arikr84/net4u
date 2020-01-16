import random

def start_the_lottery():
    option =  int(input("Please choose one of the following options:\n1 - Manual lotto\n2 - Automatic lotto"
                        "\n3 - Check win\n4 - Manual double lotto\n5 - Automatic double lotto\n\nEnter you choice: "))
    while option == 0 or option > 5:
        option = int(input("Option " + str(option) + " is invalid. Please choose between option 1 to 5: "))
    if option == 1:
        manual_lotto()
    if option == 2:
        automatic_lotto()
    if option == 3:
        print("WHAT?")
    if option == 4:
        double_manual_lotto()
    if option == 5:
        double_automatic_lotto()

def lotto_columns():
    columns =  int(input(">>> Welcome to Arik's lottery! <<<\nEach lottery column costs 30 ILS.\nHow many columns would"
                         " you like to purchases?: "))
    print(str(columns) + " columns will cost you " + str(columns*30) + " ILS.\n")
    decision = input("Press (Y) to continue or (N) to withdrew: ")
    while decision != ("y", "Y") and decision != ("n", "N"):
        if decision == "N" or decision == "n":
            print("You have chosen to withdrew. Kindly join us another time. Farewell.\n")
            quit()
        if decision == "Y" or decision == "y":
            print("You have chosen to continue. May the luck shines upon you.\n")
            break
        else:
            decision = input("("+ str(decision) + ")" + " is not a valid option. Please choose (Y) or (N): ")
    return columns


def generate_column():
    gen = []
    while len(set(gen)) < 6:
        x = (random.randint(1, 37))
        if x not in gen:
            gen.append(x)
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
        # print("Generated the numbers " + str(gen) + " for column " + str(i + 1))
        automatic_list.append(gen)
    print("Generated " + str(a) + " column(s): " + str(automatic_list))
    return automatic_list


def manual_lotto():
    a=lotto_columns()
    b=enter_manual_numbers(a)
    c=generate_column()
    print("\n***** WINNING NUMBERS ***** \n" + str(c) + "\n")
    for z in range(a):
        loss_counter = 0
        win_counter = 0
        for y in range(6):
            if b[z][y] not in c:
                loss_counter = loss_counter + 1
            else:
                win_counter = win_counter + 1

        if win_counter == 0:
            print("Column " + str(z + 1) + " > LOST <: no match's found in lotto column " + str(
                z + 1) + ". Better luck next time")
        else:
            print("Column " + str(z + 1) + " > WIN <: " + str(win_counter) + " match(s) found in lotto column " + str(
                z + 1) + " You won {} ILS".format(10 ** win_counter))


def double_manual_lotto():
    a=lotto_columns()
    b=enter_manual_numbers(a)
    c=generate_column()
    print("\n***** WINNING NUMBERS ***** \n" + str(c) + "\n")
    for z in range(a):
        loss_counter = 0
        win_counter = 0
        for y in range(6):
            if b[z][y] not in c:
                loss_counter = loss_counter + 1
            else:
                win_counter = win_counter + 1

        if win_counter == 0:
            print("Column " + str(z + 1) + " > LOST <: no match's found in lotto column " + str(
                z + 1) + ". Better luck next time")
        else:
            print("Column " + str(z + 1) + " > WIN <: " + str(win_counter) + " match(s) found in lotto column " + str(
                z + 1) + " You won {} ILS".format(10 ** win_counter *2))


def automatic_lotto():
    a=lotto_columns()
    b=enter_automatic_numbers(a)
    c=generate_column()
    prize=0
    print("\n***** WINNING NUMBERS ***** \n" + str(c) + "\n")
    for z in range(a):
        loss_counter = 0
        win_counter = 0
        for y in range(6):
            if b[z][y] not in c:
                loss_counter = loss_counter + 1
            else:
                win_counter = win_counter + 1
        if win_counter < 4:
            pass
        else:
            print("Column " + str(z + 1) + ": (WIN) - " + str(win_counter) + " match(s) found in column " + str(z + 1) + " - you won >>>  {} ILS  <<<".format(10 ** win_counter))
            prize = prize + 10 ** win_counter
    print("\nYou spend " + str(a*30) + " ILS")
    print("You won " + str(prize) + " ILS")
    if int(prize) > int(a*30):
        print("You now have extra " + str(prize - a*30) + " ILS")
    else:
        print("[ You owns Arik Rozenman " + str(a * 30 - prize) + " ILS ]")


def double_automatic_lotto():
    a=lotto_columns()
    b=enter_automatic_numbers(a)
    c=generate_column()
    prize=0
    print("\n***** WINNING NUMBERS ***** \n" + str(c) + "\n")
    for z in range(a):
        loss_counter = 0
        win_counter = 0
        for y in range(6):
            if b[z][y] not in c:
                loss_counter = loss_counter + 1
            else:
                win_counter = win_counter + 1
        if win_counter < 4:
            pass
            # print("Column " + str(z + 1) + ": (LOST) - " + str(win_counter) + " match(s) found in column " + str(z + 1) + " - no win")
        else:
            print("Column " + str(z + 1) + ": (WIN) - " + str(win_counter) + " match(s) found in column " + str(z + 1) + " - you won >>>  {} ILS  <<<".format(10 ** win_counter * 2))
            prize = prize + 10 ** win_counter * 2
    print("\nYou spend " + str(a*30) + " ILS")
    print("You won " + str(prize) + " ILS")
    if int(prize) > int(a*30):
        print("You now have extra " + str(prize - a*30) + " ILS")
    else:
        print("[ You owns Arik Rozenman " + str(a * 30 - prize) + " ILS ]")


start_the_lottery()