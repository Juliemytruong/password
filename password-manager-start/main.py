
from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("password saver")
window.geometry("500x500")
window.config(padx=20, pady=20)

canvas=Canvas(width=250, height=200)
logo=PhotoImage(file="logo.png")
canvas.create_image(150,100,image=logo)
canvas.grid(column=2,row=1)

label_web=Label(text="Website:")
label_web.grid(column=1,row=2)

entry_web=Entry(width=35)
entry_web.grid(column=2,row=2,columnspan=2)

label_user=Label(text="Username:")
label_user.grid(column=1,row=3)

entry_user=Entry(width=35)
entry_user.grid(column=2,row=3,columnspan=2)

label_pw=Label(text="password:")
label_pw.grid(column=1,row=4)

entry_pw=Entry(width=21)
entry_pw.grid(column=2,row=4)

button = Button(text="generate")
button.grid(column=3,row=4)

window.mainloop()