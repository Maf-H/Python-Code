#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

class Employee:
    """ Employee class with attributes of first name and last name """
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name
    
    def __str__(self):
        #return "%s %s" % ( self.first_name, self.last_name )
        return f"Employee name : {self.first_name} {self.last_name}"
    
class Hourly_Worker(Employee):
    def __init__(self, f_name, l_name, hours, wage):
        Employee.__init__(self, f_name, l_name)
        self.hours = hours
        self.wage = wage
            
    def get_pay(self):
        if (self.hours <= 40):
            pay = self.hours * self.wage
        else:
            pay = (40*self.wage + (self.hours-40)*self.wage*1.5)
        return pay
    
    def __str__(self):
        return f"{Employee.__str__(self)} payed : {self.get_pay()} ETB"
    
employee = Employee("Mesfin", "Haftu")
hourly_worker = Hourly_Worker("Mesfin", "Haftu", 50, 150)
print(hourly_worker)
print(hourly_worker.__str__())
print(Employee.__str__(hourly_worker)) # Dynamic (run-time) polymorphism, late binding

    
