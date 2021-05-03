from tkinter import ttk, StringVar, constants
from services.service import service, InvalidCredentialsError

class LoginView:
    def __init__(self, root, handle_login, handle_show_create_user_view, handle_show_remove_user_view):
        self.root = root
        self.handle_login = handle_login
        self.handle_show_create_user_view = handle_show_create_user_view
        self.handle_show_remove_user_view = handle_show_remove_user_view
        self.frame = None
        self.username_entry = None
        self.password_entry = None
        self.error_variable = None
        self.error_label = None

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def login_handler(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            service.login(username, password)
            self.handle_login()
        except InvalidCredentialsError:
            self.show_error("Väärä käyttäjätunnus tai salasana")

    def show_error(self, message):
        self.error_variable.set(message)
        self.error_label.grid()

    def hide_error(self):
        self.error_label.grid_remove()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        self.error_variable = StringVar(self.frame)
        self.error_label = ttk.Label(master=self.frame, textvariable=self.error_variable, foreground="red")

        heading_label = ttk.Label(master=self.frame, text="Tervetuloa budjetointisovellukseen!")

        username_label = ttk.Label(master=self.frame, text="Käyttäjätunnus")
        self.username_entry = ttk.Entry(master=self.frame)

        password_label = ttk.Label(master=self.frame, text="Salasana")
        self.password_entry = ttk.Entry(master=self.frame, show="*")

        login_button = ttk.Button(master=self.frame, text="Kirjaudu sisään", command=self.login_handler)
        register_button = ttk.Button(master=self.frame, text="Rekisteröidy", command=self.handle_show_create_user_view)
        remove_button = ttk.Button(master=self.frame, text="Poista käyttäjä", command=self.handle_show_remove_user_view)

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        username_label.grid(row=1, column=0, columnspan=1, sticky=constants.W)
        self.username_entry.grid(row=1, column=1, columnspan=2, sticky=constants.W, padx=4, pady=4, ipadx=30)
        password_label.grid(row=2, column=0, columnspan=1, sticky=constants.W)
        self.password_entry.grid(row=2, column=1, columnspan=2, sticky=constants.W, padx=4, pady=4, ipadx=30)
        login_button.grid(row=3, column=0, sticky=constants.W, padx=4, pady=4)
        register_button.grid(row=3, column=1, sticky=constants.W, padx=4, pady=4)
        remove_button.grid(row=3, column=2, sticky=constants.W, padx=4, pady=4)
        self.error_label.grid(row=4, column=0, columnspan=2, padx=4, pady=4, sticky=constants.W)

        self.hide_error()
        self.frame.grid_columnconfigure(2, weight=1, minsize=400)