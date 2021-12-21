try:
    print("hello world")
    a = int(input("enter the no: "))
    b = int(input("enter the no: "))
    if b>199:
        raise Exception("this no. is too large")
except ValueError:
    print("value error occured")
except ZeroDivisionError:
    print("this is zero division error")    
except Exception as e:
    print(f"this problem occured:{e} ")
else:
    print("try was successfull")
print("there is exception used")       
