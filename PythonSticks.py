
import random

stickPreset = [1,3,5,7]
currentSticks = [1,3,5,7]
name = "Not Entered"
playerMove = False

print("Welcome to Nim")
name = input("Enter name:")
print("Welcome " + name)

if random.randrange(0,100) >= 50:
    print("CPU goes first!")
    playerMove = False
else:
    print("Player goes first!")
    playerMove = True
    
def DisplaySticks(currentSticks):
    for x in currentSticks:
        print("I" * x)

while(sum(currentSticks) > 0):
    DisplaySticks(currentSticks)
    name = input("Enter name:")
