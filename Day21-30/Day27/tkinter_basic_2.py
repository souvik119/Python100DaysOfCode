from tkinter import *

window = Tk()
window.title("My Second GUI program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="First Label Text", font=("Arial", 24, "bold"))
my_label.pack()


#Button
def button_click():
    #change the my_label property by using config()
    my_label.config(text="Button got Clicked")

def user_input_display():
    new_text = user_input.get()
    my_label.config(text=new_text)

button = Button(text="Click me", command=user_input_display)
button.pack()

#Entry
user_input = Entry(width=10)
user_input.pack()


#challenge : change my_label value to whatever user inputs when button is clicked


window.mainloop()