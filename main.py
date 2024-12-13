from questions import f_questions
from exam_process import f_exam_process
from result import f_result

questions = f_questions()

if __name__ == '__main__':
    f_exam_process(questions)
    f_result(questions)
