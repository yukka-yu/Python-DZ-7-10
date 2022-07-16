from View.view_menu import view_menu 
from In.user_answer import read_user_answer
from In.init_data import employee, employee_surname
from Prog.add_employee import add_employee
from Prog.show_employees import show_employees
from Prog.find_employee import find_employee
from Prog.delete_employee import delete_employee

def start():
    while True:
        view_menu()
        #user_select = user_answer.read_user_answer() - это оригинальный вызов
        user_select = read_user_answer() # Это я переделал, чтобы работало
        if user_select == 0:
            print('GoodBye! See you later!')
            return
        elif user_select == 1:
            #Вызов фукции добаления сотрудника 
            emp = employee()
            add_employee(emp)
        elif user_select == 2:
            #Вызов функции просмотра сотрудников
            show_employees()
        elif user_select == 3:
            #Поиск сотрудников по фамилии
            emp = employee_surname()
            find_employee(emp)
            
        elif user_select == 4:
            #Удаление сотрудников
            show_employees()
            emp = employee_surname()
            delete_employee(emp)      
            

        
            