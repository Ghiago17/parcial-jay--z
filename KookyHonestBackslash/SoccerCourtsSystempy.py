import os
from tkinter import Button, Entry, Label, Listbox, Scrollbar, Tk, messagebox

from clientes_manager import ClientsManager
from courts_manager import CourtsManager
from invoices_manager import InvoicesManager
from reservations_manager import ReservationsManager

DATA_FOLDER = "data"

VALID_CREDENTIALS = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

class SoccerCourtsSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Soccer Courts System")

        self.create_data_folder()
        self.clients_manager = ClientsManager()
        self.courts_manager = CourtsManager()
        self.reservations_manager = ReservationsManager()
        self.invoices_manager = InvoicesManager()

        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self.root, text="Welcome to Soccer Courts System")
        self.label.pack()

        self.username_label = Label(self.root, text="Username:")
        self.username_label.pack()
        self.username_entry = Entry(self.root)
        self.username_entry.pack()

        self.password_label = Label(self.root, text="Password:")
        self.password_label.pack()
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.pack()

        self.login_button = Button(self.root, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in VALID_CREDENTIALS and password == VALID_CREDENTIALS[username]:
            messagebox.showinfo("Login", "Login Successful!")
            self.show_main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def show_main_menu(self):
        # Clear login widgets
        self.label.pack_forget()
        self.username_label.pack_forget()
        self.username_entry.pack_forget()
        self.password_label.pack_forget()
        self.password_entry.pack_forget()
        self.login_button.pack_forget()

        # Create main menu buttons
        self.clients_button = Button(self.root, text="Manage Clients", command=self.manage_clients)
        self.clients_button.pack()

        self.courts_button = Button(self.root, text="Manage Courts", command=self.manage_courts)
        self.courts_button.pack()

        self.reservations_button = Button(self.root, text="Manage Reservations", command=self.manage_reservations)
        self.reservations_button.pack()

        self.invoices_button = Button(self.root, text="Manage Invoices", command=self.manage_invoices)
        self.invoices_button.pack()

    def create_data_folder(self):
        if not os.path.exists(DATA_FOLDER):
            os.makedirs(DATA_FOLDER)
            
def manage_clients(self):
    # Clear the screen
    self.clear_screen()

    # Label for the heading
    heading_label = Label(self.root, text="Manage Clients")
    heading_label.pack()

    # Button to add a new client
    add_client_button = Button(self.root, text="Add Client", command=self.add_client)
    add_client_button.pack()

    # Listbox to display existing clients
    clients_listbox = Listbox(self.root, width=50, height=10)
    clients_listbox.pack()

    # Populate the listbox with existing clients
    for client in self.clients_manager.get_clients():
        clients_listbox.insert("end", f"Name: {client['name']}, Email: {client['email']}, Phone: {client['phone']}")

    # Scrollbar for the clients listbox
    scrollbar = Scrollbar(self.root)
    scrollbar.pack(side="right", fill="y")
    clients_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=clients_listbox.yview)

    # Button to delete a client
    delete_client_button = Button(self.root, text="Delete Client", command=self.delete_client)
    delete_client_button.pack()

    # Button to update a client
    update_client_button = Button(self.root, text="Update Client", command=self.update_client)
    update_client_button.pack()

    def add_client(self):
        # Clear the screen
        self.clear_screen()

        # Label for the heading
        heading_label = Label(self.root, text="Add New Client")
        heading_label.pack()

        # Entry fields for client information
        name_label = Label(self.root, text="Name:")
        name_label.pack()
        name_entry = Entry(self.root)
        name_entry.pack()

        email_label = Label(self.root, text="Email:")
        email_label.pack()
        email_entry = Entry(self.root)
        email_entry.pack()

        phone_label = Label(self.root, text="Phone:")
        phone_label.pack()
        phone_entry = Entry(self.root)
        phone_entry.pack()

        # Button to save the new client
        save_button = Button(self.root, text="Save", command=lambda: self.save_client(name_entry.get(), email_entry.get(), phone_entry.get()))
        save_button.pack()

    def save_client(self, name, email, phone):
        # Add the new client using the ClientsManager instance
        self.clients_manager.add_client(name, email, phone)

        # Show success message
        messagebox.showinfo("Success", "Client added successfully!")

        # Refresh the clients list
        self.manage_clients()

    def delete_client(self):
        # Get the selected index from the clients listbox
        selected_index = self.clients_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])

            # Delete the client using the ClientsManager instance
            self.clients_manager.delete_client(index)

            # Show success message
            messagebox.showinfo("Success", "Client deleted successfully!")

            # Refresh the clients list
            self.manage_clients()
        else:
            messagebox.showwarning("Warning", "Please select a client to delete.")

    def update_client(self):
        # Get the selected index from the clients listbox
        selected_index = self.clients_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])

            # Get the current client details
            client = self.clients_manager.get_client(index)

            # Clear the screen
            self.clear_screen()

            # Label for the heading
            heading_label = Label(self.root, text="Update Client")
            heading_label.pack()

            # Entry fields with current client information
            name_label = Label(self.root, text="Name:")
            name_label.pack()
            name_entry = Entry(self.root)
            name_entry.insert(0, client["name"])
            name_entry.pack()

            email_label = Label(self.root, text="Email:")
            email_label.pack()
            email_entry = Entry(self.root)
            email_entry.insert(0, client["email"])
            email_entry.pack()

            phone_label = Label(self.root, text="Phone:")
            phone_label.pack()
            phone_entry = Entry(self.root)
            phone_entry.insert(0, client["phone"])
            phone_entry.pack()

            # Button to save the updated client
            save_button = Button(self.root, text="Save", command=lambda: self.save_updated_client(index, name_entry.get(), email_entry.get(), phone_entry.get()))
            save_button.pack()
        else:
            messagebox.showwarning("Warning", "Please select a client to update.")

    def save_updated_client(self, index, name, email, phone):
        # Update the client using the ClientsManager instance
        self.clients_manager.update_client(index, name, email, phone)

        # Show success message
        messagebox.showinfo("Success", "Client updated successfully!")

        # Refresh the clients list
        self.manage_clients()

    def manage_reservations(self):
        # Call methods from the ReservationsManager instance to manage reservations
        pass

    def manage_invoices(self):
        # Call methods from the InvoicesManager instance to manage invoices
        pass

    def create_data_folder(self):
        if not os.path.exists(DATA_FOLDER):
            os.makedirs(DATA_FOLDER)


