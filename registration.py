import hashlib 
from tkinter import *
from tkinter import messagebox
from firebase import firebase

firebase = firebase.FirebaseApplication("https://login-6adfa-default-rtdb.firebaseio.com/",None)
registration_window = Tk()
registration_window.title("REGISTER")
registration_window.geometry("400x400")
registration_window.configure(bg="darkorchid")

login_username_entry=""
login_password_entry=""

def login(): 
    print("login function")
    
def register(): 
    print("register function")
    username=username_entry.get()
    password=password_entry.get()
    coded= hashlib.md5(password.encode())
    code = coded.hexdigest()
    print(code)
    firebase.put("https://d-login-system-598f4-default-rtdb.firebaseio.com/",username,code)
    messagebox.showinfo("Registered","User is registered: ")
    
def login_window():
    login_window = Tk()
    login_window.title("LOGIN")
    login_window.geometry("400x400")
    login_window.configure(bg="MediumOrchid")
    
    global login_username_entry
    global login_password_entry
    registration_window.destroy()
    
    log_heading_label = Label(login_window, text="Log In" ,fg="DarkOrange4", font = 'arial 20 bold',bg="MediumOrchid")
    log_heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)
    
    login_username_label = Label(login_window, text="Username : " , fg="DarkOrange1",font = 'arial 13 bold',bg="MediumOrchid")
    login_username_label.place(relx=0.3,rely=0.4, anchor=CENTER)
    
    login_username_entry = Entry(login_window)
    login_username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)
    
    login_password_label = Label(login_window, text="Password : " , font = 'arial 13 bold',bg="MediumOrchid",fg="DarkOrange1")
    login_password_label.place(relx=0.3,rely=0.5, anchor=CENTER)
    
    login_password_entry = Entry(login_window)
    login_password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)
    
    btn_login = Button(login_window, text="Log In" , font = 'arial 13 bold' , command=login, relief=FLAT,bg="orchid4",fg="DarkGoldenrod1")
    btn_login.place(relx=0.5,rely=0.65, anchor=CENTER)
    
    login_window.mainloop()
    
    
heading_label = Label(registration_window, text="Register" , font = 'arial 20 bold',bg="darkorchid",fg="DarkGoldenrod1")
heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)

username_label = Label(registration_window, text="Username : " , font = 'arial 13',bg="darkorchid",fg="DarkGoldenrod1")
username_label.place(relx=0.3,rely=0.4, anchor=CENTER)

username_entry = Entry(registration_window)
username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)

password_label = Label(registration_window, text="Password :  " , font = 'arial 13',bg="darkorchid",fg="DarkGoldenrod1")
password_label.place(relx=0.3,rely=0.5, anchor=CENTER)

password_entry = Entry(registration_window)
password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)

btn_reg = Button(registration_window, text="Sign Up" , font = 'arial 13 bold' ,command=register, fg="DarkGoldenrod1",padx=10,bg="DarkOrchid4")
btn_reg.place(relx=0.5,rely=0.75, anchor=CENTER)

btn_login_window = Button(registration_window, text="Log In" , font = 'arial 10 bold' ,  command=login_window,bg="DarkOrchid4",fg="DarkGoldenrod1")

btn_login_window.place(relx=0.9,rely=0.06, anchor=CENTER)
registration_window.mainloop()