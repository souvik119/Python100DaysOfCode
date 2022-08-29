from tkinter import *

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

#username text label
username_text_label = Label(text="Email/Username:", font=(FONT_NAME, 10, "bold"))
username_text_label.grid(row=2, column=0)

#username entry label
username_entry_label = Entry(width=35)
username_entry_label.grid(row=2, column=1, columnspan=2)

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
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()