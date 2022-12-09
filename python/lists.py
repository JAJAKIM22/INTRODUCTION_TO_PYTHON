list1 = [1, 2, 3, 4, 5]
print(*list1)
print(list1, sep=" ")

##ADDING ITEMS TO LIST
list1.insert(len(list1), 6)
print(list1, sep=" ")

list1.append(6)
print(list1, sep=" ")

list1.extend([7,8,9])
print(list1, sep=" ")

##REMOVING ITEMS FROM A LIST
list1.pop(7)
print(list1, sep=" ")

del list1[6]
print(list1, sep=" ")


##ITERATE OVER LIST
for i in list1:
    print("Value is:", i)
