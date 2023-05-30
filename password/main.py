from tkinter import *
import random
from tkinter import messagebox
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

up_letters = [l.upper() for l in letters]

punc = ['!', '#', '$', '%', '&', '*', '+', '-', '<', '>', '?', '@', '_',
        '|', '~']
numbers = [str(n) for n in range(0, 10)]


def password_generator():
    generated_password = []
    letter_choice = [random.choice(letters) for _ in range(3)]
    up_letters_choice = [random.choice(up_letters) for _ in range(3)]
    punch_choice = [random.choice(punc) for _ in range(3)]
    number_choice = [random.choice(numbers) for _ in range(3)]

    for n in letter_choice:
        generated_password.append(n)

    for n in up_letters_choice:
        generated_password.append(n)

    for n in punch_choice:
        generated_password.append(n)
    for n in number_choice:
        generated_password.append(n)

    random.shuffle(generated_password)
    generated_password = ''.join(generated_password)
    psw_entry.delete(0, END)
    psw_entry.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website_data=web_entry.get()
    mail_data=mail_entry.get()
    password_data=psw_entry.get()
    new_data={
        website_data:{
            "email":mail_data,
            "password":password_data,
        }
    }

    try:
        with open("saved_data.json", "r") as data_file:
            data=json.load(data_file)


    except FileNotFoundError:

        with open("saved_data.json","w") as data_file:
            json.dump(new_data,data_file,indent=4)

    else:

        data.update(new_data)
        with open("saved_data.json","w") as data_file:
            json.dump(data,data_file,indent=4)
            # file.write("-----------------------------\n")
            # file.write(f"Website:{website_data}\n")
            # file.write(f"User Name:{mail_data}\n")
            # file.write(f"Password:{password_data}\n")
            # file.write("-----------------------------\

    finally:

        psw_entry.delete(0, END)
        web_entry.delete(0, END)



# --------------------------Search--------------------------------------#


def find_the_password():
    website_data=web_entry.get()

    try:
        with open("saved_data.json","r") as data_file:
            data = json.load(data_file)
            e_mail=data.get (website_data,{}).get("email")
            s_password=data.get (website_data,{}).get("password")
            messagebox.askokcancel(title=website_data, message=(f"Your mail is:{e_mail} \n Your password is:{s_password}"))
    except :
        messagebox.showinfo(title="Error", message="No data file found.")
        


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(height=250, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
text_web = Label(text="Website ")
text_web.grid(column=0, row=1)

text_mail = Label(text="Email/Username: ")
text_mail.grid(column=0, row=2)

text_psw = Label(text="Password ")
text_psw.grid(column=0, row=3)

# Entries
web_entry = Entry(width=25)
web_entry.grid(column=1, row=1, columnspan=2, sticky="w")
web_entry.focus()

mail_entry = Entry(width=35)
mail_entry.grid(column=1, row=2, columnspan=2, sticky="w")

psw_entry = Entry(width=25)
psw_entry.grid(column=1, row=3, columnspan=1, sticky="w")

# Button
generat_button = Button(text="Password Generator", command=password_generator)
generat_button.grid(column=2, row=3, sticky="e")

add_button = Button(text="Add", width=36,command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

search_button=Button(text="   Search    " , command=find_the_password,width=13)
search_button.grid(column=2,row=1,sticky="e")

window.mainloop()
