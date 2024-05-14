# print("these are my library notes")
# import random

# print(random.random())

# import random
# random_number = random.randint(0, 1000)
# print(f"Random number: {random_number}")

# import random
# from colorama import Fore, back, style

# my_number = 11

# rand_num = random.randint(1,50)

# while my_number != rand_num:
#     print(f"i've picked: {rand_num}")
#     rand_num = random.randint(1,50)

# print (f"you picked {my_number}and i picked {rand_num}")

# import colorama
# from colorama import Fore, Back, Style

# # Initialize Colorama
# colorama.init()

# # Example: Print numbers in different colors
# print(Fore.RED + "Red Number: 42")
# print(Fore.GREEN + "Green Number: 123")
# print(Fore.BLUE + "Blue Number: 987")

# # Reset color settings
# print(Style.RESET_ALL + "Back to normal text")

# # You can also change the background color:
# print(Back.YELLOW + Fore.BLACK + "Yellow Background with Black Text")

# # Reset color settings again
# print(Style.RESET_ALL + "Back to normal text")

# # Note: Make sure to reset the color settings after using them.

# # Available colors:
# # Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE
# # Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE

# # You can also apply styles like BRIGHT, DIM, etc. (e.g., Style.BRIGHT + Fore.RED)

import datetime

def days_alive(birthdate):
    today = datetime.date.today()
    birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d").date()
    days = (today - birthdate).days
    return days

# Example usage: Replace "YYYY-MM-DD" with your actual birthdate
birthdate_str = "1995-01-11"
days_lived = days_alive(birthdate_str)
print(f"You've been alive for {days_lived} days!")