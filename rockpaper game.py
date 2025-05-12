import random as r # random stuff

things = ["rock", "paper", "scissors"]  # the three options

player = input("Choose rock, paper or scissors: ") # ask user
com = r.choice(things)  # computer picks one randomly

print("Computer picked", com)  # show what computer picked

# checking all possibilities
if player == com:
    print("Draw")
elif (player == "0" and com == "2") or \
     (player == "2" and com == "1") or \
     (player == "1" and com == "0"):
    print("You win.")
else:
    print("You lost!")
