import tkinter as tk
from tkinter import messagebox

def login():
    username = "matas"
    password = "matas123"
    if username_entry.get() == username and password_entry.get() == password:
        print("Succsess")
        messagebox.showinfo(title  ="LOGGED IN", message="Succsesfully logged in!" )
    else:
        messagebox.showinfo(title  ="ERROR", message="Error was acured!" )
def shortcut(event):
    if event.state == 8 and event.keysym == "Return" and login():
        login
        
back_color = "#5b5b5b"
input_color = "#e4e0d5"

window = tk.Tk()
window.title("Log in page")
window.geometry("400x400")
window.configure(bg = back_color)

frame = tk.Frame(bg = back_color)

login_label = tk.Label(frame, text="Login", bg = back_color, fg = "#FF3399", font = ("Arial", 32))
username_label = tk.Label(frame, text = "Username", bg = back_color, font = ("Arial", 16), fg = "#FFFFFF")
username_entry = tk.Entry(frame, bg = input_color, font = ("Arial", 12))
password_entry = tk.Entry(frame, show="*", bg = input_color, font = ("Arial", 12))
password_label = tk.Label(frame, text="Password", bg = back_color, font = ("Arial", 16), fg = "#FFFFFF")
login_button = tk.Button(frame, text = "Login", bg = "#FF3399", fg = "#FFFFFF", command=login)
password_entry.bind("<KeyPress>", shortcut)



login_label.grid(row = 0, column= 0 , columnspan=2, pady = 50)
username_label.grid(row=1, column=0,  pady = 10)
username_entry.grid(row=1, column=1)
password_label.grid(row = 2, column= 0)
password_entry.grid(row=2, column=1)
login_button.grid(row=3, column=0, columnspan=2, pady = 50)

frame.pack()

window.mainloop()