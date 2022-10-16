rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
choice=int(input())
if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
  
computerchoice = int(random.randint(0,2))
if computerchoice == 0:
  print(rock)
elif computerchoice == 1:
  print(paper)
elif computerchoice == 2:
  print(scissors)
  
if choice == 0:
  if computerchoice == 1:
    print('Computer win you play Rock computer Paper and Paper covers Rock')
  elif computerchoice == 2:
    print('Human win you play Rock computer Scissors and Rock dulls Scissors')
  elif computerchoice == 0:
    print('Human draw both play Rock')
elif choice == 1:
  if computerchoice == 1:
    print('Human draw both play Paper')
  elif computerchoice == 2:
    print('Computer win you play Paper Computer Scissors and Scissors cuts Paper')
  elif computerchoice == 0:
    print('Human win you play Paper computer Rock and Paper covers Rock')
elif choice == 2:
  if computerchoice == 1:
    print('Human win you play Scissors computer Paper and Scissors cuts Paper')
  elif computerchoice == 2:
    print('Human draw both play Scissors')
  elif computerchoice == 0:
    print('Computer win you play Scissors Computer Rock and Rock dulls Scissors')
  
#* How you will store the user's input.
#* How you will generate a random choice for the computer.
#* How you will compare the user's and the computer's choice to determine the winner (or a draw).
#* And also how you will give feedback to the player. 
