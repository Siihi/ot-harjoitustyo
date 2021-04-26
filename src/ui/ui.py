from tkinter import Tk, ttk, constants

class UI:
    def __init__(self, root):
        self.root = root

    def start(self):
        heading_label = ttk.Label(master=self.root, text="Sisäänkirjautuminen")

        username_label = ttk.Label(master=self.root, text="Käyttäjänimi:")
        username_entry = ttk.Entry(master=self.root)

        password_label = ttk.Label(master=self.root, text="Salasana:")
        password_entry = ttk.Entry(master=self.root)

        button = ttk.Button(master=self.root, text="Kirjaudu sisään")

        heading_label.grid(row=0, column=0, columnspan=2)

        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)

        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)

        button.grid(row=3, column=0, columnspan=2)

    def button_click(self):
        pass

window = Tk()
window.title("Budjetointisovellus")

ui = UI(window)
ui.start()

window.mainloop()