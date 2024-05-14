# print ("these are my notes on functions")

# def say_hello():
#     print("hello!")

# say_hello()

# def say_goodbye():
#     print("goodbye")

# say_goodbye()

# def say_something(phrase):
#     print(f"{phrase}!")

# say_something("how do you do")

# say_something("isnt the weather lovely")

# def cash_withdrawal(amount, accnum):
#     print(f"you are withdrawing {amount} from {accnum}")

# cash_withdrawal(£250, 12345678)
# cash_withdrawal(10, 876654321)
# cash_withdrawal(input("how much do you want to withdraw"),12345678)




# # Simple Cash Withdrawal Simulation

# # Initial account balance
# account_balance = 1000

# def withdraw_cash(amount):
#     global account_balance
#     if amount > 0 and amount <= account_balance:
#         account_balance -= amount
#         print(f"Withdrew ${amount}. New balance: ${account_balance}")
#     else:
#         print("Invalid withdrawal amount or insufficient funds.")

# # Example usage
# withdraw_cash(200)  # Withdraw $200
# withdraw_cash(800)  # Withdraw $800 (insufficient funds)
# withdraw_cash(100)  # Withdraw $100

# # Note: In a real-world application, you'd have additional features like PIN validation, error handling, etc.

# def drinks_order(size, drink_type):
#     print(f"You ordered a {size} {drink_type}. Enjoy!")


# drinks_order("medium", "sprite")
# drinks_order("large", "coke")

# def take_order(topping):
#     print("pizza with {}".format(topping))

# take_order("cheese")

# def take_order(size, type_of_pizza, topping1, topping2):
#     print(f"You ordered a {size} {type_of_pizza} pizza with {topping1} and {topping2}. Enjoy!")

# # Example usage
# take_order("large", "vegetarian", "mushrooms", "olives")
# take_order("medium", "pepperoni", "extra cheese", "bell peppers")