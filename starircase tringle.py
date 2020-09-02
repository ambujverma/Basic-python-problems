def staircase():
    n =int(input('how many staircase you want to print'))
    
    n1=n-1
    i=1
    for i in range(1,n):
         print(' '*(n1-i),'#' ' '*i)
            
    print('#' ' '*n)
    
staircase()
        
#   OUTPUT
#   how many staircase you want to print4
#      # 
#     # # 
#    # # # 
#   # # # # 
