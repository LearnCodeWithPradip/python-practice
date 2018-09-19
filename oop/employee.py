class Employee:
    raise_apply = 1.04
    no_of_employee = 0
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.email = fname + '.' +lname +'@gmail.com'

        Employee.no_of_employee += 1

    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)

    def increment(self):
        self.salary = int(self.salary * self.raise_apply)

emp = Employee('pradip','kolage',10000)
print(Employee.no_of_employee)
print(emp.fullname())
print(emp.email)
print(emp.salary)
emp.increment()
print(emp.salary)

