import csv
from collections import namedtuple

Employee = namedtuple('Employee', ('name', 'age', 'title', 'department'))

if __name__ == '__main__':
    with open('employees.csv') as f:
        rows = csv.reader(f)
        for emp in map(Employee._make, rows):
            print(emp)
            print(emp.name, emp.age)
