from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import *

# Create a question bank
question_bank = []
for item in question_data:
    new_question = Question(item["question"], item["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
# quiz.next_question()
question = quiz.next_question()


quizui = QuizUI(quiz)

# while quiz.still_has_question():
#     quiz.next_question()
