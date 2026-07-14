import datetime

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

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split("-")
        return cls(first, last, int(pay))

class  Developer(Employee):
    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for i, emp in enumerate(self.employees):
            print(f"{i+1}. {emp.full_name()}")


dev_1 = Developer("Michał","Kowalczyk",5000,"Python")
dev_2 = Developer("Kamil","Gałuszka",3000,"C++")

mng_1 = Manager("Maciej","Michalczyk",7000,[dev_1])

print(mng_1.email)

mng_1.print_emps()

mng_1.add_emp(dev_2)

mng_1.print_emps()

mng_1.remove_emp(dev_1)

mng_1.print_emps()