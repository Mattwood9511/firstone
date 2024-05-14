# #Activity 1.

# for _ in range(13):
#     print("Hello, world!")
# #second part
# count = 0
# while count < 13:
#     print("Hello, world!")
#     count += 1

#    #Activity 2.

#    # this is how to do a Nested for loop to print multiplication tables
# for i in range(1, 13):
#     print(f"Multiplication table for {i}:")
#     for j in range(1, 13):
#         result = i * j
#         print(f"{i} × {j} = {result}")
#     print()  # Adds a line-break between tables

#    # Activity 3

#     #Initialise a list called 'numbers_list' with some integers (both even and odd)
# numbers_list = [2, 7, 14, 9, 6, 11, 20, 3, 8]

# # Initialize a counter variable for even numbers
# even_count = 0

# # Iterate through each number in the list
# for num in numbers_list:
#     if num % 2 == 0:  # Check if the current number is even
#         even_count += 1

# # Print the total number of even numbers
# print(f"Total even numbers in the list: {even_count}")

# #part 2 activity 3

# # same but a larger list 'numbers_list' with both even and odd
# numbers_list = [2, 7, 14, 9, 6, 11, 20, 3, 8, 15, 22, 25, 30, 33, 36, 40, 42, 45, 50, 55, 60]

# # Initialize a counter variable for even numbers
# even_count = 0

# # Iterate through each number in the list
# for num in numbers_list:
#     if num % 2 == 0:  # Check if the current number is even
#         even_count += 1

# # Calculate the percentage of even numbers
# total_numbers = len(numbers_list)
# even_percentage = (even_count / total_numbers) * 100

# # Print the total number of even numbers and the percentage
# print(f"Total even numbers in the list: {even_count}")
# print(f"Percentage of even numbers: {even_percentage:.2f}%")

# #Activity 4

# # Initialise the first two numbers of the Fibonacci sequence
# first_num = 0
# second_num = 1

# # Print the first two numbers of the sequence
# print(first_num, second_num, end=' ')

# # Loop to generate the next 8 Fibonacci numbers (makes a total of 10)
# for _ in range(8):
#     next_num = first_num + second_num
#     print(next_num, end=' ')
#     # Update the previous two numbers
#     first_num = second_num
#     second_num = next_num


# # Initialise the first two numbers of the Fibonacci sequence
# first_num = 0
# second_num = 1

# # Ask the user for the number of Fibonacci numbers to generate
# num_fibonacci = 15  # Predefined value for demo

# # Print the first two numbers of the sequence
# print(first_num, second_num, end=' ')

# # Loop to generate the next Fibonacci numbers
# for _ in range(num_fibonacci - 2):  # Subtract 2 to account for the first two numbers
#     next_num = first_num + second_num
#     print(next_num, end=' ')
#     # Update the previous two numbers
#     first_num = second_num
#     second_num = next_num



# first_num = int(input("First number"))
# second_num = int(input("Second number"))
 
# print(first_num, second_num, end=' ')56
 
 
# for i in range(8):
#     next_num = first_num + second_num
#     print(next_num, end=' ')
 
#     first_num = second_num
#     second_num = next_num


# #Activity 5


# size = int(input("Enter the number of rows for the pattern: "))


# for i in range(1, size + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")  
#     print()  

# ##part 2
# rows = 15
# # below is a reverse loop
# for i in range(rows, 0, -1):
#     num = i
#     for j in range(0, i):
#         print(num, end=' ')
#     print("\r")

# #Activity 6

# rows = 5

# total_sum = 0


# for i in range(rows, 0, -1):
#     num = i
#     row_sum = 0  
#     for j in range(0, i):
#         print(num, end=' ')
#         row_sum += num  
#     print("\r")
#     total_sum += row_sum  

# print(f"Total sum of digits: {total_sum}")