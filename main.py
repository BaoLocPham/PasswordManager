from tkinter import *
# not really sure why import * not import all modules :v
from tkinter import messagebox
import random
import pyperclip

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ----------------------------------- Generate Random password  --------------------------------------------- #
def random_password():
    password_list = []
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list += [random.choice(LETTERS) for _ in range(nr_letters)]
    password_list += [random.choice(SYMBOLS) for _ in range(nr_symbols)]
    password_list += [random.choice(NUMBERS) for _ in range (nr_numbers)]

    random.shuffle(password_list)
    password = ''.join(password_list)
    pyperclip.copy(password)
    messagebox.showinfo(title="Generate successful", message=f"Password: {password} already copied to clipboard")
    password_input.delete(0, END)
    password_input.insert(0, password)


# --------------------------------- Saving Password --------------------------------------------- #
def saving_password():
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Info", message="uh oh, make sure you haven't left any field")
    else:
        if messagebox.askokcancel(title="Saving password", message=f"There are details entered: {website}\n"
                                                                f"Email: {email}\n Password: {password}\n"
                                                                f"Is it okay to save?"):
            with open("data_password.txt", "a") as file:
                file.write(website+"|"+email+"|"+password+"\n")


# --------------------------------------------- Setting UI --------------------------------------------- #
# window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# create canvas to import img
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="C:/StudyingandExaminations/Python/100Days project/Day29/PasswordManager/img/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# col 1
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username: ")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# col 2
website_input = Entry(width=52)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
###

email_username_input = Entry(width=52)
email_username_input.grid(row=2, column=1, columnspan=2)


password_input = Entry(width=33)
password_input.grid(row=3, column=1)

# col 3
generate_password_button = Button(text="Generate Password", command=random_password)
generate_password_button.grid(row=3, column=2)

# row 4
add_button = Button(text="Add", width=44, command=saving_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()