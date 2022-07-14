# data -  данные контакта, которые вводит пользователь после выбора пункта меню

def get_text_from_file():
              text = []
              with open('phonebook.txt', 'r') as f:
                            text = ''.join(line for line in f.readlines())
                            return text.split('\n')

def get_text_to_file(text):
              with open('phonebook.txt', 'w') as f:
                            f.write(text)


def contact_add(data):
              with open('phonebook.txt', 'a') as f:
                            f.write(f'\n{data}')


def contact_del(data):
              my_lines = []
              with open('phonebook.txt', 'r') as f:
                            for line in f.readlines():
                                          if not data in line:
                                                        my_lines.append(line)
              with open('phonebook.txt', 'w') as f:
                            for line in my_lines:
                                          f.write(line)

#contact_add('*Ivanov, Aleksey, 8(967) 132-54-80, police*')
#data = get_text_from_file()
#get_text_to_file(data)