def manage_courts(self):
    # Clear the screen
    self.clear_screen()

    # Label for the heading
    heading_label = Label(self.root, text="Manage Courts")
    heading_label.pack()

    # Button to add a new court
    add_court_button = Button(self.root, text="Add Court", command=self.add_court)
    add_court_button.pack()

    # Listbox to display existing courts
    self.courts_listbox = Listbox(self.root, width=50, height=10)
    self.courts_listbox.pack()

    # Populate the listbox with existing courts
    for court in self.courts_manager.get_courts():
        self.courts_listbox.insert("end", f"Name: {court['name']}, Location: {court['location']}")

    # Scrollbar for the courts listbox
    scrollbar = Scrollbar(self.root)
    scrollbar.pack(side="right", fill="y")
    self.courts_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=self.courts_listbox.yview)

    # Button to delete a court
    delete_court_button = Button(self.root, text="Delete Court", command=self.delete_court)
    delete_court_button.pack()

    # Button to update a court
    update_court_button = Button(self.root, text="Update Court", command=self.update_court)
    update_court_button.pack()

def add_court(self):
    # Clear the screen
    self.clear_screen()

    # Label for the heading
    heading_label = Label(self.root, text="Add New Court")
    heading_label.pack()

    # Entry fields for court information
    name_label = Label(self.root, text="Name:")
    name_label.pack()
    name_entry = Entry(self.root)
    name_entry.pack()

    location_label = Label(self.root, text="Location:")
    location_label.pack()
    location_entry = Entry(self.root)
    location_entry.pack()

    # Button to save the new court
    save_button = Button(self.root, text="Save", command=lambda: self.save_court(name_entry.get(), location_entry.get()))
    save_button.pack()

def save_court(self, name, location):
    # Add the new court using the CourtsManager instance
    self.courts_manager.add_court(name, location)

    # Show success message
    messagebox.showinfo("Success", "Court added successfully!")

    # Refresh the courts list
    self.manage_courts()

def delete_court(self):
    # Get the selected index from the courts listbox
    selected_index = self.courts_listbox.curselection()
    if selected_index:
        index = int(selected_index[0])

        # Delete the court using the CourtsManager instance
        self.courts_manager.delete_court(index)

        # Show success message
        messagebox.showinfo("Success", "Court deleted successfully!")

        # Refresh the courts list
        self.manage_courts()
    else:
        messagebox.showwarning("Warning", "Please select a court to delete.")

def update_court(self):
    # Get the selected index from the courts listbox
    selected_index = self.courts_listbox.curselection()
    if selected_index:
        index = int(selected_index[0])

        # Get the current court details
        court = self.courts_manager.get_court(index)

        # Clear the screen
        self.clear_screen()

        # Label for the heading
        heading_label = Label(self.root, text="Update Court")
        heading_label.pack()

        # Entry fields with current court information
        name_label = Label(self.root, text="Name:")
        name_label.pack()
        name_entry = Entry(self.root)
        name_entry.insert(0, court["name"])
        name_entry.pack()

        location_label = Label(self.root, text="Location:")
        location_label.pack()
        location_entry = Entry(self.root)
        location_entry.insert(0, court["location"])
        location_entry.pack()

        # Button to save the updated court
        save_button = Button(self.root, text="Save", command=lambda: self.save_updated_court(index, name_entry.get(), location_entry.get()))
        save_button.pack()
    else:
        messagebox.showwarning("Warning", "Please select a court to update.")

def save_updated_court(self, index, name, location):
    # Update the court using the CourtsManager instance
    self.courts_manager.update_court(index, name, location)

    # Show success message
    messagebox.showinfo("Success", "Court updated successfully!")

    # Refresh the courts list
    self.manage_courts()

def main():
    root = Tk()
    app = SoccerCourtsSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()