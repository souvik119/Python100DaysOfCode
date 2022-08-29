from tkinter import *
from tkinter import messagebox #this is not a class so had to import separately

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def write_info_to_file():
    website = website_entry_label.get()
    username = username_entry_label.get()
    password = password_entry_label.get()
    #check if any field is empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure no field is empty!")
    else:
        #create a message box check if satisfied with the entered details
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered : \nEmail : {username}\nPassword: {password}\nIs it okay to save?")
        if is_okay:
            with open("data.txt", mode="a") as f:
                f.write(f"{website} | {username} | {password}\n")
            website_entry_label.delete(0, END)
            password_entry_label.delete(0, END)

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
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

#add button
add_button = Button(text="Add", width=36, command=write_info_to_file)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()