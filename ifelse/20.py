# Function to find the youngest boy
def find_youngest_boy(ages):
    # Find the minimum age in the list
    youngest_age = min(ages)
    return youngest_age

# Input ages of the boys
ages = []
for i in range(1, 5):
    age = int(input(f"Enter the age of boy {i}: "))
    ages.append(age)

# Find and print the youngest boy's age
youngest = find_youngest_boy(ages)
print(f"The youngest boy is {youngest} years old.")
