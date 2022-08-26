import tkinter

#create window
window = tkinter.Tk()

window.title("My First GUI program")

#minimum size of window when it first starts up
window.minsize(width=500, height=300)

#create a label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
#put the label on screen
my_label.pack()

#keep the window on screen
#this has to be at the very end of the program
window.mainloop()