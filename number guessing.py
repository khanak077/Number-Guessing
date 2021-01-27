n = int(input("Enter no. from 1 to 10: "))
x = 8
for i in range(3):
    if (n != x):
        if (i == 1):
            print("The no. entered is wrong. Two chance left")
            n = int(input("Next chance: "))
        elif (i == 2):
            print("The no. entered is wrong. One chance left")
            n = int(input("Next chance: "))
            print("Chances over")
            if (x == n):
                print("The numb8er chosen is correct")
            break
    if (x == n):
        print("The number chosen is correct")
        break
    elif (x % 2 == 0):
        print("Choose a no. which is divisible by 2")
    elif (x % 3 == 0):
        print("Choose a no. which is divisible by 3")
    elif (x % 5 == 0):
        print("Choose a no. which is divisible by 5")
    else:
        print("Choose a no. which is divisible by 7")
    if (x - n == 1):
        print("The no. chosen is wrong. Choose a greater no.")
    elif (x - n == 2):
        print("The no. chosen is wrong. Choose a greater no.")
    elif (x - n == 3):
        print("The no. chosen is wrong. Choose a greater no.")
    elif (x - n == 4):
        print("The no. chosen is wrong. Choose a greater no.")
    elif (x - n == 5):
        print("The no. chosen is wrong. Choose a greater no.")
    elif (x - n == 6):
        print("The no. chosen is wrong. Choose a greater no.")
    elif (x - n == 7):
        print("The no. chosen is wrong. Choose a greater no.")

