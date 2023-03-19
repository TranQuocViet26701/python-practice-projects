import random
from tkinter import *
from tkinter import messagebox
import json


# ------------------------------ SEARCH WEBSITE --------------------------------- #
def search_website():
    website = website_input.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        found_website = data[website]
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    except KeyError:
        messagebox.showerror(title="Error", message="Website Not Found.")
    else:
        messagebox.showinfo(title=website, message=f"Email: {found_website['email']}\n"
                                                   f"Password: {found_website['password']}\n")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    return password


def handle_generate_button():
    password = generate_password()
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    is_empty = not (website and email and password)

    if is_empty:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"There are the details entered: \nEmail: {email} \nPassword: {password}")

    if is_ok:
        try:
            # How to load data from json file to dict
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # print(data)  # type: dict
        except FileNotFoundError:
            # Write data to json file
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            # Write data to json file
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            # Clear data when add successful
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# LOGO
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# WEBSITE TITLE
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# EMAIL/USERNAME TITLE
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

# PASSWORD TITLE
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# WEBSITE INPUT
website_input = Entry(width=20)
website_input.grid(column=1, row=1)

# EMAIL/USERNAME INPUT
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "tranquocviet26701@gmail.com")

# PASSWORD INPUT
password_input = Entry(width=20)
password_input.grid(column=1, row=3)

# SEARCH BUTTON
generate_button = Button(text="Search", width=11, highlightthickness=0, command=search_website)
generate_button.grid(column=2, row=1)

# GENERATE PASSWORD BUTTON
generate_button = Button(text="Generate Password", width=11, highlightthickness=0, command=handle_generate_button)
generate_button.grid(column=2, row=3)

# ADD BUTTON
add_button = Button(text="Add", width=32, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
