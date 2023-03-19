import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
timer_running = False


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfigure(timer_text, text="25:00")
    check_mark.config(text="")
    time_label.config(text="Timer")
    global reps, timer_running
    reps = 0
    timer_running = False


# ---------------------------- TIMER MECHANISM ------------------------------- #
def handle_start_button():
    global timer_running

    if not timer_running:
        start_timer()

    # Display number of check_marks when the work is done
    marks = ""
    work_sessions = math.floor(reps / 2)
    for _ in range(work_sessions):
        marks += "✔"
    check_mark.config(text=marks)


def start_timer():
    global reps, timer_running
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    timer_running = True
    reps += 1

    if reps % 8 == 0:
        time_label.config(text="Break", fg=RED)
        count_down(long_break_seconds)
    elif reps % 2 == 0:
        time_label.config(text="Break", fg=PINK)
        count_down(short_break_seconds)
    else:
        time_label.config(text="Work", fg=GREEN)
        count_down(work_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minutes = f"00{math.floor(count / 60)}"[-2:]
    count_seconds = f"00{count % 60}"[-2:]
    canvas.itemconfigure(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1, count_down, count - 1)
    else:
        global timer_running
        timer_running = False


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

time_label = Label(text="Timer", font=(FONT_NAME, 50, "normal"), bg=YELLOW, fg=GREEN)
time_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="25:00", font=(FONT_NAME, 36, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", highlightthickness=0, command=handle_start_button)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

check_mark = Label(font=(FONT_NAME, 24, "normal"), fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)


window.mainloop()
