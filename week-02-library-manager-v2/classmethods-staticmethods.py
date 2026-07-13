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
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

emp_str_1 = "Michał-Kowalczyk-5000"
emp_str_2 = "Kamil-Gałuszka-3000"

emp_1 = Employee.from_string(emp_str_1)

my_date = datetime.date(2026, 7, 13)

print(Employee.is_workday(my_date))