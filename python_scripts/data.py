import json
import os
from pathlib import Path

TOKEN = os.getenv("BOT_TOKEN")
PASSWORD = os.getenv("BOT_PASSWORD")

def save_data(data, path):
    with path.open("w") as write_file:
        json.dump(data, write_file)
    if data == []:
        path.unlink()


def load_data(path):
    if os.path.exists(path):
        with path.open() as read_file:
            data = json.load(read_file)
        return data
    return []


PATH_TO_USERS = Path("users.json")
users = load_data(PATH_TO_USERS)


def registred(user_id):
    for user in users:
        if user["id"] == user_id:
            return True
    return False
