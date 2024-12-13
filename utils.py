
def f_make_data():
    questions = []
    try:
        with open('quiz.txt', mode='r') as quiz:
            while True:
                line = quiz.readline()
                if not line:
                    break
                if line == '\n':
                    continue
                # print(line.split()[0])
                if line.split()[0].endswith('.'):
                    position = line.index('.')
                    questions.append({'question': line[position+1:-1]})
                elif line.split()[0].endswith(')'):
                    answer_key = f'{line.split()[0][:-1].strip()}'
                    answer_value = line[position+1:-1]
                    if answer_value.endswith('[+]'):
                        answer_value = answer_value[:-3].strip()
                        questions[-1].update({'correct': answer_key})
                    position = line.index(')')
                    questions[-1].update({answer_key: answer_value})
                else:
                    questions[-1]['question'] += line
                    
        return questions
    except FileNotFoundError:
            print('File not found')
            return None

        
    