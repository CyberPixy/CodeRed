
class Employee:
    """A simple Employee class"""
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def full_name(self):
        return f'{self.first}, {self.last.capitalize()}'
    
    def apply_rasie(self):
        self.pay = int(self.pay * self.raise_amt)
        return self.pay



# empl_1 = Employee("Lola", "kowalska", 10000)
# empl_1.apply_rasie()
# print(empl_1.pay)
