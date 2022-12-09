#IMPORT MODULES
import sys

locations = sys.path
# print(locations) 

for x in locations:
    print(x)


import calendar

leapdays = calendar.leapdays(2020, 2022)
print(leapdays)

leapyear = calendar.isleap(2020)
print(leapyear)