# class QuizGame:
#     def __init__(self, questions):
#         self.questions = questions
#         self.score = 0

#     def display_question(self, question):
#         print(question)

#     def display_score(self):
#         print("Your score is:", self.score)

#     def play(self):
#         for question, answer in self.questions.items():
#             self.display_question(question)
#             user_answer = input("Your answer: ")
#             if user_answer.lower() == answer.lower():
#                 print("Correct!")
#                 self.score += 1
#             else:
#                 print("Incorrect.")
#             self.display_score()


# # Example usage:
# if __name__ == "__main__":
#     questions = {
#         "What is the capital of France?": "Paris",
#         "What is the largest planet in our solar system?": "Jupiter",
#         "Who wrote 'Romeo and Juliet'?": "William Shakespeare"
#     }

#     game = QuizGame(questions)
#     game.play()

##VERSION 2

# class QuizGame:
#     def __init__(self, questions):
#         self.questions = questions
#         self.score = 0

#     def display_question(self, question):
#         print(question)

#     def display_score(self):
#         print("Your score is:", self.score)

#     def play(self):
#         for question, answer in self.questions.items():
#             self.display_question(question)
#             while True:
#                 user_answer = input("Your answer: ")
#                 if user_answer.lower() == answer.lower():
#                     print("Correct!")
#                     self.score += 1
#                     break
#                 else:
#                     print("Incorrect. Try again.")

#             self.display_score()


# # Example usage:
# if __name__ == "__main__":
#     questions = {
#         "What is the capital of France?": "Paris",
#         "What is the largest planet in our solar system?": "Jupiter",
#         "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
#         "which city has the worlds tallest building'?": "Dubai",
#         "who was the first US president'?": "George Washington"
#     }

#     game = QuizGame(questions)
#     game.play()

##VERSION 3

# class QuizGame:
#     def __init__(self, questions):
#         self.questions = questions
#         self.score = 0

#     def display_question(self, question):
#         print(question)

#     def display_score(self):
#         print("Your score is:", self.score)

#     def play(self):
#         for question, answer in self.questions.items():
#             self.display_question(question)
#             while True:
#                 user_answer = input("Your answer: ")
#                 if user_answer.lower() == answer.lower():
#                     print("Correct! You earn 2 points.")
#                     self.score += 2
#                     break
#                 else:
#                     print("Incorrect. You lose 1 point. Try again.")
#                     self.score = max(0, self.score - 1)

#             self.display_score()
#             if self.score >= 20:
#                 print("Congratulations! You win!")
#                 break


# # Example usage:
# if __name__ == "__main__":
#     questions = {
#         "What is the capital of France?": "Paris",
#         "What is the largest planet in our solar system?": "Jupiter",
#         "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
#         "What is the tallest mountain in the world?": "Mount Everest",
#         "How many continents are there in the world?": "7",
#         "What is the chemical symbol for water?": "H2O",
#         "Who painted the Mona Lisa?": "Leonardo da Vinci",
#         "What is the currency of Japan?": "Yen",
#         "What is the square root of 144?": "12",
#         "What is the capital of Australia?": "Canberra",
#         "Which planet is known as the Red Planet?": "Mars",
#         "Who discovered penicillin?": "Alexander Fleming",
#         "What is the largest ocean on Earth?": "Pacific Ocean",
#         "Which country is known as the Land of the Rising Sun?": "Japan",
#         "Who was the first man to step on the moon?": "Neil Armstrong",
#         "What is the main ingredient in guacamole?": "Avocado",
#         "What is the boiling point of water in Celsius?": "100",
#         "What is the chemical symbol for gold?": "Au",
#         "What year did World War II end?": "1945",
#         "Who wrote 'To Kill a Mockingbird'?": "Harper Lee"
#     }

#     game = QuizGame(questions)
#     game.play()


    ##VERSION 3

# class QuizGame:
#     def __init__(self, questions):
#         # Initialize the game with a dictionary of questions and answers
#         self.questions = questions
#         self.score = 0  # Initialize the score to 0

#     def display_question(self, question):
#         # Display a question to the player
#         print(question)

#     def display_score(self):
#         # Display the player's current score
#         print("Your score is:", self.score)

