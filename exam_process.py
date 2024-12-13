import string
import os
import time

variants = string.ascii_lowercase
def f_exam_process(questions):
    for index, question in enumerate(questions):
        os.system('cls')
        question.print_before
        length = len(question.answers)
        allowed_letters = [x for x in variants[:length]]
        print(f'Enter correct variant {allowed_letters}: ', end='')
        selected = input()
        while selected not in allowed_letters:
            print(f'Enter one of letters {allowed_letters}: ', end='')
            selected = input()
        questions[index].selected_answer = question.answers[allowed_letters.index(selected)]
        time.sleep(0.1)
    return questions
