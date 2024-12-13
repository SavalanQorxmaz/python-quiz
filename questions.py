from question import Question
from utils import f_read_file


def f_questions():
    data = f_read_file('quiz.txt')
    questions = []
    if not data:
         return None
    else:
        for line in data:
            if line.startswith('Question'):
                questions.append(Question())
                questions[-1].question = ' '.join(line.split()[1:])
            elif line.startswith('-') or line.startswith('+'):
                if line.startswith('+'):
                    questions[-1].correct_answer = ' '.join(line.split()[1:])
                questions[-1].answers.append(' '.join(line.split()[1:]))
            else:
                questions[-1].question += f'\n{line}'
                
    return questions
        
