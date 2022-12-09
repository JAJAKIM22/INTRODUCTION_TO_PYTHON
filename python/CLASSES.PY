#INSTANTIATION
class MyClass:
    # pass
    print("Hello")
myclass = MyClass()

## ATTRIBUTE REFERENCING
class MyClass:
    a = 6
    print("Hello")

    def hello(self):
        print("Hey i'm Peter")
myclass = MyClass()
print(MyClass.a)
print(myclass.a)
# print(MyClass.hello())
print(myclass.hello())

# Define class MyFirstClass
class  MyFirstClass():
    print("Who wrote this?")
    # Define string variable called index
    index = "Author-Book"
    # Define function hand_list()
    def hand_list(self, philosopher, book):
        # variable + “ wrote the book: ” + variable
        # print(MyFirstClass.index)
        print(philosopher+ " wrote the book: " + book) 

# Call function handlist()
whodunnit = MyFirstClass()
print(whodunnit.hand_list("Sun Tzu", "The Art"))



class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2

    def cost_evaluation(self, rate):
        # Functionality to calculate the costs from the area of the house
        cost = rate * self.num_rooms
        return cost



house = House()
print(house.num_rooms)
print(House.num_rooms)
house.num_rooms = 7
# House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)