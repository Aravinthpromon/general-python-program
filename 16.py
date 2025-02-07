lst=[]

for i in range(1,101):
    lst.append(i)
    if i%10==0:
        print(f"Iteration{i}:{lst}")
print("final list:",lst)        