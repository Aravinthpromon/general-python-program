a = []

for i in range(1, 5):
    num = int(input(f"Enter the value {i}: "))  # Using f-string to display the value of i
    a.append(num)

print(a)

sum = 0
for i in a:
    sum = sum + i
print("your sum is" , sum)
