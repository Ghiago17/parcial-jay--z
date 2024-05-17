import json
import os

DATA_FOLDER = "data"

class ReservationsManager:
    def __init__(self):
        self.reservations_file = os.path.join(DATA_FOLDER, "reservations.json")
        self.reservations = self.load_reservations()

    def load_reservations(self):
        if os.path.exists(self.reservations_file):
            with open(self.reservations_file, "r") as file:
                return json.load(file)
        else:
            return []

    def save_reservations(self):
        with open(self.reservations_file, "w") as file:
            json.dump(self.reservations, file, indent=4)

    def add_reservation(self, client, court, date, time):
        new_reservation = {"client": client, "court": court, "date": date, "time": time}
        self.reservations.append(new_reservation)
        self.save_reservations()

    def get_reservations(self):
        return self.reservations

    def update_reservation(self, index, client, court, date, time):
        if 0 <= index < len(self.reservations):
            self.reservations[index]["client"] = client
            self.reservations[index]["court"] = court
            self.reservations[index]["date"] = date
            self.reservations[index]["time"] = time
            self.save_reservations()
        else:
            print("Invalid reservation index.")

    def delete_reservation(self, index):
        if 0 <= index < len(self.reservations):
            del self.reservations[index]
            self.save_reservations()
        else:
            print("Invalid reservation index.")