#     def play(self):
#         # Main method to play the quiz game
#         for question, answer in self.questions.items():  # Iterate over each question in the dictionary
#             self.display_question(question)  # Display the current question to the player
#             while True:  # Keep looping until the player gives a correct answer
#                 user_answer = input("Your answer: ")  # Get the player's answer
#                 if user_answer.lower() == answer.lower():  # Check if the answer is correct
#                     print("Correct! You earn 2 points.")  # Inform the player that the answer is correct
#                     self.score += 2  # Increase the player's score by 2 points
#                     break  # Exit the loop since the correct answer was given
#                 else:
#                     # Inform the player that the answer is incorrect and prompt them to try again
#                     print("Incorrect. You lose 1 point. Try again.")
#                     # Deduct 1 point from the player's score, but ensure it doesn't go below 0
#                     self.score = max(0, self.score - 1)

#             self.display_score()  # Display the player's current score after each question
#             if self.score >= 20:  # Check if the player's score reaches 20
#                 print("Congratulations! You win!")  # Inform the player that they have won
#                 break  # Exit the loop since the player has reached the winning score


# # Example usage:
# if __name__ == "__main__":
#     # Dictionary containing questions as keys and their corresponding answers as values
#     questions = {
#         "What is the capital of France?": "Paris",
#         "What is the largest planet in our solar system?": "Jupiter",
#         "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
#         "What is the tallest mountain in the world?": "Mount Everest",
#         "How many continents are there in the world?": "7",
#         "What is the chemical symbol for water?": "H2O",
#         "Who painted the Mona Lisa?": "Leonardo da Vinci",
#         "What is the currency of Japan?": "Yen",
#         "What is the square root of 144?": "12",
#         "What is the capital of Australia?": "Canberra",
#         "Which planet is known as the Red Planet?": "Mars",
#         "Who discovered penicillin?": "Alexander Fleming",
#         "What is the largest ocean on Earth?": "Pacific Ocean",
#         "Which country is known as the Land of the Rising Sun?": "Japan",
#         "Who was the first man to step on the moon?": "Neil Armstrong",
#         "What is the main ingredient in guacamole?": "Avocado",
#         "What is the boiling point of water in Celsius?": "100",
#         "What is the chemical symbol for gold?": "Au",
#         "What year did World War II end?": "1945",
#         "Who wrote 'To Kill a Mockingbird'?": "Harper Lee"
#         # Add more questions here...
#     }

#     # Create an instance of the QuizGame class with the questions dictionary
#     game = QuizGame(questions)
#     # Start playing the game
#     game.play()

##Version 4

# class QuizGame:
#     def __init__(self, questions):
#         self.questions = questions
#         self.score = 0

#     def display_question(self, question, choices):
#         print(question)
#         for index, choice in enumerate(choices, start=1):
#             print(f"{index}. {choice}")
        
#     def display_score(self):
#         print("Your score is:", self.score)

#     def play(self):
#         for question, (choices, answer) in self.questions.items():
#             self.display_question(question, choices)
#             while True:
#                 user_answer = input("Your answer: ")
#                 if user_answer.isdigit() and 1 <= int(user_answer) <= len(choices):
#                     if choices[int(user_answer) - 1].lower() == answer.lower():
#                         print("Correct! You earn 2 points.")
#                         self.score += 2
#                     else:
#                         print("Incorrect. You lose 1 point.")
#                         self.score = max(0, self.score - 1)
#                     break
#                 else:
#                     print("Invalid choice. Please enter the number corresponding to your answer.")

#             self.display_score()
#             if self.score >= 20:
#                 print("Congratulations! You win!")
#                 break


# # Example usage:
# if __name__ == "__main__":
#     print("Welcome to the Quiz Game!")
#     print("In this game, you will earn 2 points for each correct answer, but you will lose 1 point for each incorrect answer.")
#     print("Let's begin!\n")

