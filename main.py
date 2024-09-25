from tkinter import *
from tkinter import messagebox
import pyperclip
from password_generator import Generate

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    gen = Generate()
    password = gen.generate_pass()
    pass_w.delete(0, END)
    pass_w.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_s.get()
    email = user_n.get()
    password = pass_w.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Empty Field", message="Don't leave fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIf it is correct, press 'Ok' to save.")
        if is_ok:
            with open("saved_passwords.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
                web_s.delete(0, END)
                pass_w.delete(0, END)
                web_s.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Entry
web_s = Entry(width=37)
web_s.focus()
web_s.grid(row=1, column=1, columnspan=2)

user_n = Entry(width=37)
user_n.insert(END, "rrmfajardo@gmail.com")
user_n.grid(row=2, column=1, columnspan=2)

pass_w = Entry(width=21)
pass_w.grid(row=3, column=1, columnspan=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Buttons
generate_pass = Button(text="Generate Password", width=12, command=generate_password)
generate_pass.grid(row=3, column=2, columnspan=1)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()