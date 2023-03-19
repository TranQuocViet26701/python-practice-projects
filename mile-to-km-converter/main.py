from tkinter import *

FONT = ("Arial", 16, "normal")


def handle_calculate():
    result["text"] = round(float(mile_input.get()) * 1.61, 2)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=100)
window.config(padx=10, pady=10)

mile_input = Entry(width=5)
mile_input.grid(column=1, row=0)
mile_input.focus_set()

mile_unit_label = Label(text="Miles", font=FONT)
mile_unit_label.grid(column=2, row=0)


equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)

result = Label(text="", font=FONT)
result.grid(column=1, row=1)

km_unit_label = Label(text="Km", font=FONT)
km_unit_label.grid(column=2, row=1)

button = Button(text="Calculate", command=handle_calculate)
button.grid(column=1, row=2)

window.mainloop()

