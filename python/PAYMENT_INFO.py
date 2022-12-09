class payslip():
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def paid(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
           print(self.payment + " " + self.name + " has been paid " + str(self.amount))
        else:
            print(self.name + " has not been paid ")

peter = payslip("Peter", "no", 3000)
james = payslip("James", "no", 6000) 
print(peter.status()) 
print(james.status()) 

print("AFTER PAYMENT:")
peter.paid()
print(peter.status()) 
print(james.status()) 
    
    

     
