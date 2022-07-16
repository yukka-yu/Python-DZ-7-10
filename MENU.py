def get_menu():
    print('\nСписок функций'
          '\n1 - добавить сотрудника '
          '\n2 - посмотреть список сотрудников'
          '\n3 - Создать рандомных сотрудников'
          '\n4 - Найти сотрудников по имени'
          '\n5 - Удалить сотрудников'
          '\n0 - выйти из программы')

def read_user_answer(user_answer_text = 'Выберите операцию: ', minNumber = 0, maxNumber = 5):
    global user_answer
    while True:
        user_answer = isNumber(user_answer_text)
        if user_answer >= minNumber and user_answer <= maxNumber:
            break
    return user_answer


def isNumber(string = 'Enter the number: '):
    while True:
        number = input(string)
        if number.isdigit():
            return int(number)

def start():
    while True:
        #employee_list = init_data.init()
        #Это фонкция загрузки базы данных сотрудников, не понятно для чего именно тут
        get_menu()
        #user_select = user_answer.read_user_answer() - это оригинальный вызов
        user_select = read_user_answer() # Это я переделал, чтобы работало
        if user_select == 0:
            print('GoodBye! See you later!')
            break
        elif user_select == 1:
            pass
            #Вызов фукции добаления сотрудника 
            #add_employee.add_employee(employee_list)
        elif user_select == 2:
            pass
            #Вызов функции просмотра сотрудников
            #show_employee_list.show_employee_list()
        elif user_select == 3:
            pass
            #Создание рандомных сотрудников
            #generate_random_employee.generate_random_employee(employee_list)
        elif user_select == 4:
            pass
            #Поиск сотрудников по имени
            #find_employee(employee_list)
        elif user_select == 5:
            pass
            #Удаление сотрудников
            #delete_employee.delete_employee(employee_list)


start()