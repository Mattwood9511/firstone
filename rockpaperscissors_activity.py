# import random

# def get_user_choice():
#     while True:
#         user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
#         if user_choice in ["rock", "paper", "scissors"]:
#             return user_choice
#         else:
#             print("Invalid choice. Please choose rock, paper, or scissors.")

# def determine_winner(user, computer):
#     if user == computer:
#         return "It's a tie!"
#     elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
#         return "You win!"
#     else:
#         return "Computer wins!"

# def play_game():
#     user_score = 0
#     computer_score = 0

#     for _ in range(7):
#         user_choice = get_user_choice()
#         computer_choice = random.choice(["rock", "paper", "scissors"])

#         print(f"Computer chose {computer_choice}")
#         result = determine_winner(user_choice, computer_choice)
#         print(result)

#         if result == "You win!":
#             user_score += 1
#         elif result == "Computer wins!":
#             computer_score += 1

#     print("\nGame Over!")
#     print(f"Your score: {user_score} | Computer score: {computer_score}")
#     if user_score > computer_score:
#         print("Congratulations! You win!")
#     elif user_score < computer_score:
#         print("Computer wins! Better luck next time.")
#     else:
#         print("It's a tie!")

# # Start the game
# play_game()


##  GAME 2


# import random
# import colorama
# from colorama import Fore, Style

# # Initialize Colorama
# colorama.init()

# def get_user_choice():
#     while True:
#         user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
#         if user_choice in ["rock", "paper", "scissors"]:
#             return user_choice
#         else:
#             print("Invalid choice. Please choose rock, paper, or scissors.")

# def determine_winner(user, computer):
#     if user == computer:
#         return "It's a tie!"
#     elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
#         return "You win!"
#     else:
#         return "Computer wins!"

# def play_game():
#     user_score = 0
#     computer_score = 0

#     print("\nLet's play Rock-Paper-Scissors!\n")

#     for _ in range(7):
#         user_choice = get_user_choice()
#         computer_choice = random.choice(["rock", "paper", "scissors"])

#         print(f"\nComputer chose {Fore.YELLOW}{computer_choice}{Style.RESET_ALL}")

#         result = determine_winner(user_choice, computer_choice)
#         print(result)

#         if result == "You win!":
#             user_score += 1
#         elif result == "Computer wins!":
#             computer_score += 1

#         print(f"Score: You {user_score} - {computer_score} Computer\n")

#     print("\nGame Over!")
#     if user_score > computer_score:
#         print(f"{Fore.GREEN}Congratulations! You win!{Style.RESET_ALL}")
#     elif user_score < computer_score:
#         print(f"{Fore.RED}Computer wins! Better luck next time.{Style.RESET_ALL}")
#     else:
#         print("It's a tie!")

# # Start the game
# play_game()



## GAME 3

import random

# ASCII art for rock, paper, and scissors
rock_art = '''
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_art = '''
  _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_art = '''
  _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0

    print("\nLet's play Rock-Paper-Scissors!\n")

    for _ in range(7):
        user_choice = get_user_choice()
        computer_choice = random.choice(["rock", "paper", "scissors"])

        print(f"\nComputer chose:")
        if computer_choice == "rock":
            print(rock_art)
        elif computer_choice == "paper":
            print(paper_art)
        else:
            print(scissors_art)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer\n")

    print("\nGame Over!")
    if user_score > computer_score:
        print("Congratulations! You win!")
    elif user_score < computer_score:
        print("Computer wins! Better luck next time.")
    else:
        print("It's a tie!")

# Start the game
play_game()