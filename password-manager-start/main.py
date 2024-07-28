
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
import random
import string
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pw():
    # global entry_pw
    # res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    # entry_pw.delete(0,END)
    # entry_pw.insert(0,f"{res}")
    # print(res)

    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

  #  password_list = []

    pw_letter = [random.choice(letters) for _ in range(nr_letters)]
    pw_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    pw_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = pw_letter + pw_numbers + pw_symbols

    random.shuffle(password_list)

    password =''.join(password_list)

    entry_pw.insert(0,password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    #text_for_add=f"\n{entry_web.get()} | {entry_user.get()} | {entry_pw.get()}"
    #print(text_for_add)

    text_for_add={
        entry_web.get():{
            "user name":entry_user.get(),
            "password":entry_pw.get()
        }
    }


    if len(entry_web.get())==0 or len(entry_pw.get())==0:
        messagebox.showinfo("check data","check for empty cells")
    else:

        with open("password.json", "r") as f:
            data=json.load(f)
        print(data)

        with open("password.json","w"):

            data.update(text_for_add)
            json.dump(data,f,indent=4)

        f.close()



        entry_web.delete(0,END)
        entry_pw.delete(0,END)



#----------------------------findPW---------------------------------------#

def find_password():
    with open("password.json","r") as dataA:
        datap=json.load(dataA)
    print(datap)

    try:
        return_data=datap[entry_web.get()]
        print(return_data)
        return_user=return_data["email"]
        return_pw=return_data["password"]
    except KeyError:
        messagebox.showinfo("return info","no password created")
    else:
        messagebox.showinfo("return info",f"your user name is {return_user} and your passwords is {return_pw}")








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

entry_web=Entry(width=25)
entry_web.focus()
entry_web.grid(column=2,row=1,columnspan=1)

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

button_search = Button(text="search",width=8,command=find_password)
button_search.grid(column=3,row=1)


window.mainloop()