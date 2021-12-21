m1 = int(input("Enter the marks for subject"))
m2 = int(input("Enter the marks for subject"))
m3 = int(input("Enter the marks for subject"))

total = (m1+m2+m3)/3

if(total>=40 and m1>=33 and m2>=33 and m3>=33):
    print("You have passed")
else:
     print("You have not passed")