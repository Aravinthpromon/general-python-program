num = int(input("Enter a number: "))

if num > 1:  # Check if the number is greater than 1
    for i in range(2, int(num ** 0.5) + 1):  # Loop from 2 to the square root of num
        if num % i == 0:  # If num is divisible by i
            print(num, "is not a prime number")
            break  # Exit the loop if a divisor is found
    else:
        print(num, "is a prime number")  # If no divisors were found
else:
    print(num, "is not a prime number")  # Numbers less than or equal to 1 are not prime
