class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary

    def calculate_paycheck(self):
        return self.salary/52

class hourlyEmployee(Employee):
    def __init__(self, fname, lname, hoursWorked, hourlyRate):
        super().__init__(fname, lname)
        self.hoursWorked = hoursWorked
        self.hourlyRate = hourlyRate
    def calculate_paycheck(self):
        return self.hoursWorked*self.hourlyRate

class CommissionEmployee(SalaryEmployee):
    def __init_(self, fname, lname, salary, sales_num, commissionRate):
        super().__init__(fname, lname, salary)
        self.sales_num = sales_num
        self.commissionRate = commissionRate

    def calculate_paycheck(self):
        regular_salary = super().calculate_paycheck()
        total_com = self.sales_num*self.commissionRate
        return regular_salary + total_com
    