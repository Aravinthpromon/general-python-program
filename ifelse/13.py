sal = int(input("Enter your salary : "))
age = int(input("Enter your age : "))

if(sal>=200000 or age <=25):
    loan = int(input("Enter your required loan amount : "))
    if(loan <=50000):
        print("You are eligible for loan")
    else:
        print("maximum loan amount is 50000")
else:
    print("you are not eligible")        