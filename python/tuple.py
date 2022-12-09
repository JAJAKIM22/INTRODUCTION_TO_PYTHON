## IMMUTABLE CANNOT BE CHANGED

my_tuple = (1, "new", 4.5, 9)

print(type(my_tuple[1]))

print(my_tuple.count('new'))

print(my_tuple.index(4.5))

for x in my_tuple:
    print(x)