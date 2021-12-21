with open("poem.txt", "r") as f:
    if("twinkle" in f.read()):
        print("yes twinkle is present")
    else:
        print("the word twinkle is not present")    