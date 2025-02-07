A = int(input("enter the A value : "))
B = int(input("enter the B value : "))

Cal = str(input("Select Add or Sub or Multiply or divide : "))

if(Cal=="Add"):
    print(A+B)
elif(Cal=="Sub"):
    print(A-B) 
elif(Cal=="Multiply"):
    print(A*B)  
elif(Cal=="Divide"):
    print(A/B)  
else:
    print("invalid")          