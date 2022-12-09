from abc import ABC, abstractmethod

#ABSTRACT CLASS
class Employee(ABC):
    @abstractmethod
    def donate(self):
        pass

#SUB CLASS
class Donation(Employee):
    def donate(self):
        a = input("How much would you like to donate: ")
        return a

amounts = []
jaja = Donation()
peter = Donation()

j = jaja.donate()
p = peter.donate()
amounts.append(j)
amounts.append(p)
print(amounts)

    
   