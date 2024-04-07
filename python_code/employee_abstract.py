#  Copyright (c) 2024-02/04/2024, 21:47.
#  Mesfin Haftu
#  All rights are reserved

class Employee:
    """ Employee class with attributes of first name and last name """
    def __init__(self, f_name, l_name):
        if (self.__class__ == Employee):
            raise NotImplementedError("Can't creat object fromm abstract class 'Employee'.")

        self.first_name = f_name
        self.last_name = l_name
    
    def earnings(self):
        raise NotImplementedError("Can't call abstract class method, please override it.  ")
    
    def _check_positive(self, value):
        if (value >= 0):
            return value    
        else:
            raise (valueError, "Please enter positive value: %f" %value)
    def __str__(self):
        #return "%s %s" % ( self.first_name, self.last_name )
        return f"{self.first_name} {self.last_name}"

class Boss(Employee):
    """ Employee class with attributes of first name last name and weekly fixed salary """
    def __init__(self, f_name, l_name, w_salary):
        Employee.__init__(self, f_name, l_name)
        self.weekly_salary = self._check_positive(w_salary)
    
    def earnings(self):
        return self.weekly_salary
    
    def __str__(self):
        return f"%23s {Employee.__str__(self)}" %("Boss: ")
           
class Commusion_Worker(Employee):
    def __init__(self, f_name, l_name, w_salary, commusion, pieces):
        Employee.__init__(self, f_name, l_name)
        self.weekly_salary = self._check_positive(w_salary)
        self.quantity = self._check_positive(pieces)
        self.commusion = self._check_positive(commusion)

    def earnings(self):
        return (self.weekly_salary + self.quantity * self.commusion)
    
    def __str__(self):
        return f"%23s {Employee.__str__(self)}" %("Commusion Worker: ")
      
class Piece_Worker(Employee):
    def __init__(self, f_name, l_name, pp_piece, quantity):
        Employee.__init__(self, f_name, l_name)
        self.price_per_piece = self._check_positive(pp_piece)
        self.quantity = self._check_positive(quantity)
    
    def earnings(self):
        return self.price_per_piece * self.quantity
    
    def __str__(self):
        return f"%23s {Employee.__str__(self)}" %("Piece Worker: ")
           
class Hourly_Worker(Employee):
    def __init__(self, f_name, l_name, hours, wage):
        Employee.__init__(self, f_name, l_name)
        self.hours = self._check_positive(hours)
        self.wage = self._check_positive(wage)
            
    def earnings(self):
        if (self.hours <= 40):
            pay = self.hours * self.wage
        else:
            pay = (40*self.wage + (self.hours-40)*self.wage*1.5)
        return pay
    
    def __str__(self):
        return f"%18s {Employee.__str__(self)}" %("Hourly Worker: ")

def main():
    employees = [
    Boss("Mesfin", "Haftu", 50000),
    Commusion_Worker("Marta", "Tsegaye", 10_000, 10, 100),
    Piece_Worker("Tsiyon", "Nigusie", 100, 100),
    Hourly_Worker("Lidya", "Worku", 150, 45)]
    for employee in employees:
        print ("%35s earns: %.2f" %(employee, employee.earnings()))
    
if __name__ == "__main__":
    main()
print()