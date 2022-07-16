import csv

def find_employee(emp_name):
    with open("/home/sasha/Documents/Developing/Python/Python Dz/Python-DZ-7-10/DZ8_DataBase_Project/Emp.csv", 'rt') as csvfile:
        flag = 0
        for row in csv.reader(csvfile):
                if row[0] == emp_name:
                    flag += 1
                    print(row)
        if flag == 0: print("Такой сотрудник не найден!")
# find_employee('Kazakov')