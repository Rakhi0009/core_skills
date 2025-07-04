class Employee:
    """ Class representation of an employee"""
    company_name = "EPAM"
    
    def __init__(self, Id, name, department, salary):
        self.id = Id
        self.name = name
        self.department = department
        self.salary = salary

    def get_salary(self):
        return self.salary
    
    def get_department(self):
        return self.department
    
    def get_name(self):
        return self.name
    
    def increment_salary(self, increment):
        self.salary += increment
    

anuj = Employee(1, "Anuj Kumar", "Backend", 50000)
deepak = Employee(2, "Deepak Kumar", "Full Stack", 100000)

print(anuj.salary,deepak.salary)
print(anuj.get_department(), deepak.get_department())
anuj.increment_salary(20000)
print(anuj.get_salary())

print(anuj.company_name)
deepak.company_name = "AMAZON"
deepak.allow = True
print(deepak.company_name)
print(anuj.company_name)
print(anuj.__dict__)
print(deepak.__dict__)