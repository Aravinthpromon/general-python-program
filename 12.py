def func(*args):
    return args[0]+args[1]+args[2]

a= int(input("Enter the value of a:"))
b= int(input("Enter the value of b:"))
c= int(input("Enter the value of c:"))

add=func(a,b,c)   

print(add)