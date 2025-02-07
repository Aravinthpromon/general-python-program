odd_count=0
even_count=0


for i in range (1,11):
    if(i%2==0):
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("The count of odd numbers :" ,odd_count)
print("The count of even numbers :" ,even_count)        