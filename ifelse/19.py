A= int(input("Enter the value of a:"))
B= int(input("Enter the value of b:"))
C= int(input("Enter the value of c:"))

if(A==B==C):
    print("all three are same")
elif(A>=B and A>=C):
    print("A is greatest num")
elif(B>=C and B>=A):
    print("B is greatest num")
elif(C>=A and C>=B):
    print("C is greatest num")    
            
    