#     questions = {
#         "What is the capital of France?": (["a. Paris", "b. Rome", "c. Berlin", "d. London"], "a"),
#         "What is the largest planet in our solar system?": (["a. Mars", "b. Venus", "c. Jupiter", "d. Saturn"], "c"),
#         "Who wrote 'Romeo and Juliet'?": (["a. Charles Dickens", "b. William Shakespeare", "c. Jane Austen", "d. Mark Twain"], "b"),
#         "What is the tallest mountain in the world?": (["a. Mount Everest", "b. K2", "c. Kangchenjunga", "d. Lhotse"], "a"),
#         "What is the main ingredient in guacamole?": (["a. Avocado", "b. Tomato", "c. Onion", "d. Garlic"], "a"),
#         "What is the chemical symbol for gold?": (["a. Ag", "b. Au", "c. Pt", "d. Cu"], "b"),
#         "What year did World War II end?": (["a. 1943", "b. 1944", "c. 1945", "d. 1946"], "c"),
#         "Who wrote 'To Kill a Mockingbird'?": (["a. Harper Lee", "b. J.D. Salinger", "c. F. Scott Fitzgerald", "d. Ernest Hemingway"], "a"),
#         "What is the largest ocean on Earth?": (["a. Atlantic Ocean", "b. Indian Ocean", "c. Arctic Ocean", "d. Pacific Ocean"], "d"),
#         "What is the chemical symbol for water?": (["a. O", "b. H2O", "c. H2", "d. HO"], "b"),
#         "What is the boiling point of water in Celsius?": (["a. 0°C", "b. 50°C", "c. 100°C", "d. 200°C"], "c"),
#         "Who discovered penicillin?": (["a. Alexander Fleming", "b. Louis Pasteur", "c. Marie Curie", "d. Robert Koch"], "a"),
#         "What is the currency of Japan?": (["a. Dollar", "b. Euro", "c. Yen", "d. Yuan"], "c"),
#         "Who was the first man to step on the moon?": (["a. Neil Armstrong", "b. Buzz Aldrin", "c. Michael Collins", "d. Alan Shepard"], "a"),
#         "Which planet is known as the Red Planet?": (["a. Venus", "b. Mars", "c. Jupiter", "d. Saturn"], "b"),
#         "What is the tallest building in the world?": (["a. Shanghai Tower", "b. Burj Khalifa", "c. Abraj Al-Bait Clock Tower", "d. Ping An Finance Centre"], "b"),
#         "What is the chemical symbol for oxygen?": (["a. O", "b. O2", "c. O3", "d. H2O"], "a"),
#         "What is the smallest prime number?": (["a. 1", "b. 2", "c. 3", "d. 4"], "b"),
#         "Who is known as the 'Father of Computers'?": (["a. Alan Turing", "b. Charles Babbage", "c. Ada Lovelace", "d. John von Neumann"], "b"),
#         "What is the largest organ in the human body?": (["a. Liver", "b. Brain", "c. Heart", "d. Skin"], "d"),
#         "What is the only mammal capable of true flight?": (["a. Bat", "b. Bird", "c. Butterfly", "d. Bee"], "a"),
#     }

#     game = QuizGame(questions)
#     game.play()

# Version 5

# from colorama import Fore, Style
# import random

# class QuizGame:
#     def __init__(self, questions):
#         self.questions = questions
#         self.score = 0

#     def display_question(self, question, choices):
#         print(Fore.BLUE + question)
#         for index, choice in enumerate(choices, start=1):
#             print(f"{index}. {choice}")
#         print(Style.RESET_ALL)
        
#     def display_score(self):
#         print("Your score is:", self.score)

#     def play(self):
#         for question, (choices, answer) in self.questions.items():
#             self.display_question(question, choices)
#             while True:
#                 user_answer = input("Your answer (1, 2, 3, or 4): ")
#                 if user_answer.isdigit() and 1 <= int(user_answer) <= len(choices):
#                     if choices[int(user_answer) - 1].lower() == answer.lower():
#                         print(Fore.GREEN + "Correct! You earn 2 points.")
#                         self.score += 2
#                     else:
#                         print(Fore.RED + "Incorrect. You lose 1 point.")
#                         self.score = max(0, self.score - 1)
#                     break
#                 else:
#                     print("Invalid choice. Please enter the number corresponding to your answer.")

#             self.display_score()
#             if self.score >= 20:
#                 print(Fore.YELLOW + "Congratulations! You win!")
#                 break


# # Example usage:
# if __name__ == "__main__":
#     print(Fore.MAGENTA + "Welcome to the Quiz Game!")
#     print("In this game, you will earn 2 points for each correct answer, but you will lose 1 point for each incorrect answer.")
#     print("Let's begin!\n")
#     print(Style.RESET_ALL)

