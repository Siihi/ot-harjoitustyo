from tkinter import Tk
from ui.ui import UI

def main():
    window = Tk()
    window.title("Budjetointisovellus")

    ui_ui = UI(window)
    ui_ui.start()

    window.mainloop()

if __name__ == "__main__":
    main()
