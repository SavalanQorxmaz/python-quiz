import string

variants = string.ascii_lowercase

colors = dict(
    RED     = '\x1b[1;39;41m',
    GREEN   = '\x1b[1;37;42m',
    RESET   = '\x1b[1;39;49m',
)

class Question:
    def __init__(self):
        self.question = None
        self.answers = []
        self.correct_answer = None
        self.__selected_answer = None

    @property
    def selected_answer(self):
        return self.__selected_answer
    
    @selected_answer.setter
    def selected_answer(self, answer):
        self.__selected_answer = answer

    @property
    def result(self):
        if self.selected_answer is not None and self.selected_answer == self.correct_answer:
            return True
        return False
    
    @property
    def print_before(self):
        result = self.question
        for i, answer in enumerate(self.answers):
            temp = f'\n{variants[i]}) {answer}'
            result +=temp
        print(result)

    @property
    def print_after(self):
        
        question = self.question
        result = self.result
        for i, answer in enumerate(self.answers):

            # temp = f'\n{variants[i]}) {answer}'
            # if answer == self.correct_answer:
            #     temp = f'\n{colors["GREEN"]}{variants[i]}) {answer}{colors["RESET"]}'
            # elif not result and answer == self.selected_answer:
            #     temp = f'\n{colors["RED"]}{variants[i]}) {answer}{colors["RESET"]}'

            temp = f'\n{colors["GREEN"]}{variants[i]}) {answer}{colors["RESET"]}' if answer == self.correct_answer else (
                f'\n{colors["RED"]}{variants[i]}) {answer}{colors["RESET"]}' if not result and answer == self.selected_answer else f'\n{variants[i]}) {answer}'
            )
            question +=temp
        print(question)

    def __str__(self):
        return self.question
    def __repr__(self):
        return f'{self.question}'