import random

from game_data import data
from art import logo, vs

def clear():
    print("\n" * 100)

# Display art

# Generate random item from game_data
def generate_random_item():
    return random.choice(data)

# Format item data into a printable data
def format_data(item):
    name = item("name")
    description = item("description")
    country = item("country")
    return f"{name}, a {description}, from {country}"
 
# Ask the user for a guess

# Check if user is correct

# Make the game repeatable
## If the user get it right the item from prosition B needs to move to position A

def game():
    print(logo)

    score = 0
    game_should_continue = True
    item_A = generate_random_item()
    item_B = generate_random_item()