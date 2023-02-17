import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Hesap Makinesi")

        # Ekran
        self.screen = tk.Entry(master, width=30, justify='right', font=('Arial', 16))
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Butonlar
        self.create_button('7', 1, 0)
        self.create_button('8', 1, 1)
        self.create_button('9', 1, 2)
        self.create_button('/', 1, 3)

        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('*', 2, 3)

        self.create_button('1', 3, 0)
        self.create_button('2', 3, 1)
        self.create_button('3', 3, 2)
        self.create_button('-', 3, 3)

        self.create_button('0', 4, 0)
        self.create_button('.', 4, 1)
        self.create_button('C', 4, 2)
        self.create_button('+', 4, 3)

        self.create_button('←', 5, 0)
        self.create_button('=', 5, 1, 3)

    def create_button(self, text, row, col, colspan=1, rowspan=1):
        button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 16), command=lambda: self.click(text))
        button.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan, padx=5, pady=5)

    def click(self, key):
        if key == 'C':
            self.screen.delete(0, tk.END)
        elif key == '←':
            self.screen.delete(len(self.screen.get())-1)
        elif key == '=':
            result = eval(self.screen.get())
            self.screen.delete(0, tk.END)
            self.screen.insert(0, result)
        else:
            self.screen.insert(tk.END, key)

root = tk.Tk()
#altaki satırı aktif etmek isterseniz lütfen turkey-flag.ico isimli bir ikon dosyasını bu kodun bulundugu dizie kaydedin
# root.iconbitmap('turkey-flag.ico')
calculator = Calculator(root)
root.mainloop()
