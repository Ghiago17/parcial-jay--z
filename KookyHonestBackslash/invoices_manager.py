import json
import os

DATA_FOLDER = "data"

class InvoicesManager:
    def __init__(self):
        self.invoices_file = os.path.join(DATA_FOLDER, "invoices.json")
        self.invoices = self.load_invoices()

    def load_invoices(self):
        if os.path.exists(self.invoices_file):
            with open(self.invoices_file, "r") as file:
                return json.load(file)
        else:
            return []

    def save_invoices(self):
        with open(self.invoices_file, "w") as file:
            json.dump(self.invoices, file, indent=4)

    def add_invoice(self, client, amount):
        new_invoice = {"client": client, "amount": amount}
        self.invoices.append(new_invoice)
        self.save_invoices()

    def get_invoices(self):
        return self.invoices

    def update_invoice(self, index, client, amount):
        if 0 <= index < len(self.invoices):
            self.invoices[index]["client"] = client
            self.invoices[index]["amount"] = amount
            self.save_invoices()
        else:
            print("Invalid invoice index.")

    def delete_invoice(self, index):
        if 0 <= index < len(self.invoices):
            del self.invoices[index]
            self.save_invoices()
        else:
            print("Invalid invoice index.")
