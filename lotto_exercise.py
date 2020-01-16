import random

def menu():
    option =  int(input(">>> Please choose one of the following options: <<<\n1 for manual_lotto\n2 for automatic lotto\n2 to check win\n4 for double lotto\n\nEnter you choice: "))
    if option == 1:
    elif
    elif
    elif


def manual():
    num =  int(input("You have selected the 'Manual Lotto'. How much ILS you wish to pay?: "))
    print(num // 3)

def automatic():
    money = int(input("You have selected the 'Automatic Lotto'. How much ILS you wish to pay?: "))
    return money

def generate_list():
    gen = []
    while len(set(gen)) < 6:
        x = (random.randint(1, 37))
        if x not in gen:
            gen.append(x)
    return gen

def manual_fill_lotto(a):
    list2 = []
    print("this is a: {}".format(a))
    for i in range(a//3):
        print("Print 6 numbers for list " + str(i + 1) + ":")
        list1 = []
        for x in range(6):
            num = int(input("Enter a number: "))
            while (num > 37) or (num < 1) or num in list1:
                num = int(input("ERROR: Enter a number between 1 and 37 that was not added before: "))
            list1.append(num)
        list2.append(list1)
    print("Manual lottery columns: " + str(list2))
    return list2

def manual_statistics():
    a=manual()
    b=manual_fill_lotto(a)
    c=generate_list()
    print("Winning Numbers: " + str(c))
    for z in range(a//3):
        loss_counter = 0
        win_counter = 0
        for y in range(6):
            if b[z][y] not in c:
                # print("LOST: " + str(b[z][y]) + " not contained within " + str(c))
                loss_counter = loss_counter + 1
            else:
                # print("WIN: " + str(b[z][y]) + " contained within " + str(c))
                win_counter = win_counter + 1

        if win_counter == 0:
            print("Column " + str(z + 1) + " > LOST <: no match's found in lotto column " + str(
                z + 1) + ". Better luck next time")
        else:
            print("Column " + str(z + 1) + " > WIN <: 1 match found in lotto column " + str(
                z + 1) + " You won {}$".format(10 ** win_counter))
        # if win_counter == 0:
        #     print("Column " + str(z+1) + " > LOST <: no match's found in lotto column " + str(z+1) + ". Better luck next time")
        # elif win_counter == 1:
        #     print("Column " + str(z+1) + " > WIN <: 1 match found in lotto column " + str(z+1) + " You won 10$")
        # elif win_counter == 2:
        #     print("Column " + str(z+1) + " > WIN <: 2 match's found in lotto column " + str(z + 1) + " You won 100$")
        # elif win_counter == 3:
        #     print("Column " + str(z+1) + " > WIN <: 3 match's found in lotto column " + str(z + 1) + " You won 1,000$")
        # elif win_counter == 4:
        #     print("Column " + str(z+1) + " > WIN <: 4 match's found in lotto column " + str(z + 1) + " You won 10,000$")
        # elif win_counter == 5:
        #     print("Column " + str(z+1) + " > WIN <: 5 match's found in lotto column " + str(z + 1) + " You won 100,000$")
        # elif win_counter == 6:
        #     print("Column " + str(z+1) + " > WIN <: 6 match's found in lotto column " + str(z + 1) + " You won 1,000,000$")

manual_statistics()

