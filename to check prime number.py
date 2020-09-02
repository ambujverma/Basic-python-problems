#1
num = int(input('Insert a number: '))
a = [x for x in range(2, num-1) if num % x == 0]

def is_prime():
	if num > 1:
		if len(a) == 0:
			print ('prime')
		else:
		    print ('NOT prime')
	else:
		print('NOT prime') 
	
is_prime()
print(a)



#2
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
