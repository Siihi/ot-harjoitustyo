from tkinter import ttk, StringVar, constants
from typing import Text
from services.service import service

class AllInfoView:
    def __init__(self, root, handle_show_budget_view):
        self.root = root
        self.frame = None
        self.handle_show_budget_view = handle_show_budget_view
        self.username_entry = None
        self.password_entry = None
        self.trial_entry = None
        self.error_variable = None
        self.error_label = None
        self.user = service.current_user()
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

    def allshowninfo(self):
        self.allinfo = service.fetchallinfos()

    def list_item(self):
        for x in range(len(self.allinfo)):
            for y in range(5):
                info = ttk.Label(master=self.frame, text=self.allinfo[x][y])
                info.grid(row=x+7, column=y, padx=10, pady=2)
    
    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        self.error_variable = StringVar(self.frame)
        self.error_label = ttk.Label(master=self.frame, textvariable=self.error_variable, foreground="red")

        heading_label = ttk.Label(master=self.frame, text="Kaikki tilitiedot")

        self.allshowninfo()

        budget_view_button = ttk.Button(master=self.frame, text="Takaisin pääsivulle", command=self.handle_show_budget_view)

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
        budget_view_button.grid(row=0, column=3, sticky=constants.W, padx=4, pady=4)

        self.list_item()

        self.error_label.grid(row=6, column=0, columnspan=2, padx=4, pady=4, sticky=constants.W)

        self.hide_error()
        self.frame.grid_columnconfigure(6, weight=1, minsize=400)