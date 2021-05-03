from tkinter import ttk, StringVar, constants
from services.service import service, UsernameExistsError


class CreateUserView:
    def __init__(self, root, handle_create_user, handle_show_login_view):
        self.root = root
        self.handle_create_user = handle_create_user
        self.handle_show_login_view = handle_show_login_view
        self.frame = None
        self.username_entry = None
        self.password_entry = None
        self.trial_entry = None
        self.error_variable = None
        self.error_label = None
        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def create_user_handler(self):
        username = self.username_entry.get()
        trial = self.trial_entry.get()
        password = self.password_entry.get()

        if password != trial:
            self.show_error("Salasanat eivät täsmää")
            return
        if len(username) == 0 or len(password) == 0 or len(trial) == 0:
            self.show_error("Kaikki kentät pitää olla täytettynä")
            return
        try:
            service.register(username, password)
            self.handle_create_user()
        except UsernameExistsError:
            self.show_error("Käyttäjätunnus on jo olemassa")

    def show_error(self, message):
        self.error_variable.set(message)
        self.error_label.grid()

    def hide_error(self):
        self.error_label.grid_remove()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        self.error_variable = StringVar(self.frame)
        self.error_label = ttk.Label(master=self.frame, textvariable=self.error_variable, foreground="red")

        heading_label = ttk.Label(master=self.frame, text="Rekisteröidy")

        username_label = ttk.Label(master=self.frame, text="Käyttäjätunnus")
        self.username_entry = ttk.Entry(master=self.frame)

        password_label = ttk.Label(master=self.frame, text="Salasana")
        self.password_entry = ttk.Entry(master=self.frame, show="*")

        trial_label = ttk.Label(master=self.frame, text="Salasana uudelleen")
        self.trial_entry = ttk.Entry(master=self.frame, show="*")

        create_user_button = ttk.Button(master=self.frame, text="Luo", command=self.create_user_handler)
        login_button = ttk.Button(master=self.frame, text="Kirjaudu sisään", command=self.handle_show_login_view)

        self.frame.grid_columnconfigure(1, weight=1, minsize=400)

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=4, pady=4)
        username_label.grid(row=1, column=0, sticky=constants.W, padx=4, pady=4)
        self.username_entry.grid(row=1, column=1, sticky=constants.W, padx=4, pady=4, ipadx=30)
        password_label.grid(row=2, column=0, sticky=constants.W, padx=4, pady=4)
        self.password_entry.grid(row=2, column=1, sticky=constants.W, padx=4, pady=4, ipadx=30)
        trial_label.grid(row=3, column=0, sticky=constants.W, padx=4, pady=4)
        self.trial_entry.grid(row=3, column=1, sticky=constants.W, padx=4, pady=4, ipadx=30)

        create_user_button.grid(row=4, column=0, sticky=constants.W, padx=4, pady=4)
        login_button.grid(row=4, column=1, sticky=constants.W, padx=4, pady=4)

        self.error_label.grid(row=5, column=0, columnspan=2, sticky=constants.W)
        self.hide_error()