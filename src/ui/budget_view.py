from tkinter import ttk, StringVar, constants
from typing import Text
from services.service import service

class BudgetView:
    def __init__(self, root, handle_show_login_view, handle_show_add_info, handle_show_add_cash, handle_show_add_cash_purchase, handle_show_all_info):
        self.root = root
        self.frame = None
        self.handle_show_login_view = handle_show_login_view
        self.handle_show_add_info = handle_show_add_info
        self.handle_show_add_cash = handle_show_add_cash
        self.handle_show_add_cash_purchase = handle_show_add_cash_purchase
        self.handle_show_all_info = handle_show_all_info
        self.username_entry = None
        self.password_entry = None
        self.trial_entry = None
        self.error_variable = None
        self.error_label = None
        self.user = service.current_user()

        self.incomeofalltime = None
        self.expensesofalltime = None
        self.incomeofmonth = None
        self.expensesofmonth = None
        self.allinfo = None

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def show_error(self, message):
        self.error_variable.set(message)
        self.error_label.grid()

    def hide_error(self):
        self.error_label.grid_remove()

    def logout_handler(self):
        service.logout()
        self.handle_show_login_view()

    def allshowninfo(self):
        self.incomeofalltime = service.fetchincomeofalltime()
        self.expensesofalltime = service.fetchexpensesofalltime()
        self.incomeofmonth = service.fetchincomeofmonth()
        self.expensesofmonth = service.fetchexpensesofmonth()
        self.allinfo = service.fetchallinfos()
    
    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        self.error_variable = StringVar(self.frame)
        self.error_label = ttk.Label(master=self.frame, textvariable=self.error_variable, foreground="red")

        heading_label = ttk.Label(master=self.frame, text="Pääsivu")

        self.allshowninfo()
        monthincome_label = ttk.Label(master=self.frame, text=f"Kuukauden tulot: {self.incomeofmonth}")
        monthexpenses_label = ttk.Label(master=self.frame, text=f"Kuukauden menot: {self.expensesofmonth}")
        monthall_label = ttk.Label(master=self.frame, text=f"Kuukauden menot ja tulot yhteensä: {self.incomeofmonth + self.expensesofmonth:.2f}")
        allincome_label = ttk.Label(master=self.frame, text=f"Kaikki tulot: {self.incomeofalltime}")
        allexpenses_label = ttk.Label(master=self.frame, text=f"Kaikki menot: {self.expensesofalltime}")
        alltogether_label = ttk.Label(master=self.frame, text=f"Kaikki menot ja tulot yhteensä: {self.incomeofalltime + self.expensesofalltime:.2f}")

        add_info_button = ttk.Button(master=self.frame, text="Lisää tietoja", command=self.handle_show_add_info)
        add_cash_button = ttk.Button(master=self.frame, text="Lisää käteistä", command=self.handle_show_add_cash)
        add_cash_purchase_button = ttk.Button(master=self.frame, text="Lisää käteisosto", command=self.handle_show_add_cash_purchase)
        logout_button = ttk.Button(master=self.frame, text="Kirjaudu ulos", command=self.logout_handler)
        all_info_button = ttk.Button(master=self.frame, text="Kaikki tilitiedot", command=self.handle_show_all_info)

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        monthincome_label.grid(row=1, column=0, sticky=constants.W, padx=4, pady=4)
        monthexpenses_label.grid(row=1, column=1, columnspan=2, sticky=constants.W, padx=4, pady=4)
        monthall_label.grid(row=2, column=0, columnspan=2, sticky=constants.W, padx=4, pady=4)
        allincome_label.grid(row=3, column=0, sticky=constants.W, padx=4, pady=4)
        allexpenses_label.grid(row=3, column=1, columnspan=2, sticky=constants.W, padx=4, pady=4)
        alltogether_label.grid(row=4, column=0, columnspan=2, sticky=constants.W, padx=4, pady=4)

        add_info_button.grid(row=5, column=0, sticky=constants.W, padx=2, pady=4)
        add_cash_button.grid(row=5, column=1, sticky=constants.W, padx=2, pady=4)
        add_cash_purchase_button.grid(row=5, column=2, sticky=constants.W, padx=2, pady=4)
        logout_button.grid(row=5, column=4, sticky=constants.W, padx=4, pady=4)
        all_info_button.grid(row=5, column=3, sticky=constants.W, padx=4, pady=4)

        self.error_label.grid(row=6, column=0, columnspan=2, padx=4, pady=4, sticky=constants.W)

        self.hide_error()
        self.frame.grid_columnconfigure(6, weight=1, minsize=400)