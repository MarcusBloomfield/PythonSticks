
import random


def main():
    
    name = "Not Entered"
    players = ["Player", "CPU"]
    currentPlayer = "CPU"
    continuePlaying = True
    wins = 0
    losses = 0
    
    print("Welcome to Nim")
    name = input("Enter name:")

    while continuePlaying:

        # set the starting player and set the currentSticks
        currentPlayer = random.choice(players)
        currentSticks = [1,3,5,7]

        #Display the intial set of sticks
        DisplaySticks(currentSticks)

        while sum(currentSticks) > 0:
            
            if currentPlayer == "Player":
                print(f"It is {name}'s turn")
                
                #take the player input 
                row = GetRow(currentSticks)
                stickAmount = GetStickAmount(currentSticks, row)
                
                # update the current sticks array using the players moves
                currentSticks = TakeSticks(currentSticks, row, stickAmount)

                # display the players moves
                PrintMove("Player", row, stickAmount)
                DisplaySticks(currentSticks)

                # set the current player to the computer
                currentPlayer = "CPU"

            else :
                print("It is CPUs turn")

                # define the cpus moves
                row = random.randint(0,3)
                while currentSticks[row] == 0:
                    row = random.randint(0,3)
                stickAmount = random.randint(1, currentSticks[row])

                # update the current sticks array using the cpus moves
                currentSticks = TakeSticks(currentSticks, row, stickAmount)

                # Display the CPUS move
                PrintMove("CPU", row, stickAmount)
                DisplaySticks(currentSticks)

                # set the current player to the human
                currentPlayer = "Player"

        
        print("Game Over!")
        # if the current player is set to the cpu when there are no sticks left it means the player has won
        if currentPlayer == "CPU":
            print(f"{name} wins!")
            wins += 1
        else:
            print("CPU wins!")
            losses += 1
            
        print(f"Total Wins: {wins}")
        print(f"Total Losses: {losses}")
        
        # if the player enters anything other then yes the game ends
        continuePlaying = input("Would you like to play again? (yes/no): ").lower() == "yes"
                
def DisplaySticks(currentSticks):
    print()
    rowNumber = 0;
    for x in currentSticks:
        print(str(rowNumber + 1) + ". " + "I" * x)
        rowNumber += 1
    print("================================")

def GetRow(currentSticks):
    row = 0
    while row == 0:
        # take the player input and set the input to an interger value 
        rowInput = int(input("From which row would you like to take sticks? (1-4): "))

        # check if the input is within parameters
        if 1 <=  rowInput  <= 4 and currentSticks[rowInput  - 1] > 0:
            row = rowInput
        else:
            print("Invalid row, please try again.")
    # return the row interger - 1 so we can use it in arrays correctly
    return row - 1

def GetStickAmount(currentSticks, row):
    stickAmount = 0
    while stickAmount == 0:
        # take the player input and set the input to an interger value
        stickInput = int(input("How many sticks would you like to take? (1-7): "))
        
        # check if the input is within parameters
        if currentSticks[row] >= stickInput and stickInput > 0:
            stickAmount = stickInput
        else:
            print("Invalid stick amount, please try again.")
    return stickAmount

def TakeSticks(currentSticks, row, stickAmount):
    # remove the sticks from the array using the parameters and return the array
    currentSticks[row ] -= stickAmount
    return currentSticks

def PrintMove(player, row, sticks):
    # display the move of who ever just made a move
    print(f"{player} takes {sticks} stick(s) from row {row + 1}")

if __name__ == "__main__":
    main()