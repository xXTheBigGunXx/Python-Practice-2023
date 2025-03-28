import tkinter as tk
class GUI:
    def __init__(self):
        
        self.root_win = tk.Tk()
        self.root_win.configure(bg='#c0c0c0')
        self.root_win.geometry("500x800")
        self.root_win.title("Calculator")

        button_bg_color = "#999999"

        self.text_ = tk.StringVar()
        self.text_.set("")

        self.label = tk.Label(self.root_win, textvariable=self.text_, height=3, width=40, font=(10), bg = "#8188a1")
        self.label.pack(padx=50, pady=50)

        def clear():
            self.text_.set("")

        def equal():
            try:
                result = eval(self.text_.get())
                self.text_.set(str(result))
            except:
                self.text_.set("Error")

        def press(num):
            self.text_.set(self.text_.get() + str(num))

        self.buttonflame = tk.Frame(self.root_win)
        self.buttonflame.columnconfigure(0, weight=1)
        self.buttonflame.columnconfigure(1, weight=1)
        self.buttonflame.columnconfigure(2, weight=1)
        self.buttonflame.columnconfigure(3, weight=1)
        self.buttonflame.rowconfigure(4, weight=1)

        self.first_button = tk.Button(self.buttonflame, text = "First", height = 4, width=8 ,font = (10), bg = button_bg_color, command=lambda: press(1))
        self.first_button.grid(row=0, column=0, sticky = tk.W + tk.E)

        self.second_button = tk.Button(self.buttonflame, text = "Second", height = 4, width=8 ,font = (10), bg = button_bg_color, command=lambda: press(2))
        self.second_button.grid(row=0, column=1, sticky = tk.W + tk.E)

        self.third_button = tk.Button(self.buttonflame, text = "Third", height = 4, width=8 ,font = (10), bg = button_bg_color, command=lambda: press(3))
        self.third_button.grid(row=0, column=2, sticky = tk.W + tk.E)

        self.four_button = tk.Button(self.buttonflame, text = "four", height = 4, width=8 ,font = (10), bg = button_bg_color, command=lambda: press(4))
        self.four_button.grid(row=1, column=0, sticky = tk.W + tk.E)

        self.five_button = tk.Button(self.buttonflame, text = "Five", height = 4, width=8 ,font = (10), bg = button_bg_color, command=lambda: press(5))
        self.five_button.grid(row=1, column=1, sticky = tk.W + tk.E)

        self.six_button = tk.Button(self.buttonflame, text = "Six", height = 4, width=8 ,font = (10), bg = button_bg_color, command=lambda: press(6))
        self.six_button.grid(row=1, column=2, sticky = tk.W + tk.E)

        self.seven_button = tk.Button(self.buttonflame, text = "Seven", height = 4, width=8 ,font = (10), bg = button_bg_color, command=lambda: press(7))
        self.seven_button.grid(row=2, column=0, sticky = tk.W + tk.E)

        self.eight_button = tk.Button(self.buttonflame, text = "Eight", height = 4, width=8 ,font = (10), bg = button_bg_color, command=lambda: press(8))
        self.eight_button.grid(row=2, column=1, sticky = tk.W + tk.E)

        self.nine_button = tk.Button(self.buttonflame, text = "Nine", height = 4, width=8 ,font = (10), bg = button_bg_color, command=lambda: press(9))
        self.nine_button.grid(row=2, column=2, sticky = tk.W + tk.E)

        self.zero_button = tk.Button(self.buttonflame, text = "Zero", height = 4, width=8 ,font = (10), bg = button_bg_color, command=lambda: press(0))
        self.zero_button.grid(row=3, column=0, sticky = tk.W + tk.E)

        self.decimal_button = tk.Button(self.buttonflame, text = " . ", height = 4, width=8 ,font = (10), bg = button_bg_color, command=lambda: press("."))
        self.decimal_button.grid(row=3, column=1, sticky = tk.W + tk.E)

        self.equal_button = tk.Button(self.buttonflame, text = " = ", height = 4, width=8 ,font = (10), bg = button_bg_color, command=equal)
        self.equal_button.grid(row=3, column=2, sticky = tk.W + tk.E)

        self.plus_button = tk.Button(self.buttonflame, text = " + ", height = 4, width=8 ,font = (10), bg = button_bg_color, command=lambda: press("+"))
        self.plus_button.grid(row=0, column=3, sticky = tk.W + tk.E)

        self.minus_button = tk.Button(self.buttonflame, text = " - ", height = 4, width=8 ,font = (10), bg = button_bg_color, command=lambda: press("-"))
        self.minus_button.grid(row=1, column=3, sticky = tk.W + tk.E)

        self.times_button = tk.Button(self.buttonflame, text = " * ", height = 4, width=8 ,font = (10), bg = button_bg_color, command=lambda: press("*"))
        self.times_button.grid(row=2, column=3, sticky = tk.W + tk.E)

        self.devide_button = tk.Button(self.buttonflame, text = " / ", height = 4, width=8 ,font = (10), bg = button_bg_color, command=lambda: press("/"))
        self.devide_button.grid(row=3, column=3, sticky = tk.W + tk.E)

        self.clear = tk.Button(self.root_win, text="Clear", height=2, width=50, font=(10), bg=button_bg_color, command=clear)
        self.clear.pack(fill="x", padx=5, pady=1)

        self.buttonflame.pack(fill="x")

        self.root_win.mainloop()

GUI()