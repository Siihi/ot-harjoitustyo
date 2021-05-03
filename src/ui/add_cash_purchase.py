from tkinter import ttk, StringVar, constants
from services.service import service, InvalidCredentialsError

class AddCashPurchase:
    def __init__(self, root, handle_show_budget):
        self.root = root
        self.frame = None
        self.handle_show_budget = handle_show_budget
        self.amount = None
        self.shop = None
        self.date = None
        self.error_variable = None
        self.error_label = None
        self.user = service.current_user()
        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def cash_handler(self):
        amount = self.amount.get()
        shop = self.shop.get()
        date = self.date.get()
        try:
            service.addcashpurchase(amount, shop, date)
            self.handle_show_budget()
        except InvalidCredentialsError:
            self.show_error("Rahamäärä tai päivämäärä kirjoitettu väärin")

    def show_error(self, message):
        self.error_variable.set(message)
        self.error_label.grid()

    def hide_error(self):
        self.error_label.grid_remove()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        self.error_variable = StringVar(self.frame)
        self.error_label = ttk.Label(master=self.frame, textvariable=self.error_variable, foreground="red")

        heading_label = ttk.Label(master=self.frame, text="Lisää käteisosto (muodossa -0,00) päivämääränä (muodossa 30.09.2000)")

        amount_label = ttk.Label(master=self.frame, text="Määrä")
        self.amount = ttk.Entry(master=self.frame)
        shop_label = ttk.Label(master=self.frame, text="Kauppa")
        self.shop = ttk.Entry(master=self.frame)
        date_label = ttk.Label(master=self.frame, text="Päivämäärä")
        self.date = ttk.Entry(master=self.frame)

        go_button = ttk.Button(master=self.frame, text="OK", command=self.cash_handler)
        back_button = ttk.Button(master=self.frame, text="Takaisin", command=self.handle_show_budget)

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        amount_label.grid(row=1, column=0)
        self.amount.grid(row=1, column=1, sticky=constants.W, padx=4, pady=4, ipadx=10)
        shop_label.grid(row=2, column=0)
        self.shop.grid(row=2, column=1, sticky=constants.W, padx=4, pady=4, ipadx=30)
        date_label.grid(row=3, column=0)
        self.date.grid(row=3, column=1, sticky=constants.W, padx=4, pady=4, ipadx=30)
        
        go_button.grid(row=4, column=0, sticky=constants.E, padx=4, pady=4)
        back_button.grid(row=4, column=1, sticky=constants.W, padx=4, pady=4)
        self.error_label.grid(row=5, column=0, columnspan=2, padx=4, pady=4, sticky=constants.W)

        self.hide_error()
        self.frame.grid_columnconfigure(1, weight=1, minsize=400)