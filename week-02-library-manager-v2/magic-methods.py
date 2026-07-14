class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def full_name(self):
        return f"{self.first} {self.last}"
    
    def raise_pay(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return f"Employee({self.first},{self.last},{self.pay})"
    
    def __str__(self):
        return f"{self.full_name()}, {self.email}"


emp_1 = Employee("Michał","Kowalczyk", 5000)
emp_2 = Employee("Kamil","Gałuszka", 3000)

print(emp_1)

print(repr(emp_1))

print(str(emp_1))
