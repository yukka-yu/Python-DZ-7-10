import view
import logger


def do_action(action):

              if action == 0: # (view contact)
                            view.call_action(0)
                            word_to_find = view.get_data()
                            finded_line = []
                            for line in logger.get_text_from_file():
                                          if word_to_find in line:
                                                        finded_line.append(line)
                            # finded_line = (line for line in logger.get_text_from_file() if word_to_find in line)
                            # (поиск в тексте из файла строки, в которой есть искомое слово)
                            view.print_result(finded_line)

              elif action == 1: # (add contact)
                            view.call_action(1)
                            logger.contact_add(view.get_data())

              elif action == 2: # (delete contact)
                            view.call_action(2)
                            logger.contact_del(view.get_data())

              else: 
                            view.call_action(3)


