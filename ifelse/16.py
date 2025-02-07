# Get the month number from the user
month = int(input("Enter a month number (1-12): "))

# Dictionary with month names and number of days
months = {
    1: ("January", 31),
    2: ("February", 28),  # Assuming a non-leap year
    3: ("March", 31),
    4: ("April", 30),
    5: ("May", 31),
    6: ("June", 30),
    7: ("July", 31),
    8: ("August", 31),
    9: ("September", 30),
    10: ("October", 31),
    11: ("November", 30),
    12: ("December", 31)
}

# Check if the month number is valid
if 1 <= month <= 12:
    name, days = months[month]
    print(f"The month is {name} and it has {days} days.")
else:
    print("Invalid month number. Please enter a number from 1 to 12.")
