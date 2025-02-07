cost = int(input("Enter the cost of your bike :"))

tax =0

if(cost>100000):
    tax= (15/100*cost)
elif(cost>50000 and cost <=100000 ):
    tax= (10/100*cost)
elif(cost<=50000):
    tax= (5/100*cost); 
    
print("The total road tax is :", tax)        