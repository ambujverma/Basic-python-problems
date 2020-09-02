a = [1, 1, 2, 2, 2, 3, 3, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


result_overlaped =[ i for i in a if i in b]
result = []
for j in result_overlaped:
    if j not in result:
        result.append(j)

        
print(result)        
