A = int(input("enter your A mark : "))
B = int(input("enter your B mark : "))
C = int(input("enter your C mark : "))
D = int(input("enter your D mark : "))
E = int(input("enter your E mark : "))

Total = A+B+C+D+E  #Total = (A+B+C+D+E)/5 # 
if(Total/5<35):
    print("you need a tuition")
else:
    print("You good to go")    