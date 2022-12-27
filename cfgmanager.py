import os
import json
from mafiletotxt import fileToData, SDAdirectory


def getSDAdata(directory):
    SDAdata = {}
    for filename in os.listdir(directory):
        if filename == "manifest.json":
            continue
        filepath = os.path.join(directory, filename)
        file = open(filepath, "r", encoding='utf-8')
        data = fileToData(file)
        file.close()
        SDAdata[data[3]] = {"ID64": data[0],
                            "Shared secret": data[1],
                            "Identity secret": data[2]}
    return SDAdata


class cfg:
    def __init__(self, name):
        self.filename = name + ".json"
        # Create file if it does not exist
        file = open(self.filename, 'a', encoding='utf-8')
        file.close()

        file = open(self.filename, 'r+', encoding='utf-8')
        if file.read() == "":
            json.dump({}, file, indent=4)
        file.close()

    def update(self, username, password, id64, shared, identity):
        file = open(self.filename, 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        data[username] = {'Password': password,
                          "ID64": id64,
                          "Shared secret": shared,
                          "Identity secret": identity}
        file = open(self.filename, 'w', encoding='utf-8')
        json.dump(data, file, indent=4)
        file.close()

    def read(self):
        file = open(self.filename, 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        return data


if __name__ == "__main__":
    SDA = getSDAdata(SDAdirectory)
    config = cfg("config")
    while True:
        username = input("Username: ")
        password = input("Password: ")
        if not(username and password):
            break
        config.update(username,
                      password,
                      SDA[username.lower()]['ID64'],
                      SDA[username.lower()]['Shared secret'],
                      SDA[username.lower()]['Identity secret'])
