import unittest
from question import Question

class QuizTest(unittest.TestCase):
    question = Question()
    def test_question(self): 
        self.assertEqual(self.question.answers, [])


if __name__ == '__main__':
    unittest.main(verbosity=2)