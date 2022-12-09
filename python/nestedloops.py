import time

start_time = time.time()

#outer loop
for i in range(100):
    #inner loop
    for j in range(100):
        print(0, end="")
    print()

print(round(time.time() - start_time, 2))


num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

for i in(num_list):
    if i > 45:
     print("Over 45:", i)
    else:
        print("Under 45:", i)

num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
count = 0
for num, i in enumerate(num_list):
    count += 1
    if i == 36:
     print("Number found at position:", num)
    #  count +=1
     break
    if i > 45:
     print("Over 45:", i)
    else:
        print("Under 45:", i)
print(count)