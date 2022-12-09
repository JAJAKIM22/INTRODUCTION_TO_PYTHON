my_dict = {1: "Peter", "name": "JAJA"}

# my_dict[1] = "Miashi"

# my_dict['name'] = "Miashi"

# del my_dict[1]

print(my_dict['name'])
# print(my_dict[1])
print(my_dict)

for x in my_dict:
    print(x)

for key, value in my_dict.items():
    print(str(key) + ":" + value)