#     questions = {
#         "What is the capital of France?": (["Paris", "Rome", "Berlin", "London"], "Paris"),
#         "What is the largest planet in our solar system?": (["Mars", "Venus", "Jupiter", "Saturn"], "Jupiter"),
#         "Who wrote 'Romeo and Juliet'?": (["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], "William Shakespeare"),
#         "What is the tallest mountain in the world?": (["Mount Everest", "K2", "Kangchenjunga", "Lhotse"], "Mount Everest"),
#         "What is the main ingredient in guacamole?": (["Avocado", "Tomato", "Onion", "Garlic"], "Avocado"),
#         "What is the chemical symbol for gold?": (["Ag", "Au", "Pt", "Cu"], "Au"),
#         "What year did World War II end?": (["1943", "1944", "1945", "1946"], "1945"),
#         "Who wrote 'To Kill a Mockingbird'?": (["Harper Lee", "J.D. Salinger", "F. Scott Fitzgerald", "Ernest Hemingway"], "Harper Lee"),
#         "What is the largest ocean on Earth?": (["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "Pacific Ocean"),
#         "What is the chemical symbol for water?": (["O", "H2O", "H2", "HO"], "H2O"),
#         "What is the boiling point of water in Celsius?": (["0°C", "50°C", "100°C", "200°C"], "100°C"),
#         "Who discovered penicillin?": (["Alexander Fleming", "Louis Pasteur", "Marie Curie", "Robert Koch"], "Alexander Fleming"),
#         "What is the currency of Japan?": (["Dollar", "Euro", "Yen", "Yuan"], "Yen"),
#         "Who was the first man to step on the moon?": (["Neil Armstrong", "Buzz Aldrin", "Michael Collins", "Alan Shepard"], "Neil Armstrong"),
#         "Which planet is known as the Red Planet?": (["Venus", "Mars", "Jupiter", "Saturn"], "Mars"),
#         "What is the tallest building in the world?": (["Shanghai Tower", "Burj Khalifa", "Abraj Al-Bait Clock Tower", "Ping An Finance Centre"], "Burj Khalifa"),
#         "What is the chemical symbol for oxygen?": (["O", "O2", "O3", "H2O"], "O"),
#         "What is the smallest prime number?": (["1", "2", "3", "4"], "2"),
#         "Who is known as the 'Father of Computers'?": (["Alan Turing", "Charles Babbage", "Ada Lovelace", "John von Neumann"], "Charles Babbage"),
#         "What is the largest organ in the human body?": (["Liver", "Brain", "Heart", "Skin"], "Skin"),
#         "What is the only mammal capable of true flight?": (["Bat", "Bird", "Butterfly", "Bee"], "Bat"),
#     }

#     game = QuizGame(questions)
#     game.play()

##Version 6

# from colorama import Fore, Style
# import random

# class QuizGame:
#     def __init__(self, questions):
#         self.questions = questions
#         self.score = 0

#     def display_question(self, question, choices):
#         print(Fore.BLUE + question)
#         for index, choice in enumerate(choices, start=1):
#             print(f"{index}. {choice}")
#         print(Style.RESET_ALL)
        
#     def display_score(self):
#         print("Your score is:", self.score)

#     def play(self):
#         for question, (choices, answer) in self.questions.items():
#             self.display_question(question, choices)
#             while True:
#                 user_answer = input("Your answer (1, 2, 3, or 4): ")
#                 if user_answer.isdigit() and 1 <= int(user_answer) <= len(choices):
#                     if choices[int(user_answer) - 1].lower() == answer.lower():
#                         print(Fore.GREEN + "Correct! You earn 2 points.")
#                         self.score += 2
#                     else:
#                         print(Fore.RED + "Incorrect. You lose 1 point.")
#                         print("""
# (`-').->(`-')  _   (`-')  
#    <-.        .->    ( OO)_  ( OO).-/<-.(OO )  
#  ,--. )  (`-')----. (_)--\_)(,------.,------,) 
#  |  (`-')( OO).-.  '/    _ / |  .---'|   /`. ' 
#  |  |OO )( _) | |  |\_..`--.(|  '--. |  |_.' | 
# (|  '__ | \|  |)|  |.-._)   \|  .--' |  .   .' 
#  |     |'  '  '-'  '\       /|  `---.|  |\  \  
#  `-----'    `-----'  `-----' `------'`--' '--'""")
#                         self.score = max(0, self.score - 1)
#                     break
#                 else:
#                     print("Invalid choice. Please enter the number corresponding to your answer.")

#             self.display_score()
#             if self.score >= 20:
#                 print(Fore.YELLOW + "Congratulations! You win!")
#                 break


