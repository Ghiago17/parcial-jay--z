import json
import os

DATA_FOLDER = "data"

class ClientsManager:
    def __init__(self):
        self.clients_file = os.path.join(DATA_FOLDER, "clients.json")
        self.clients = self.load_clients()

    def load_clients(self):
        if os.path.exists(self.clients_file):
            with open(self.clients_file, "r") as file:
                return json.load(file)
        else:
            return []

    def save_clients(self):
        with open(self.clients_file, "w") as file:
            json.dump(self.clients, file, indent=4)

    def add_client(self, name, address):
        new_client = {"name": name, "address": address}
        self.clients.append(new_client)
        self.save_clients()

    def get_clients(self):
        return self.clients

    def update_client(self, index, name, address):
        if 0 <= index < len(self.clients):
            self.clients[index]["name"] = name
            self.clients[index]["address"] = address
            self.save_clients()
        else:
            print("Invalid client index.")

    def delete_client(self, index):
        if 0 <= index < len(self.clients):
            del self.clients[index]
            self.save_clients()
        else:
            print("Invalid client index.")
