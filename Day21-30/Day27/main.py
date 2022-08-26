from cgitb import text
from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    km_result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

#Entry box
miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

#miles label
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

#is equal label
is_equal_label = Label(text="is qual to")
is_equal_label.grid(row=1, column=0)

# km result label
km_result_label = Label(text="0")
km_result_label.grid(row=1, column=1)

# km label
km_label = Label(text="Km")
km_label.grid(row=1, column=2)

#calculate button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)

window.mainloop()
