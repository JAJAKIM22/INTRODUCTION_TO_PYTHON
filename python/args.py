def sum_of(a,b):
    return(a +b)

print(sum_of(4, 5)) 
# print(sum_of(4,5, 6)) # IF I ADD ANOTHER NUMER (4,5, 7) GIVE AN ERROR

def sum_off(*args):
    sum = 0
    for x in args:
        sum += x
    return sum
print(sum_off(4, 5, 6, 7)) 