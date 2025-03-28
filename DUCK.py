import tkinter as tk
from playsound import playsound

class GUI():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x800")

        self.first_button = tk.Button(self.window, text="Shot", height=8, width=8, font=(None, 10), command=self.sound)
        self.first_button.pack()

        self.window.mainloop()

    def sound(self):
        playsound("Desktop/projects/duck.mp3")

GUI()