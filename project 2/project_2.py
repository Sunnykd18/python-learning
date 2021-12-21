import random

number = random.randint(1,100)
attempt = 1
guess = int(input("guess the no.: "))

while(True):
   if(guess>number):
    guess = int(input("guess another number. this one is too big: "))
    attempt += 1
   elif(guess<number):
    guess = int(input("guess another number. this one is too less"))
    attempt += 1
   else:
    print(f"you won.your no. of attempts is {attempt}")    
    break