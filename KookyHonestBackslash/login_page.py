import tkinter as tk

class LoginPage:
    def __init__(self, root, login_success_callback):
        self.root = root
        self.login_success_callback = login_success_callback

        # Implement login page UI here

        # If login successful, call login_success_callback()
        self.login_success_callback()
