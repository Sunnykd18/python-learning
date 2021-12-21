'''
factorial(n) = n* factorial(n-1)
factorial(0) = 1
factorial(4) = 4 x 3 x 2 x 1
factorial(3) = 3 x 2 x 1 

'''
def factorial(n):
    # base condition to stop the code reccurring to infinity
    if (n==0 or n==1):
        return 1
    return n * factorial(n - 1)  

a = factorial(7)    
print(a)