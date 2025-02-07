data={"Name":"Aravinth","Age":23}

print(data)
print(type(data))
print(data[("Name")])
print(data["Age"])
print(data.keys())

# to print dict in list
print(data.items())

print(data["Name"])

print(data.get("Name"))

data["Location"]="Chennai"
print(data)