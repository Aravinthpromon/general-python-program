km = int(input("Enter your travel distance :"))

if(km<=10):
    amt = km*11
elif(km>10 and km<=100):
    amt = 110+ (km - 10)*10
elif(km>100):
    amt= 110+900 (km - 100)*9
    
print("your travel amount :", amt)            