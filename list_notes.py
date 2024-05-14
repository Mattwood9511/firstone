# print ("these are my notes on lists")

# coffee_order = [
#     "alex - cortado",
#     "ben - latte",
#     "charlie - mocha"
# ]

# print(coffee_order)

# things_i_can_see =[
#     "energy drink",
#     "snake tank",
#     "television"
# ]

# print(things_i_can_see)


# coffee_order = [
#     "alex - cortado",
#     "ben - latte",
#     "charlie - mocha"
# ]

# print(coffee_order[2])

# coffee_order = [
#     "alex - cortado",
#     "ben - latte",
#     "charlie - mocha"
# ]

# print(coffee_order)

# coffee_order[2] = "charlie - hot chocolate"

# print(coffee_order)

# coffee_order = [
#     "alex - cortado",
#     "ben - latte",
#     "charlie - mocha",
# ]

# print(len(coffee_order))

# coffee_order = [
#     "alex - cortado",
#     "ben - latte",
#     "charlie - mocha",
#     "brian-mocha",
#     "toby-mocha"
# ]

# print(coffee_order)

# coffee_order.append("diane-tea")

# print(coffee_order)

# coffee_order = [
#     "alex - cortado",
#     "ben - latte",
#     "charlie - mocha"
# ]

# # Print the coffee orders
# print(coffee_order)

# # Count the number of orders
# num_orders = len(coffee_order)
# print(f"Total number of coffee orders: {num_orders}")

# coffee_order = [
#     "alex - cortado",
#     "ben - latte",
#     "charlie - mocha",
#     "brian - mocha",
#     "toby - mocha",
#     "sam - latte"
# ]

# # Create an empty dictionary to store the counts
# order_counts = {}

# # Iterate through each order
# for order in coffee_order:
#     name, coffee_type = order.split(" - ")
#     if coffee_type in order_counts:
#         order_counts[coffee_type] += 1
#     else:
#         order_counts[coffee_type] = 1

# # Print the coffee orders
# print("Coffee orders:")
# for order in coffee_order:
#     print(order)

# # Print the counts
# print("\nNumber of each coffee type ordered:")
# for coffee_type, count in order_counts.items():
#     print(f"{coffee_type}: {count}")


# Create a list of 3 favorite websites
favorite_websites = ["Google",
                      "reddit", 
                      "instagram"]

# Add two more websites using the `append()` method
favorite_websites.append("spotify")
favorite_websites.append("YouTube")

# Print the updated list
print("Favorite websites:")
for website in favorite_websites:
    print(f"- {website}")