# # Example usage:
# if __name__ == "__main__":
#     print(Fore.MAGENTA + "Welcome to the Quiz Game!")
#     print("In this game, you will earn 2 points for each correct answer, but you will lose 1 point for each incorrect answer.")
#     print("Let's begin!\n")
#     print(Style.RESET_ALL)

#     questions = {
#         "What is the capital of France?": (["Paris", "Rome", "Berlin", "London"], "Paris"),
#         "What is the largest planet in our solar system?": (["Mars", "Venus", "Jupiter", "Saturn"], "Jupiter"),
#         "Who wrote 'Romeo and Juliet'?": (["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], "William Shakespeare"),
#         "What is the tallest mountain in the world?": (["Mount Everest", "K2", "Kangchenjunga", "Lhotse"], "Mount Everest"),
#         "What is the main ingredient in guacamole?": (["Avocado", "Tomato", "Onion", "Garlic"], "Avocado"),
#         "What is the chemical symbol for gold?": (["Ag", "Au", "Pt", "Cu"], "Au"),
#         "What year did World War II end?": (["1943", "1944", "1945", "1946"], "1945"),
#         "Who wrote 'To Kill a Mockingbird'?": (["Harper Lee", "J.D. Salinger", "F. Scott Fitzgerald", "Ernest Hemingway"], "Harper Lee"),
#         "What is the largest ocean on Earth?": (["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "Pacific Ocean"),
#         "What is the chemical symbol for water?": (["O", "H2O", "H2", "HO"], "H2O"),
#         "What is the boiling point of water in Celsius?": (["0°C", "50°C", "100°C", "200°C"], "100°C"),
#         "Who discovered penicillin?": (["Alexander Fleming", "Louis Pasteur", "Marie Curie", "Robert Koch"], "Alexander Fleming"),
#         "What is the currency of Japan?": (["Dollar", "Euro", "Yen", "Yuan"], "Yen"),
#         "Who was the first man to step on the moon?": (["Neil Armstrong", "Buzz Aldrin", "Michael Collins", "Alan Shepard"], "Neil Armstrong"),
#         "Which planet is known as the Red Planet?": (["Venus", "Mars", "Jupiter", "Saturn"], "Mars"),
#         "What is the tallest building in the world?": (["Shanghai Tower", "Burj Khalifa", "Abraj Al-Bait Clock Tower", "Ping An Finance Centre"], "Burj Khalifa"),
#         "What is the chemical symbol for oxygen?": (["O", "O2", "O3", "H2O"], "O"),
#         "What is the smallest prime number?": (["1", "2", "3", "4"], "2"),
#         "Who is known as the 'Father of Computers'?": (["Alan Turing", "Charles Babbage", "Ada Lovelace", "John von Neumann"], "Charles Babbage"),
#         "What is the largest organ in the human body?": (["Liver", "Brain", "Heart", "Skin"], "Skin"),
#         "What is the only mammal capable of true flight?": (["Bat", "Bird", "Butterfly", "Bee"], "Bat"),
#     }

#     game = QuizGame(questions)
#     game.play()

##Version 7


    # Importing necessary modules
from colorama import Fore, Style  # For colored output
import random  # For shuffling questions (not used in this version)

