from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def save():
    if Name.get()=='':
        messagebox.showerror("Error","Name must be required!!")
    else:
        f=open('files.txt','w')
        f.write(
                    str(f"Name :{Name.get()}\n")      +
                    str(f"Roll_NO :{Roll_NO.get()}\n")   +
                    str(f"Course :{Course.get()}\n")    +
                    str(f"Address :{Address.get()}\n")   +
                    str(f"City :{City.get()}\n")     +
                    str(f"Contact:{Contact.get()}\n")   +
                    str(f"Date:{Date.get()}\n")      +
                    str(f"Degree:{Date.get()}\n")    +
                    str(f"Id_proof:{Id_proof.get()}\n")  +
                    str(f"Payment:{Payment.get()}")
              )
        f.close()
        messagebox.showinfo("Success",'Record Saved!!')

def clear():
    Name.set('')
    Roll_NO.set('')
    Course.set('')
    Address.set('')
    City.set('')
    Contact.set('')
    Date.set('')
    Degree.set('')
    Id_proof.set('')
    Payment.set('')


def logout():
    root.destroy()
    import code1


def exit1():
    ask=messagebox.askyesno('Exit','Are you sure to exit?')
    if ask>0:
        root.destroy()

def open1():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = NONE
    else:
        root.title(os.path.basename(file) + "Record System")
        file_list.delete(1.0, END)
        f = open(file, "r")
        file_list.insert(1.0, f.read())
        f.close()


root=Tk()

root.geometry('1360x700')

root.title('File Record System')

lbl=Label(root,text='File Record System',bd=4,relief=GROOVE,font='georgia 20 bold',pady=2).pack(fill=X)
#
f1=Frame(root,relief=GROOVE,bd=5)
f1.place(width=700,height=400,x=4,y=80)

lbl1=Label(f1,text='Student Details',font='arial 20 bold').pack()

name_lbl=Label(f1,text='Name',font='arial 18 bold').place(x=4,y=70)

roll_lbl=Label(f1,text='Roll No',font='arial 18 bold').place(x=4,y=120)

course_lbl=Label(f1,text='Course',font='arial 18 bold').place(x=4,y=170)

addr_lbl=Label(f1,text='Address',font='arial 18 bold').place(x=4,y=220)

city_lbl=Label(f1,text='City',font='arial 18 bold').place(x=4,y=270)

contact_lbl=Label(f1,text='Contact No',font='arial 18 bold').place(x=350,y=70)

date_lbl=Label(f1,text='Date(dd/mm/yy)',font='arial 18 bold').place(x=350,y=120)

degree_lbl=Label(f1,text='Degree',font='arial 18 bold').place(x=350,y=170)

id_lbl=Label(f1,text='ID Proof',font='arial 18 bold').place(x=350,y=220)

pay_lbl=Label(f1,text='Payment Mode',font='arial 18 bold').place(x=350,y=270)


Name=StringVar()
Roll_NO=StringVar()
Course=StringVar()
Address=StringVar()
City=StringVar()
Contact=IntVar()
Date=StringVar()
Degree=StringVar()
Id_proof=StringVar()
Payment=StringVar()

name_entry=Entry(f1,textvariable=Name).place(x=140,y=80)

roll_entry=Entry(f1,textvariable=Roll_NO).place(x=140,y=130)

course_entry=Entry(f1,textvariable=Course).place(x=140,y=180)

address_entry=Entry(f1,textvariable=Address).place(x=140,y=230)

city_entry=Entry(f1,textvariable=City).place(x=140,y=280)

contact_entry=Entry(f1,textvariable=Contact).place(x=550,y=80)

date_entry=Entry(f1,textvariable=Date).place(x=550,y=130)

degree_combo=ttk.Combobox(f1,textvariable=Degree,state='readonly',width=17)
degree_combo['values']=('B-Tech','M-Tech','MCA','BCA','B.Sc')
degree_combo.place(x=550,y=180)

id_combo=ttk.Combobox(f1,textvariable=Id_proof,state='readonly',width=17)
id_combo['values']=('Id-card','License','Aadhar Card')
id_combo.place(x=550,y=230)

pay_combo=ttk.Combobox(f1,textvariable=Payment,state='readonly',width=17)
pay_combo['values']=('Paytm','G-Pay','PhonePay','NetBanking')
pay_combo.place(x=550,y=280)

#
f2=Frame(root,relief=GROOVE,bd=5)
f2.place(x=800,y=80,width=450,height=400)

bl2=Label(f2,text='File Data',font='arial 15 bold').pack()

scroll_y=Scrollbar(f2,orient=VERTICAL)
file_list=Text(f2,yscrollcommand=scroll_y.set)
file=NONE
scroll_y.pack(fill=Y,side=RIGHT)
scroll_y.config(command=file_list.yview)
file_list.pack(fill=BOTH,expand='yes')

#
btn_frame=Frame(root,relief=GROOVE,bd=5,bg='#074463')
btn_frame.place(x=4,y=530,width=1252,height=100)

save_btn=Button(btn_frame,text='Save',width=20,bg='white',pady=20,font='arial 12 bold',command=save).place(x=20,y=10)
del_btn=Button(btn_frame,text='Open',width=20,bg='white',pady=20,font='arial 12 bold',command=open1).place(x=270,y=10)
clr_btn=Button(btn_frame,text='Clear',width=20,bg='white',pady=20,font='arial 12 bold',command=clear).place(x=520,y=10)
logo_btn=Button(btn_frame,text='Log Out',width=20,bg='white',pady=20,font='arial 12 bold',command=logout).place(x=760,y=10)
exit_btn=Button(btn_frame,text='Exit',width=20,bg='white',pady=20,font='arial 12 bold',command=exit1).place(x=1000,y=10)

root.mainloop()