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


emp_str_1 = "Michał-Kowalczyk-5000"
emp_str_2 = "Kamil-Gałuszka-3000"

emp_1 = Developer.from_string(emp_str_1)
emp_2 = Developer.from_string(emp_str_2)

print(emp_1.__dict__)
