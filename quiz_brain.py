class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        length = len(self.question_list)
        if length > self.question_number:
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}:{current_question.text}(True/[F]alse)? ")
        self.score_check(answer, current_question.answer)

    def score_check(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            print("That's correct")
        else:
            print(f"Incorrect, Correct answer is {question_answer}")
        print(f"Your score is {self.score}/{self.question_number} ")
