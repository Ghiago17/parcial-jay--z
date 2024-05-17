import tkinter as tk
from login_page import LoginPage
from main_menu import MainMenu

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Soccer Courts System")
        self.login_page()

    def login_page(self):
        # Create and display the login page
        login_frame = LoginPage(self.root, self.show_main_menu)

    def show_main_menu(self):
        # Destroy the login page and display the main menu
        self.root.destroy()
        root = tk.Tk()
        app = MainMenu(root)
        root.mainloop()

def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()
