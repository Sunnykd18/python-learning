import random

def swg(comp,player):
    if (comp == player):
        return None
    if(comp =='s' and player == 'g'):
        return True
    elif(comp == 'w' and player == 's'):
        return True
    elif(comp == 'g' and player == 'w'):
        return True
    else:
        return False   

choice = ('s','w','g')
comp = random.randint(0,2)
comp = choice[comp]
player = input("choice either s, w or g : ") 

win = swg(comp,player)
print(f"you choose {player} and the comp chose {comp}")
if win is None:
    print("match drawn")
if win:
     print("You won")
else:
     print("You lose")