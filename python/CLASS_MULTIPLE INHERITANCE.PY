# #SIMPLE INHERITANCE
# class A:
#     pass

# class B(A):
#     pass
# b = B()
# print(issubclass(A,B))
# print(issubclass(B,A))

# print(isinstance(b,B))


# # MULTIPLE INHERITANCE
# class A:
#    a = 1
   
# class B:
#    b = 2
   
# class C(A, B):
#    pass

# c = C()
# print(c.a, c.b)


# #MULTILINE INHERITANCE
# class A:
#    a = 1

# class B(A):
#    a = 2

# class C(B):
#    pass

# c = C()
# print(c.a)
# print(C.mro())
# # print(help(c))
# ##USE OF SUPER() FUNCTION
# class Fruit():
#     def __init__(self, fruit):
#         print('Fruit type: ', fruit)


# class FruitFlavour(Fruit):
#     def __init__(self):
#         super().__init__('Apple')
#         print('Apple is sweet')

# apple = FruitFlavour()


class A:
    def b(self):
        return "Function inside A"

class B:
    def b(self):
        return "Function inside B"

class C(A, B):
    def b(self):
        return "Function inside C"
    pass

class D(C):
    pass

d = D()
print(d.b())
