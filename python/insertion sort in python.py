def insertionSort1(n, arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j >=0 and key < arr[j]:
            arr[j+1]=arr[j]
            print(" ".join(str(a) for a in arr))
            j-=1
        arr[j+1]=key
    print(" ".join(str(a) for a in arr))