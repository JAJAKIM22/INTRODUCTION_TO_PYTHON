#SCOPE FOR AN ATTRIBUTE LEGB// LOCAL, ENCLOSED, GLOBAL AND BUILT-IN

def d():
    animal = "elephant"
    def e():
        nonlocal animal
        animal = "giraffe"
        print("Inside nested function: " +animal)
    print("Before calling function: " +animal)
    e()
    print("After calling nested function: " +animal)

animal = "camel" #GLOBAL VARIABLE
d()
print("Global animal: " +animal)