from tkinter import *
from quiz_brain import *

THEME_COLOUR = "#375362"


class QuizUI:

    def __init__(self,quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOUR, padx=20, pady=20)


        def feeback(result):

            if result:
                self.display.config(bg="green")
                self.window.after(1000, func=color_reset)
            else:
                self.display.config(bg="red")
                self.window.after(1000, func=color_reset)

        def color_reset():
            self.display.config(bg="white")

        def next_question():
            self.quiz.next_question()


        def ans_true():

            user_answer = "True"
            self.response = user_answer
            correct = self.quiz.score_check(user_answer=user_answer,question_answer=self.quiz.q_answer)
            feeback(correct)
            self.scoreboard.config(text=f"Score:{self.quiz.score} ", font=("Arial", 10, "normal"))

            if self.quiz.still_has_question():
                next_question()
                self.display.itemconfig(self.question_text, text=f"{self.quiz.q_text}")
            else:
                self.display.itemconfig(self.question_text, text=f"Quiz Complete Your Score is:\n"
                                                                 f"{self.quiz.score}/{len(self.quiz.question_list)}")



        def ans_false():

            user_answer = "False"
            self.response = user_answer
            correct = self.quiz.score_check(user_answer=user_answer, question_answer=self.quiz.q_answer)
            feeback(correct)
            self.scoreboard.config(text=f"Score:{self.quiz.score} ", font=("Arial", 10, "normal"))
            if self.quiz.still_has_question():
                next_question()
                self.display.itemconfig(self.question_text, text=f"{self.quiz.q_text}")
            else:
                self.display.itemconfig(self.question_text, text=f"Quiz Complete Your Score is:\n"
                                                                 f"{self.quiz.score}/{len(self.quiz.question_list)}")

        self.button_true = Button(command=ans_true)
        self.button_true.config(text="True")
        self.button_true.grid(column=0, row=2)

        self.button_false = Button(command=ans_false)
        self.button_false.config(text="False")
        self.button_false.grid(column=1, row=2)

        self.display = Canvas(border=20)
        self.display.bg = "White"
        self.display.config(height=250, width=300,bg=self.display.bg)
        self.question_text = self.display.create_text(150, 125,
                                                      text=f"{self.quiz.q_text}",
                                                      font=("Arial", 15, "italic"),
                                                      width=250)
        self.display.grid(row=1, column=0, columnspan=2, pady=50)

        self.scoreboard = Label(bg=THEME_COLOUR, fg="white")
        self.scoreboard.config(text=f"Score:{self.quiz.score} ", font=("Arial", 10, "normal"))
        self.scoreboard.grid(row=0, column=1)

        self.window.mainloop()


