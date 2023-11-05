# Define arrays to store item information
item_codes = ['A1', 'A2', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1', 'D2', 'E1', 'E2', 'E3', 'F1', 'F2', 'G1', 'G2']
descriptions = ['Compact', 'Tower', '8 GB', '16 GB', '32 GB', '1 TB HDD', '2 TB HDD', '4 TB HDD', '240 GB SSD', '480 GB SSD',
                '1 TB HDD', '2 TB HDD', '4 TB HDD', 'DVD/Blu-Ray Player', 'DVD/Blu-Ray Re-writer', 'Standard Version', 'Professional Version']
prices = [75.00, 150.00, 79.99, 149.99, 299.99, 49.99, 89.99, 129.99, 59.99, 119.99, 49.99, 89.99, 129.99, 50.00, 100.00, 100.00, 175.00]

# Initialize variables for chosen components
chosen_case = None
chosen_ram = None
chosen_hdd = None

# Initialize variables for additional items
additional_items = []

# Function to display items and prices
def display_items():
    print("Item Code\tDescription\tPrice ($)")
    for i in range(len(item_codes)):
        print(f"{item_codes[i]}\t{descriptions[i]}\t{prices[i]}")

# Task 1 - Select main items
print("Task 1 - Setting up the system and ordering the main items")
display_items()

while chosen_case not in item_codes or chosen_case[0] != 'A':
    chosen_case = input("Choose a case (Enter item code 'A1' or 'A2'): ").strip().upper()

while chosen_ram not in item_codes or chosen_ram[0] != 'B':
    chosen_ram = input("Choose RAM (Enter item code 'B1', 'B2', or 'B3'): ").strip().upper()

while chosen_hdd not in item_codes or chosen_hdd[0] != 'C':
    chosen_hdd = input("Choose Main Hard Disk Drive (Enter item code 'C1', 'C2', or 'C3'): ").strip().upper()

# Calculate the price of the computer
computer_price = 200.00 + prices[item_codes.index(chosen_case)] + prices[item_codes.index(chosen_ram)] + prices[item_codes.index(chosen_hdd)]

# Display the chosen items and computer price
print("\nChosen Components:")
print(f"Case: {descriptions[item_codes.index(chosen_case)]} - ${prices[item_codes.index(chosen_case)]}")
print(f"RAM: {descriptions[item_codes.index(chosen_ram)]} - ${prices[item_codes.index(chosen_ram)]}")
print(f"Main Hard Disk Drive: {descriptions[item_codes.index(chosen_hdd)]} - ${prices[item_codes.index(chosen_hdd)]}")
print(f"Computer Price: ${computer_price:.2f}")

# Task 2 - Select additional items
print("\nTask 2 - Ordering additional items")
display_items()

while True:
    additional_item = input("Choose an additional item (Enter item code or 'done' to finish): ").strip().upper()
    if additional_item == 'DONE':
        break
    elif additional_item in item_codes:
        additional_items.append(additional_item)

# Calculate the updated price of the computer with additional items
additional_items_price = sum([prices[item_codes.index(item)] for item in additional_items])
computer_price += additional_items_price

# Display the additional items and the new computer price
if additional_items:
    print("\nAdditional Items:")
    for item in additional_items:
        print(f"{descriptions[item_codes.index(item)]} - ${prices[item_codes.index(item)]}")
    print(f"New Computer Price (with additional items): ${computer_price:.2f}")
else:
    print("No additional items selected.")

# Task 3 - Apply discounts
print("\nTask 3 - Offering discounts")

# Calculate the discount
if len(additional_items) == 1:
    discount = 0.05
elif len(additional_items) >= 2:
    discount = 0.10
else:
    discount = 0

discount_amount = discount * computer_price
discounted_price = computer_price - discount_amount

# Display the discount and the final price
if discount > 0:
    print(f"Discount Applied: {discount * 100}%")
    print(f"Amount Saved: ${discount_amount:.2f}")
    print(f"Final Computer Price (after discount): ${discounted_price:.2f}")
else:
    print("No discount applied.")

