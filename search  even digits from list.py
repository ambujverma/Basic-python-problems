#1

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
c=[]
for i in a:
    if i%2==0:
        c.append(i)
print(c)
print("even numers of list a")
print(a)      

#OUTPUT
#[4, 16, 36, 64, 100]


#2

import random
numlist = []
list_length = random.randint(5,15)
while len(numlist) < list_length:
    numlist.append(random.randint(1,10))
evenlist = [number for number in numlist if number % 2 == 0] 
print(evenlist)

#OUTPUT
#[4, 10, 8, 4, 10, 8, 4]
