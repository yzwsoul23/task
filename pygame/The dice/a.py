import random
import time
def dice():
    player = random.randint(1,6)
    print("You rolled " + str(player) )
    ai = random.randint(1,6)
    print("The computer rolls...." )
    time.sleep(2)
    print("The computer has rolled a " + str(player) )
    if player > ai :
        print("You win")  # notice indentation
    else:
        print("You lose")
    print("Quit? Y/N")
    cont = input()
    if cont == "Y" or cont == "y":
        exit()
    elif cont == "N" or cont == "n":
        pass
    else:
        print("I did not understand that. Playing again.")