try:
    a = int(input("enter the no: "))
    b = int(input("enter the no: "))
    print(a/b)

except Exception as e:
    if (b == 0):
        print(f"the ans is infinity the reason is:{e}")    