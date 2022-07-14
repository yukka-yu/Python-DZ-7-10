import logger

def get_action():
              text = 'Choose an option: \
                            0 - view contact, 1 - add contact, 2 - delete contact, 3 - exit: '
              return int(input(text))

def call_action(action):
              if action == 0:
                            print('You choose to view contact')
              elif action == 1:
                            print('You choose to add contact.')
              elif action == 2:
                            print('You choose to delete contact.')
              else:
                            print('You choose to exit')

def get_data():
              return input('Please input necessary data: ')

def print_result(result):
              print(f'Here it is: {result}')