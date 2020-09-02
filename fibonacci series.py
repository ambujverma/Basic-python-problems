#1
def fibonacci():
    n = int(input("enter number to how many terms generate :"))
    if n==0:
        print(0)
    else:
        x=0
        y=1
        print(x)
        print(y)
        for i in range(2,n):
            z=(x+y)
            x=y
            y=z
            print(y) 
fibonacci()

#2
cube = lambda x:x*x*x
def fibonacci(n):

    i = 1
    if n==0:
        fib = []
    elif n==1:
        fib = [0]
    elif n==2:
        fib = [0,1]
    elif n>2:
        fib = [0,1]
        while i<(n-1):
            fib.append(fib[i] + fib[i-1])
            i += 1
       
        
    return(fib)
print(list(map(cube, fibonacci(5))))
