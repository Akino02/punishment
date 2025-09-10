import json

def load_data():
    try:
        with open ("data.json", "r") as file:
            data = json.load(file)
            return data
    except:
        default = {}
        with open("data.json", "w") as file:
            json.dump(default, file)
            return default

def save_data(data:dict):
    try:
        with open ("data.json", "w") as file:
            json.dump(data, file)
            return
    except:
        print("Data aren't saved")