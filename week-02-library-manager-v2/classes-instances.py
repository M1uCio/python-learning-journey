

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def full_name(self):
        return f"{self.first} {self.last}"

emp_1 = Employee("Michał","Kowalczyk",5000)
emp_2 = Employee("Kamil","Gałuszka",3000)

print(emp_1.email)
print(emp_2.full_name())