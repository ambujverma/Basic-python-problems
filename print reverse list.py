import sys
number = input("Please enter a number" + "\n" + ">>>")
number = int(number)
 
if number > 0:
    for x in range (2, number -1 ):
        if number % x != 0: 
            continue 
        elif number % x == 0: 
            sys.exit("0The number is not prime.")
    sys.exit("1The number is prime.")
elif number == 0:
    sys.exit("2The number is not prime.")
else:
    sys.exit("3The number is not prime.")

