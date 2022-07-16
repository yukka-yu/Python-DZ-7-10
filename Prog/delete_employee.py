import csv
import os

def delete_employee(emp_name):
    with open("/home/sasha/Documents/Developing/Python/Python Dz/Python-DZ-7-10/DZ8_DataBase_Project/Emp.csv", 'rt') as csvfile:
        with open("/home/sasha/Documents/Developing/Python/Python Dz/Python-DZ-7-10/DZ8_DataBase_Project/Emp.csv.bkp", 'wt') as csvfile_bkp:
            writer = csv.writer(csvfile_bkp)
            for row in csv.reader(csvfile):
                if row[0] != emp_name:
                    writer.writerow(row)
    os.rename("/home/sasha/Documents/Developing/Python/Python Dz/Python-DZ-7-10/DZ8_DataBase_Project/Emp.csv.bkp", "/home/sasha/Documents/Developing/Python/Python Dz/Python-DZ-7-10/DZ8_DataBase_Project/Emp.csv")
# delete_employee('Ivanov')