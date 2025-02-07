unit = int(input("Enter the unit : "))

bill =0
if(unit<=100):
    bill =0 
elif(unit >100 and unit<=200):
   bill= (unit - 100)*5
elif(unit>200):
    bill = (unit - 200)*10 + (100*5)
    
print("the total bill is :", bill)   