from tkinter import *
from tkinter import messagebox #this is not a class so had to import separately
import random
import pyperclip
import json

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(2, 5) #password will have between 2 - 5 letters
    nr_symbols = random.randint(2, 4)  #2 - 4 symbols
    nr_numbers = random.randint(2, 4)  #2 - 4 numbers
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry_label.insert(0, password)
    #copy password to clipboard for easy pasting
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def write_info_to_file():
    website = website_entry_label.get()
    username = username_entry_label.get()
    password = password_entry_label.get()
    #json structure
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }
    #check if any field is empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure no field is empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #update old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry_label.delete(0, END)
            password_entry_label.delete(0, END)
            username_entry_label.delete(0, END)
            username_entry_label.insert(0, "common@email.com")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#canvas allows us to place things on top pf each other
canvas = Canvas(width=200, height=200)
#add logo image to canvas
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1)


#website text label
website_text_label = Label(text="Website:", font=(FONT_NAME, 10, "bold"))
website_text_label.grid(row=1, column=0)

#website entry label
website_entry_label = Entry(width=35)
website_entry_label.grid(row=1, column=1, columnspan=2)
#bring cursor to this entry box
website_entry_label.focus()

#username text label
username_text_label = Label(text="Email/Username:", font=(FONT_NAME, 10, "bold"))
username_text_label.grid(row=2, column=0)

#username entry label
username_entry_label = Entry(width=35)
username_entry_label.grid(row=2, column=1, columnspan=2)
#use default email address as username
username_entry_label.insert(0, "common@email.com")

#password text label
password_text_label = Label(text="Password:", font=(FONT_NAME, 10, "bold"))
password_text_label.grid(row=3, column=0)

#password entry label
password_entry_label = Entry(width=21)
password_entry_label.grid(row=3, column=1)

#generate password button
generate_password_button = Button(text="Generate Password", command=password_gen)
generate_password_button.grid(row=3, column=2)

#add button
add_button = Button(text="Add", width=36, command=write_info_to_file)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()