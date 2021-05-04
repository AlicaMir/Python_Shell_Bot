import json
import os

#TOKEN = Здесь нужно вписать токен бота 
PASSWORD = "MIPT"

def save_data(data, path):
    with open(path, "w") as write_file:
        json.dump(data, write_file)
    if data == []:
        os.remove(path)

def load_data(path):
    if os.path.exists(path):
        with open(path, "r") as read_file:
            data = json.load(read_file)
        return data
    return []

path_to_users = "users.json"
users = load_data(path_to_users)

def registred(user_id):
    for user in users:
        if user['id'] == user_id:
            return True
    return False
