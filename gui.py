## GUI Application ##

import tkinter as tk
from tkinter import ttk
import os

win=tk.Tk()
win.title('GUI')
 #******* Creat Level *******#

name_level=ttk.Label(win, text= "Enter your Name: ")
name_level.grid(row=0, column=0, sticky=tk.W)
email_level=ttk.Label(win, text="Enter your e-mail: ")
email_level.grid(row=1, column=0, sticky=tk.W)
age_level=ttk.Label(win, text="Enter your age: ")
age_level.grid(row=2, column=0, sticky=tk.W)
gender_level=ttk.Label(win, text="Enter your gender")
gender_level.grid(row=3, column=0)

# ******* Entry box Create ******* #
name_var=tk.StringVar()
name_entrybox=ttk.Entry(win, width= 16, textvariable=name_var)
name_entrybox.grid(row=0, column=1)

email_var=tk.StringVar()
email_entrybox=ttk.Entry(win, width= 16, textvariable=email_var)
email_entrybox.grid(row=1,column=1)

age_var=tk.StringVar()
age_entrybox=ttk.Entry(win, width= 16, textvariable= age_var)
age_entrybox.grid(row=2, column=1)

# ******* Combobox Create ******* #

gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win, width=13, textvariable=gender_var, state='readonly')
gender_combobox['value']=('Male', 'Female', 'Other')
gender_combobox.current(0)
gender_combobox.grid(row=3, column=1)

# ******* Radio Button ******* #

user_type_var=tk.StringVar()
radiobt1=ttk.Radiobutton(win, text='Student',value='Student', variable=user_type_var)
radiobt1.grid(row=4, column=0)

radiobt2=ttk.Radiobutton(win, text="Teacher", value="Teacher", variable=user_type_var)
radiobt2.grid(row=4, column=1)

# ******* Check Button ******* #

check_var=tk.IntVar()
check_bt=ttk.Checkbutton(win, text="If you want to get mail for update: ", variable=check_var)
check_bt.grid(row=5, columnspan=3)

# ******* If want to store file in text formate ******* #

def action():
    UserName=name_var.get()
    UserAge=age_var.get()
    UserEmail=email_var.get()
    UserGender=gender_var.get()
    UserType=user_type_var.get()
    UserMailUpdate=check_var.get()
    if check_var.get()==0:
        Subscribe="Yes"
    else:
        Subscribe='No'

    with open("texts.txt", 'a') as f:
        f.write(f"{UserName}, {UserAge}, {UserEmail}, {UserGender}, {UserType}, {UserMailUpdate}")

# ******* Submit Button ******* #

submit_bt=ttk.Button(win, text='Submit', command=action)
submit_bt.grid(row=6,column=1)


win.mainloop()










