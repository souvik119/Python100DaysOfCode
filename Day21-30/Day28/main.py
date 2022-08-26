from email.mime import image
from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Timer text
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
timer_label.grid(row=0, column=1)

#canvas allows us to place things on top pf each other
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
#add tomato image to canvas
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


#start button
start_button = Button(text="Start", highlightthickness=0)
start_button.grid(row=2, column=0)

#reset button
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(row=2, column=2)

#check mark
check_label = Label(text="✔", fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
check_label.grid(row=3, column=1)


window.mainloop()