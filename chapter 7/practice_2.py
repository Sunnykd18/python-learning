spamwords = ["buy now","subscribe","click this"]

email = input("enter the mail: ").lower()
spam = False
if("buy now" in email):
    spam = True
    

if("subscribe" in email):
    spam = True


if("clicks this" in email):
    spam = True

print("spam is", spam)