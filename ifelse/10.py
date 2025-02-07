Score = int(input("Enter your mark : "))

if(Score<35):
    print("Poor student")
elif(Score>=35 and Score<70):
    print("Average student")
elif(Score>=70 and Score <=100):
    print("He is a bright student")    
else:
    print("Enter valid mark")
