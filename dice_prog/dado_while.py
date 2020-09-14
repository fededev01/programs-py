import random
import time

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
  print("Rolling the dice...")
  time.sleep(1)
  num = random.randint(1,6)
  print("Your number is: ")
  print(num)
  roll_again = input("Do you want to roll again? (yes/y)")



print("You ended the game!")  

