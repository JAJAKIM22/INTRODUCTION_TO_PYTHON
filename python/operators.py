a = True
b = True

if a and b:
    print('BOTH TRUE')
if a or b:
    print('BOTH TRUE')
if not(a) and not(b):
    print("BOTH TRUE")
if not(a) or b:
    print("BOTH TRUE")


current = False

if current:
    print('Turning light off')

if not current:
    print('Turning light on')

loyalty_customer = True
total_bill = 124

if loyalty_customer and total_bill > 100:
    #give 20% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 20
elif total_bill > 100:
    #give 10% discount
    total_bill = total_bill - (float(total_bill)/ 100) * 10
else:
    #sorry no discount, 5% service charge applied.
    print('Sorry, no discount ...')

print('Total Bill: ', float(total_bill))

