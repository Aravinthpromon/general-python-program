def create_profile(**kwargs):
    if not kwargs:
        return "No data provided"
    
    result="profile:\n"
    for key, value in kwargs.items():
        result+=f"{key}:{value}\n"
    return result.strip()

lst=create_profile(name="aravinth", age =23,) 

print(lst)