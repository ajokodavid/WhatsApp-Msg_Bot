import tkinter
from threading import Thread
from tkinter import messagebox

import pywhatkit as pwk
from tkinter import *

tk = tkinter.Tk()
tk.geometry("400x250")
tk.title(string="WhatsApp Messaging Bot")

def validate_phone_number():
    if ent1.get().startswith("0"):
        messagebox.showerror(title="Error", message="Replace the first 0 with your country phone number code")
    else:
      send_msg_to_contact()
def send_msg_to_contact():
    thread = Thread(target=send_msg, args=(ent1.get(), ent2.get()))
    thread.start()

def send_msg(phone_no, message):
    pwk.sendwhatmsg_instantly(phone_no=str(phone_no), message=str(message), wait_time=30)

lb1 = Label(text="Phone Number", fg="black")
lb1.grid(row=0,column=0)
ent1 = Entry(tk,fg="black")
ent1.grid(row=0,column=1)

lb2 = Label(text="Message", fg="black")

lb2.grid(row=1,column=0)
ent2 = Entry(tk,fg="black")
ent2.grid(row=1,column=1)

btn = Button(text="Submit", command=validate_phone_number)
btn.grid()
tk.mainloop()