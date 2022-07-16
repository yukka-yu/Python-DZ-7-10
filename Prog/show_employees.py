import csv

def show_employees():
    with open("/home/sasha/Documents/Developing/Python/Python Dz/Python-DZ-7-10/DZ8_DataBase_Project/Emp.csv", 'rt') as csvfile:
        for row in csv.reader(csvfile):
            print(row)
# show_employees()