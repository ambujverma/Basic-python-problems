def divisor():
    num = int(input("enter a number: "))
    listRange = (range(1,num+1))
    divisorlist =[]        
    for i in  listRange:
        if num % i == 0:
            divisorlist.append(i)
    print(divisorlist)
divisor()

#output:

# enter a number: 45
# [1, 3, 5, 9, 15, 45]  
