import html
# from ui import QuizUI




class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.q_text = ""
        self.q_answer = ""

    def still_has_question(self):
        length = len(self.question_list)
        if length > self.question_number:
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        question_text = html.unescape(current_question.text)
        self.q_text = question_text
        question_answer = current_question.answer
        self.q_answer = question_answer
        self.question_number += 1



    def score_check(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            return True
        else:
            return False

