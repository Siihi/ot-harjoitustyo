from tkinter import ttk, StringVar, constants
from services.service import service, InvalidCredentialsError

class AddInfo:
    def __init__(self, root, handle_show_budget):
        self.root = root
        self.frame = None
        self.handle_show_budget = handle_show_budget
        self.filename_entry = None
        self.error_variable = None
        self.error_label = None
        self.user = service.current_user()
        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def info_handler(self):
        infofile = self.filename_entry.get()
        try:
            service.addinfo(infofile)
            self.handle_show_budget()
        except InvalidCredentialsError:
            self.show_error("Tiedostoa ei löytynyt")

    def show_error(self, message):
        self.error_variable.set(message)
        self.error_label.grid()

    def hide_error(self):
        self.error_label.grid_remove()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        self.error_variable = StringVar(self.frame)
        self.error_label = ttk.Label(master=self.frame, textvariable=self.error_variable, foreground="red")

        heading_label = ttk.Label(master=self.frame, text="Lisää tietoja tiedostosta (varmista että tiedosto on data-kansiossa)")

        filename_label = ttk.Label(master=self.frame, text="Tiedoston nimi")
        self.filename_entry = ttk.Entry(master=self.frame)

        go_button = ttk.Button(master=self.frame, text="OK", command=self.info_handler)
        back_button = ttk.Button(master=self.frame, text="Takaisin", command=self.handle_show_budget)

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        filename_label.grid(row=1, column=0)
        self.filename_entry.grid(row=1, column=1, sticky=constants.W, padx=4, pady=4, ipadx=30)
        go_button.grid(row=3, column=0, sticky=constants.E, padx=4, pady=4)
        back_button.grid(row=3, column=1, sticky=constants.W, padx=4, pady=4)
        self.error_label.grid(row=4, column=0, columnspan=2, padx=4, pady=4, sticky=constants.W)

        self.hide_error()
        self.frame.grid_columnconfigure(1, weight=1, minsize=400)