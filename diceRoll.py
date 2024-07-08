import random

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total
def players(count):
    player = []
    for i in range(count):
        player.append(input("Enter player name"))
    return player
def whoWon(Tally):
    max = 0
    for i in range(len(Tally)):
        if Tally[i] > Tally[max]:
            max = i
    return max+1
    
count = int(input("How many players?"))
i=0
runTally = []
for players in players(count):
    runTally.append(roll_dice())
    print(runTally[i],'\n')
    i+=1
print("Player " + str(whoWon(runTally)) + " has won")