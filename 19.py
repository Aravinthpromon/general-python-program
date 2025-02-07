def find_max(*args):
    max_num=args[0]
    for num in args:
        if num>max_num:
            max_num=num
    return max_num  
result=find_max(10,20,30,40,50)
print(result)      