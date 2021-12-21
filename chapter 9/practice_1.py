def greatest(a,b,c):
    if (a>b):
        greater = a
    else:
        greater = b
    if (greater<c):
        greater = c
    return greater
a = greatest(1,23,125)        
print(a)

