
from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("password saver")
window.config(padx=50, pady=50)

canvas=Canvas(width=500, height=500)
logo=PhotoImage(file="logo.png")
canvas.create_image(250,200,image=logo)
canvas.grid(column=1,row=1)



window.mainloop()