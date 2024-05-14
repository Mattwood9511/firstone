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


    #Activity 2

    shopping_list =[
        "apple",
        "carrot",
        "pizza",
        "carrot",
        "dog food",
        "orange juice",
        "egg",
        "kale",
        "carrot",
        "kale",
        "orange juice",
        "kale",
        "toilet roll",
        "stamps",
        "noodles",
        "pasta sauce",
        "egg",
        "pasta sauce"
    ]
    # Create an empty dictionary to store the counts
item_counts = {}

# Iterate through each item in the shopping list
for item in shopping_list:
    if item in item_counts:
        item_counts[item] += 1
    else:
        item_counts[item] = 1

# Print the counts
print("Item counts:")
for item, count in item_counts.items():
    print(f"{item}: {count}")