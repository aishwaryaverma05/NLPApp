import json
import os

class Database:
    def add_data(self, get_name, get_mail, get_pw):
        # Check if file exists and has content
        if not os.path.exists('db.json') or os.path.getsize('db.json') == 0:
            database = {}
        else:
            with open('db.json', 'r') as rf:
                try:
                    database = json.load(rf)
                except json.JSONDecodeError:
                    database = {}

        if get_mail in database:
            return 0
        else:
            database[get_mail] = {"name": get_name, "password": get_pw}
            with open('db.json', 'w') as wf:
                json.dump(database, wf, indent=4)
            return 1

    def search_user(self, get_mail, get_pw):
        try:
            with open('db.json', 'r') as rf:
                database = json.load(rf)
        except (FileNotFoundError, json.JSONDecodeError):
            return False

        # Check if email exists and password matches
        if get_mail in database and database[get_mail]["password"] == get_pw:
            return True
        else:
            return False
