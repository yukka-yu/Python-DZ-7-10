from curses.ascii import isdigit


def read_user_answer(user_answer_text = 'Выберите операцию: ', minNumber = 0, maxNumber = 4):
    while True:
        user_answer = input(user_answer_text)
        if user_answer.isdigit():
            user_answer = int(user_answer)
            if ((user_answer >= minNumber) and (user_answer <= maxNumber)):
                return user_answer


