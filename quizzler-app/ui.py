from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.score_label.config(pady=20, padx=20)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Quiz question is here",
            fill="black",
            font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, columnspan=2, row=1, pady=20)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, borderwidth=0, command=self.handle_true_click)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, borderwidth=0, command=self.handle_false_click)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(background="white")

        if not self.quiz_brain.still_has_questions():
            self.canvas.itemconfig(self.question_text, text="You've reached at the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            return

        self.score_label.config(text=f"Score: {self.quiz_brain.score}")
        question_text = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.question_text, text=question_text)

    def handle_true_click(self):
        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)

    def handle_false_click(self):
        is_right = self.quiz_brain.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.window.after(1000, func=self.get_next_question)
        if is_right:
            self.canvas.configure(background="green")
        else:
            self.canvas.configure(background="red")


