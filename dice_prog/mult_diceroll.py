import random
import time

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    time.sleep(2)
    fir = random.randint(1,6)
    sec = random.randint(1,6)
    print("Your first number is: ")
    time.sleep(2)
    print(fir)
    print("Your second number is: ")
    time.sleep(2) 
    print(sec)
    roll_again=input("Vuoi continuare a giocare? (yes/y)")

print("You ended the game!")    