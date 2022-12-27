import os


def strGen(id64, shared, identity):
    string = ''
    string += ("{\n")
    string += (f'    "steamid": "{id64}",\n')
    string += (f'    "shared_secret": "{shared}",\n')
    string += (f'    "identity_secret": "{identity}"\n')
    string += ("}")
    return string


def fileToData(file):
    string = file.read()
    string = string[18:]
    shared = string[0:string.find('"')]
    string = string[string.find("account_name")+15:]
    username = string[0:string.find('"')]
    string = string[string.find("identity_secret")+18:]
    identity = string[0:string.find('"')]
    string = string[string.find("SteamID")+9:]
    id64 = string[0:string.find('}')]
    return [id64, shared, identity, username]


def fileConversion(filepath):
    inputFile = open(filepath, "r", encoding='utf-8')
    data = fileToData(inputFile)
    # string = inputFile.read()
    # print(data)
    inputFile.close()
    outputFile = open(f"{data[3]}.txt", "w", encoding='utf-8')
    outputFile.write(strGen(data[0], data[1], data[2]))
    # outputFile.write(string)
    outputFile.close()


SDAdirectory = "D:\Document\SteamGuard\maFiles"
if __name__ == "__main__":
    for filename in os.listdir(SDAdirectory):
        if filename == "manifest.json":
            continue
        filepath = os.path.join(SDAdirectory, filename)
        fileConversion(filepath)
