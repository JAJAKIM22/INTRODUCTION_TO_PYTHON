class Employee():
    def __init__(self, name, last) ->None:
        self.name = name
        self.last = last

class Supervisor(Employee):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password
class Chefs(Employee):
    def leave_request(self, days):
        return ("may i take leave for " + str(days) + " days")

jaja = Supervisor("Jaja", "J", "New1")
miashi = Chefs("Jaja", "M")
Peter = Chefs("Peter", "P")

print(miashi.leave_request(3))
print(jaja.password)
print(miashi.last)

