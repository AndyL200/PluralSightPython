from employee import Employee

class Company:


    def __init__(self):
        self.employees = []


    def addEmployee(self, new_worker):
        self.employees.append(new_worker)


    def displayEmployees(self):
        print('Current Employees: ')
        for i in self.employees:
            print(i.fname, i.lname, i.salary)

    def payEmployees(self):
        print('Paying Employees:')
        for i in self.employees:
            print('Paycheck for:', i.fname, i.lname)
            print(f'Amount: ${i.calculate_paycheck():,.2f}')


def main():

    my_company = Company()

    employee1 = Employee("Rob", "Chill", 50000)
    my_company.addEmployee(employee1)
    employee2 = Employee("Grob", "Bill", 500000)
    my_company.addEmployee(employee2)
    employee3 = Employee("Gru", "Minon", 20)
    my_company.addEmployee(employee3)

    my_company.displayEmployees()
    my_company.payEmployees()

main()