##How TO IMPORT A SUBCLASS # import matplotlib.pyplot as plt

import math

root = math.sqrt(9)

print(root)

##EASIER WAY
from math import sqrt

root = sqrt(4)

print(root)

##USING ALIAS
import math as m

cosine = m.cos(0)
print(cosine)

##ALIAS ON FUNCTIONS
from math import factorial as f

factorial_10 = f(10)
print(factorial_10)

##MULTIPLE IMPORTS
from math import factorial, log10, sqrt

a = log10(50)
print(a)

##OTHER WAY
from math import *

a = log10(50)
print(a)

##IMPORTING VARIABLE
# from math import some_variable

# a = log10(50)
# print(a)

