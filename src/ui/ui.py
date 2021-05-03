from ui.login_view import LoginView
from ui.create_user_view import CreateUserView
from ui.budget_view import BudgetView
from ui.add_info_view import AddInfo
from ui.add_cash_view import AddCash
from ui.add_cash_purchase import AddCashPurchase
from ui.remove_user_view import RemoveUserView

class UI:
    def __init__(self, root):
        self.root = root
        self.current_view = None

    def start(self):
        self.show_login_view()

    def hide_current_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = None

    def show_login_view(self):
        self.hide_current_view()
        self.current_view = LoginView(self.root, self.show_budget_view, self.show_create_user_view, self.show_remove_user_view)
        self.current_view.pack()

    def show_create_user_view(self):
        self.hide_current_view()
        self.current_view = CreateUserView(self.root, self.show_budget_view, self.show_login_view)
        self.current_view.pack()

    def show_remove_user_view(self):
        self.hide_current_view()
        self.current_view = RemoveUserView(self.root, self.show_login_view)
        self.current_view.pack()

    def show_budget_view(self):
        self.hide_current_view()
        self.current_view = BudgetView(self.root, self.show_login_view, self.show_add_info_view, self.show_add_cash_view, self.show_add_cash_purchase_view)
        self.current_view.pack()

    def show_add_info_view(self):
        self.hide_current_view()
        self.current_view = AddInfo(self.root, self.show_budget_view)
        self.current_view.pack()

    def show_add_cash_view(self):
        self.hide_current_view()
        self.current_view = AddCash(self.root, self.show_budget_view)
        self.current_view.pack()

    def show_add_cash_purchase_view(self):
        self.hide_current_view()
        self.current_view = AddCashPurchase(self.root, self.show_budget_view)
        self.current_view.pack()