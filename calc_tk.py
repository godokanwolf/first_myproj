import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = tk.StringVar()
        self.entered_number = tk.StringVar()
        self.entered_number.set('0')
        self.total.set('0')

        self.entry = tk.Entry(master, textvariable=self.entered_number)
        self.entry.grid(row=0, column=0, columnspan=4, pady=5)

        self.create_button("1", 1, 1)
        self.create_button("2", 1, 2)
        self.create_button("3", 1, 3)
        self.create_button("4", 2, 1)
        self.create_button("5", 2, 2)
        self.create_button("6", 2, 3)
        self.create_button("7", 3, 1)
        self.create_button("8", 3, 2)
        self.create_button("9", 3, 3)
        self.create_button("0", 4, 2)
        self.create_button("C", 4, 1)
        self.create_button("=", 4, 3)
        self.create_button("+", 1, 4)
        self.create_button("-", 2, 4)
        self.create_button("*", 3, 4)
        self.create_button("/", 4, 4)

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, command=lambda: self.button_click(text))
        button.grid(row=row, column=column)

    def button_click(self, text):
        if text == "=":
            try:
                self.total.set(eval(self.entry.get()))
                self.entered_number.set("0")
            except:
                self.total.set("Error")
                self.entered_number.set("0")
        elif text == "C":
            self.total.set("0")
            self.entered_number.set("0")
        else:
            if self.entered_number.get() == "0":
                self.entered_number.set(text)
            else:
                self.entered_number.set(self.entered_number.get() + text)

root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()