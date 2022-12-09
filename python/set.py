set_a = {1,2,3,4,5}
set_b = {5,6,7,8,9}
# set_a.add(6)
# set_a.remove(6)
# set_a.discard(5)
print(set_a)
print(set_a.union(set_b))
print(set_a | set_b)

print(set_a.intersection(set_b))
print(set_a & set_b)

print(set_a.difference(set_b))
print(set_a - set_b)

print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)