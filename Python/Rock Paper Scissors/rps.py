# Write code below 💖

import random

print("=================================")
print("Rock Paper Scissors Lizzard Spock")
print("=================================")
print("")

cp_score = 0
p_score = 0

print("CPU Score: " + str(cp_score))
print("Player Score: " + str(p_score))
print("")

list = [
  '1) is for “✊” (Rock).',
  '2) is for “✋” (Paper).',
  '3) is for “✌” (Scissors).',
  '4) is for “🦎” (Lizzard).',
  '5) is for “🖖” (Spock).'
]

for i in range(len(list)):
  print(list[i])
print("")

while cp_score < 2 and p_score < 2:
  player = int(input('Enter your choice: '))
  computer = random.randint(1 , 5)
  # break
  print("")
  if computer == 3 and player == 2:
    print("Computer choose Scissors")
    print("You choose Paper")
    print("You Lose!")
    cp_score = cp_score + 1
  elif computer == 2 and player == 3:
    print("Computer choose Paper")
    print("You choose Scissors")
    print("You Win!")
    p_score = p_score + 1
    #Paper vs Scissors
  elif computer == 2 and player == 1:
    print("Computer choose Paper")
    print("You choose Rock")
    print("You Lose!")
    cp_score = cp_score + 1
  elif computer == 1 and player == 2:
    print("Computer choose Rock")
    print("You choose Paper")
    print("You Win!")
    p_score = p_score + 1
    #Rock vs Paper
  elif computer == 1 and player == 4:
    print("Computer choose Rock")
    print("You choose Lizzard")
    print("You Lose!")
    cp_score = cp_score + 1
  elif computer == 4 and player == 1:
    print("Computer choose Lizzard")
    print("You choose Rock")
    print("You Win!")
    p_score = p_score + 1
    #Rock vs Lizzard
  elif computer == 4 and player == 5:
    print("Computer choose Lizzard")
    print("You choose Spock")
    print("You Lose!")
    cp_score = cp_score + 1
  elif computer == 5 and player == 4:
    print("Computer choose Spock")
    print("You choose Lizard")
    print("You Win!")
    p_score = p_score + 1
    #Lizzard vs Spock
  elif computer == 5 and player == 3:
    print("Computer choose Spock")
    print("You choose Scissors")
    print("You Lose!")
    cp_score = cp_score + 1
  elif computer == 3 and player == 5:
    print("Computer choose Scissors")
    print("You choose Spock")
    print("You Win!")
    p_score = p_score + 1
    #Spock vs Scissors
  elif computer == 3 and player == 4:
    print("Computer choose Scissors")
    print("You choose Lizard")
    print("You Lose!")
    cp_score = cp_score + 1
  elif computer == 4 and player == 3:
    print("Computer choose Lizard")
    print("You choose Scissors")
    print("You Win!")
    p_score = p_score + 1
    #Scissors vs Lizard
  elif computer == 4 and player == 2:
    print("Computer choose Lizard")
    print("You choose Paper")
    print("You Lose!")
    cp_score = cp_score + 1
  elif computer == 2 and player == 4:
    print("Computer choose Paper")
    print("You choose Lizard")
    print("You Win!")
    p_score = p_score + 1
    #Lizard vs Paper
  elif computer == 2 and player == 5:
    print("Computer choose Paper")
    print("You choose Spock")
    print("You Lose!")
    cp_score = cp_score + 1
  elif computer == 5 and player == 2:
    print("Computer choose Spock")
    print("You choose Paper")
    print("You Win!")
    p_score = p_score + 1
    #Paper vs Spock
  elif computer == 5 and player == 1:
    print("Computer choose Spock")
    print("You choose Rock")
    print("You Lose!")
    cp_score = cp_score + 1
  elif computer == 1 and player == 5:
    print("Computer choose Rock")
    print("You choose Spock")
    print("You Win!")
    p_score = p_score + 1
    #Spock vs Rock
  elif computer == 1 and player == 3:
    print("Computer choose Rock")
    print("You choose Scissors")
    print("You Lose!")
    cp_score = cp_score + 1
  elif computer == 3 and player == 1:
    print("Computer choose Scissors")
    print("You choose Rock")
    print("You Win!")
    p_score = p_score + 1
    #Rock vs Scissors
  else:
    print("You have the same answer")
    print("It's a TIE")

  print("")
  print("CPU score: " + str(cp_score))
  print("Player score: " + str(p_score))
  print("")

if cp_score == 3:
  print("WHAT A LOSER!")

if p_score == 3:
  print("EZ PEAZYYY!")