# def swap_head_tail(arr):
#     # Calculate the midpoint of the array
#     mid = len(arr) // 2
    
#     # Swap the head and tail using slicing
#     swapped_arr = arr[mid:] + arr[:mid]
    
#     return swapped_arr

# # Example usage
# original_array = [1, 2, 3, 4, 5, 6, 7, 8]
# swapped_array = swap_head_tail(original_array)
# print(swapped_array)

import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    score = 0
    while score < 20:
        input("Press Enter to roll the dice...")
        dice_roll = roll_dice()
        print("You rolled:", dice_roll)
        if dice_roll == 1:
            print("You rolled a 1. You lose your score.")
            score = 0
        else:
            score += dice_roll
            print("Your current score is:", score)
        if score >= 20:
            print("Congratulations! You've reached a score of 20. You win!")
            break

play_game()
