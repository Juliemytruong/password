
from tkinter import *
import random
import string
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pw():
    global entry_pw
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    entry_pw.delete(0,END)
    entry_pw.insert(0,f"{res}")
    print(res)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    text_for_add=f"\n{entry_web.get()}|{entry_user.get()}|{entry_pw.get()}"
    print(text_for_add)
    f = open("password.txt", "a")
    f.write(text_for_add)
    f.close()


# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("password saver")
#window.geometry("500x500")
window.config(padx=50, pady=50)

canvas=Canvas(width=200, height=200)
logo=PhotoImage(file="logo.png")
canvas.create_image(100,80,image=logo)
canvas.grid(column=2,row=0)

label_web=Label(text="Website:")
label_web.grid(column=1,row=1)

entry_web=Entry(width=38)
entry_web.focus()
entry_web.grid(column=2,row=1,columnspan=2)

label_user=Label(text="Username:")
label_user.grid(column=1,row=3)

entry_user=Entry(width=38)
entry_user.grid(column=2,row=3,columnspan=2)

entry_user.insert(0,"juliemytruong@gmail.com")

label_pw=Label(text="Password:")
label_pw.grid(column=1,row=4)

entry_pw=Entry(width=25)
entry_pw.grid(column=2,row=4)

button_gen = Button(text="generate",width=8,command=gen_pw)
button_gen.grid(column=3,row=4)

button_add = Button(text="add",width=33,command=add_to_file)
button_add.grid(column=2,row=5,columnspan=2)




window.mainloop()