# Class definition for the QuizGame
class QuizGame:
    # Constructor method to initialize the game with questions
    def __init__(self, questions):
        self.questions = questions  # Store questions dictionary
        self.score = 0  # Initialize score to zero

    # Method to display a question along with choices
    def display_question(self, question, choices):
        print(Fore.BLUE + question)  # Print the question in blue color
        for index, choice in enumerate(choices, start=1):  # Iterate over choices
            print(f"{index}. {choice}")  # Print choice index and text
        print(Style.RESET_ALL)  # Reset color after printing choices

    # Method to display the current score
    def display_score(self):
        print("Your score is:", self.score)  # Print current score

    # Main method to play the game
    def play(self):
        for question, (choices, answer) in self.questions.items():  # Iterate over questions
            self.display_question(question, choices)  # Display the current question
            while True:
                user_answer = input("Your answer (1, 2, 3, or 4): ")  # Get user input
                if user_answer.isdigit() and 1 <= int(user_answer) <= len(choices):  # Check if input is valid
                    if choices[int(user_answer) - 1].lower() == answer.lower():  # Check if answer is correct
                        print(Fore.GREEN + "Correct! You earn 2 points.")  # Print correct feedback in green
                        self.score += 2  # Increase score by 2
                    else:
                        print(Fore.RED + "Incorrect. You lose 1 point.")  # Print incorrect feedback in red
                        print("""
(`-').->(`-')  _   (`-')  
   <-.        .->    ( OO)_  ( OO).-/<-.(OO )  
 ,--. )  (`-')----. (_)--\_)(,------.,------,) 
 |  (`-')( OO).-.  '/    _ / |  .---'|   /`. ' 
 |  |OO )( _) | |  |\_..`--.(|  '--. |  |_.' | 
(|  '__ | \|  |)|  |.-._)   \|  .--' |  .   .' 
 |     |'  '  '-'  '\       /|  `---.|  |\  \  
 `-----'    `-----'  `-----' `------'`--' '--'""")
                        self.score = max(0, self.score - 1)  # Decrease score by 1 (minimum score is 0)
                    break  # Exit the loop after processing the answer
                else:
                    print("Invalid choice. Please enter the number corresponding to your answer.")  # Print invalid input message

            self.display_score()  # Display the current score
            if self.score >= 20:  # Check if player has reached the winning score
                print(Fore.YELLOW + "Congratulations! You win!")  # Print winning message in yellow
                break  # Exit the loop if player wins


# Main program
if __name__ == "__main__":
    print(Fore.MAGENTA + "Welcome to the General Knowledge Quiz!")  # Print welcome message in magenta
    print("In this game, you will earn 2 points for each correct answer, but you will lose 1 point for each incorrect answer.")  # Print game rules
    print("Let's begin!\n")  # Print start message

    # Define the questions as a dictionary
    questions = {
        "What is the capital of France?": (["Paris", "Rome", "Berlin", "London"], "Paris"),
        "What is the largest planet in our solar system?": (["Mars", "Venus", "Jupiter", "Saturn"], "Jupiter"),
        "Who wrote 'Romeo and Juliet'?": (["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], "William Shakespeare"),
        "What is the tallest mountain in the world?": (["Mount Everest", "K2", "Kangchenjunga", "Lhotse"], "Mount Everest"),
        "What is the main ingredient in guacamole?": (["Avocado", "Tomato", "Onion", "Garlic"], "Avocado"),
        "What is the chemical symbol for gold?": (["Ag", "Au", "Pt", "Cu"], "Au"),
        "What year did World War II end?": (["1943", "1944", "1945", "1946"], "1945"),
        "Who wrote 'To Kill a Mockingbird'?": (["Harper Lee", "J.D. Salinger", "F. Scott Fitzgerald", "Ernest Hemingway"], "Harper Lee"),
        "What is the largest ocean on Earth?": (["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "Pacific Ocean"),
        "What is the chemical symbol for water?": (["O", "H2O", "H2", "HO"], "H2O"),
        "What is the boiling point of water in Celsius?": (["0°C", "50°C", "100°C", "200°C"], "100°C"),
        "Who discovered penicillin?": (["Alexander Fleming", "Louis Pasteur", "Marie Curie", "Robert Koch"], "Alexander Fleming"),
        "What is the currency of Japan?": (["Dollar", "Euro", "Yen", "Yuan"], "Yen"),
        "Who was the first man to step on the moon?": (["Neil Armstrong", "Buzz Aldrin", "Michael Collins", "Alan Shepard"], "Neil Armstrong"),
        "Which planet is known as the Red Planet?": (["Venus", "Mars", "Jupiter", "Saturn"], "Mars"),
        "What is the tallest building in the world?": (["Shanghai Tower", "Burj Khalifa", "Abraj Al-Bait Clock Tower", "Ping An Finance Centre"], "Burj Khalifa"),
        "What is the chemical symbol for oxygen?": (["O", "O2", "O3", "H2O"], "O"),
        "What is the smallest prime number?": (["1", "2", "3", "4"], "2"),
        "Who is known as the 'Father of Computers'?": (["Alan Turing", "Charles Babbage", "Ada Lovelace", "John von Neumann"], "Charles Babbage"),
        "What is the largest organ in the human body?": (["Liver", "Brain", "Heart", "Skin"], "Skin"),
        "What is the only mammal capable of true flight?": (["Bat", "Bird", "Butterfly", "Bee"], "Bat"),
    }
        

    # Create an instance of QuizGame with the questions and play the game
    game = QuizGame(questions)
    game.play()