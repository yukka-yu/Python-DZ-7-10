import csv

def add_employee(emp):
    with open("/home/sasha/Documents/Developing/Python/Python Dz/Python-DZ-7-10/DZ8_DataBase_Project/Emp.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        #writer.writerows(emp)
        writer.writerow(emp.split(" "))
# add_employee(['Prilepin', 'Zahar', 'writer', '30000'])
# add_employee()
# add_employee([['Surname', 'Name', 'Dept', 'Salary'], ['Prilepin', 'Zahar', 'writer', '30000'], ['Ivanov', 'Petr', 'programmer', '60000' ], ['Petrov', 'Ivan', 'programmer', '60000'], ['Garanichev', 'Alexander', 'sportsman', '70000']])


