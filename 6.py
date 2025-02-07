def validate():
    s_username ="EMC"
    s_password= 123
    username= str(input("enter your username :"))
    password= int(input("Enter your password :"))
    if(username==s_username and password==s_password):
        return "CORRECT"
    else:
        return "WRONG"
a=validate()
print(a)            