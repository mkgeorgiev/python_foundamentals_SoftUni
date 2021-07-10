to_do_list = [0] * 10
note = input()
while not note == "End":
    importance, to_do_note = note.split("-")
    importance =int(importance) - 1
    to_do_list[importance] = to_do_note
    note = input()

print([el for el in to_do_list if not el == 0])