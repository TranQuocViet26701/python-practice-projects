import random
from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/vietnam_words.csv")
except pandas.errors.EmptyDataError:
    df = pandas.read_csv("data/vietnam_words.csv")
finally:
    to_learn = df.to_dict(orient="records")
    print(to_learn)


def check_card():
    to_learn.remove(current_card)
    to_learn_df = pandas.DataFrame(to_learn)
    to_learn_df.to_csv("data/words_to_learn.csv", index=False)
    random_card()


def flip_card():
    canvas.itemconfigure(card_image, image=card_back_image)
    canvas.itemconfigure(language_title, text="English", fill="white")
    canvas.itemconfigure(word, text=current_card["English"], fill="white")


def random_card():
    global flip_timer
    window.after_cancel(flip_timer)

    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfigure(language_title, text="Tiếng Việt", fill="black")
    canvas.itemconfigure(word, text=current_card["Vietnam"], fill="black")

    flip_timer = window.after(3000, flip_card)


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 260, image=card_front_image)
language_title = canvas.create_text(400, 150, fill="black", text="", font=TITLE_FONT)
word = canvas.create_text(400, 260, fill="black", text="", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)


# Wrong Button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, width=100, height=100,
                      highlightthickness=0, borderwidth=0, command=random_card)
wrong_button.grid(column=0, row=1)

# Right Button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, width=100, height=100,
                      highlightthickness=0, borderwidth=0, command=check_card)
right_button.grid(column=1, row=1)

current_card = random.choice(to_learn)
flip_timer = window.after(3000, flip_card)
random_card()
window.mainloop()


