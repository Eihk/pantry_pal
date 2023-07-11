import tkinter as tk


class Gui:
    def __init__(self) -> None:
        self.window = tk.Tk()   # Instantiate window
        self.window.geometry("360x420")
        self.window.title('Pantry Pal')

        # icon = PhotoImage(file=logo.png) # for icon
        # window.iconphoto(True, icon)

        self.label = tk.Label(self.window, text = 'ENTER YOUR GROCERY LIST', font=('Arial'))
        self.label.pack(padx=20, pady=20)

        self.textbox = tk.Text(self.window, height=12 ,font=('Arial', 16))
        self.textbox.pack(padx=20)

        self.button = tk.Button(self.window, text='Done', font=('Arial', 12), command=self.close)
        self.button.pack(pady=10)

        self.window.mainloop()
    
    def close(self):
        self.retrieve_input()
        self.window.destroy()
        
    def retrieve_input(self):
        input = self.textbox.get("1.0",tk.END)
        with open('groceryList.txt', "w") as f:
            f.write(input)
            f.close()
            
