x = str(input("enter some words :"))
def reverse(x):
    y =x.split()
    return " ".join(y[::-1])
    
print(reverse(x))

#OUTPUT
#enter some words :ambuj is
#is ambuj
