def fibTabulated(n):
    table = [None] * n
    table[0] = 1
    table[1] = 1

    for i in range(2,len(table)):
        table[i] = table[i-1] + table[i-2]
    
    return table[n-1]

print(fibTabulated(15))