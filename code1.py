from tkinter import *
from tkinter import messagebox

def login():
    if username.get()=='Taniv' and password.get()=='Tanivgoyal1808':
        root.destroy()
        import code2


    else:
        messagebox.showerror("Error", "Invalid")


def exit1():
    op=messagebox.askyesno("Exit",'Are you sure to exit?')
    if op>0:
        root.destroy()
def reset():
    username.set('')
    password.set('')

root = Tk()

root.geometry('1350x700')

root.title('Record System')
bg_color='#074463'

F1=Frame(root,bd=4,relief=GROOVE,bg='gold')
F1.place(x=450,y=150,width=450,height=350)
lbl1=Label(F1,text='Log In',bg='red',font='georgia 30 bold' ).grid(row=0,column=0,pady=2)

#
username=StringVar()
password=StringVar()

user_label=Label(F1,text='Username',font='georgia 20 bold',bg=bg_color,fg='white').place(x=2,y=110)
pass_label=Label(F1,text='Password',font='georgia 20 bold',bg=bg_color,fg='white').place(x=2,y=200)

user_entry=Entry(F1,textvariable=username,bd=3,relief=GROOVE).place(x=200,y=120)

pass_entry=Entry(F1,show='*',textvariable=password,bd=3,relief=GROOVE).place(x=200,y=210)

login_btn=Button(F1,text='Login',font='arial 8 bold',command=login).place(x=80,y=280,width=60)
login_btn=Button(F1,text='Reset',font='arial 8 bold',command=reset).place(x=180,y=280,width=60)
login_btn=Button(F1,text='Exit',font='arial 8 bold',command=exit1).place(x=280,y=280,width=60)

root.mainloop()