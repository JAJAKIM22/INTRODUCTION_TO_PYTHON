
for i in range(10):
    print("Peter")

favorites = ["Ice-cream" , "pizza " , "lemon, cake"]
for item in favorites:
    print("i love", item)




count = 0
while count < len(favorites):
    print("I like:", favorites[count])
    count += 1

for name, item in enumerate(favorites):
    print(name, item)

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert) 
else:
    print('No sorry, that dessert is not on my list')

## BREAK TO STOP LOOP
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        print('Yes one of my favorite desserts is', dessert)
        break 
else:
    print('No sorry, not a dessert on my list')

## CONTINUE TO SKIP ITEM
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert) 

## PASS IGNORES IF STATEMENT
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert) 
