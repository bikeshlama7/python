import random

# ASCII Art for moves
moves_art = {
    1: r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    2: r""" 
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    3: r""" 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

# Move names
move_names = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

# Computer choice
computer_choice = random.randint(1, 3)

# User input
try:
    user_choice = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
    if user_choice not in [1, 2, 3]:
        print("Invalid input")
    else:
        print(f"\nYou chose {move_names[user_choice]}:\n{moves_art[user_choice]}")
        print(f"Computer chose {move_names[computer_choice]}:\n{moves_art[computer_choice]}")

        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == 1 and computer_choice == 3) or \
             (user_choice == 2 and computer_choice == 1) or \
             (user_choice == 3 and computer_choice == 2):
            print("You win!")
        else:
            print("You lose!")
except ValueError:
    print("Please enter a valid number (1, 2, or 3).")