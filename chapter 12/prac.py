try:
    with open('1.txt','r') as f:
        f.read()

    with open('1.txt','r') as f:
        f.read()
    with open('3.txt','r') as f:
        f.read()
                
except Exception as e :
    print(f"the file is not present. reason: {e}")
print("thanks for using this program")    