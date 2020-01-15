num1 = int(input("Enter the 1st integer in the Fibonacci sequence: "))
num2 = int(input("Enter the 2nd integer in the Fibonacci sequence: "))

list = [num1,num2]
while list[-1] < 10000:
    i = list[-1] + list[-2]
    list.append(i)

print("\nEach number is the sum of the two preceding ones.\nThe 1st and 2nd numbers will determine the rest of the sequence.\n\nFibonacci sequence: " + str(list))
