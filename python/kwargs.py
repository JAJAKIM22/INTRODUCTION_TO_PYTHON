def sum_off(**order):
    sum = 0
    for key, value in order.items():
        sum += value
    return round(sum, 2)
print(sum_off(coffee=12.36, tea = 20.24, cocoa = 15.76))

