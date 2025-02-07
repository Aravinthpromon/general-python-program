sal = int(input("Enter your salary :"))
exp = int(input("Enter your experience :"))

if(exp>10):
    bon=10/100*sal
elif(exp>=6 and exp<=10):
    bon=8/100*sal
elif(exp<6):
    bon=5/100*sal  
    
print("Your bonus is:",bon) 
          

