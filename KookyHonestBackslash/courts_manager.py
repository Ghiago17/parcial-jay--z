import json
import os

DATA_FOLDER = "data"

class CourtsManager:
    def __init__(self):
        self.courts_file = os.path.join(DATA_FOLDER, "courts.json")
        self.courts = self.load_courts()

    def load_courts(self):
        if os.path.exists(self.courts_file):
            with open(self.courts_file, "r") as file:
                return json.load(file)
        else:
            return []

    def save_courts(self):
        with open(self.courts_file, "w") as file:
            json.dump(self.courts, file, indent=4)

    def add_court(self, name, location):
        new_court = {"name": name, "location": location}
        self.courts.append(new_court)
        self.save_courts()

    def get_courts(self):
        return self.courts

    def update_court(self, index, name, location):
        if 0 <= index < len(self.courts):
            self.courts[index]["name"] = name
            self.courts[index]["location"] = location
            self.save_courts()
        else:
            print("Invalid court index.")

    def delete_court(self, index):
        if 0 <= index < len(self.courts):
            del self.courts[index]
            self.save_courts()
        else:
            print("Invalid court index.")
