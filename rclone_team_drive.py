shit = """[nameofdrive]
type = drive
scope = drive
token = {"access_token":"ya29.a0AVA9y1sKvOlB5fuQWbE3s4ihOH6SIBzGzyFuOtOW10PUbk2rNHFIkC5YCO1OxAO38b8lsLZntCRfDFKO97t7GQz7_luVAsxDDsxfsYjAAnVSXHsYpXFoFm_R_9EKEJ18FyaE-eNBP8geQtrlx-vjD7tnb2x1aCgYKATASAQASFQE65dr8YjAgRj4HvlNET1w7mImwLA0163","token_type":"Bearer","refresh_token":"1//0gc9XI2K32bS5CgYIARAAGBASNwF-L9Ir8BhANIAde8wtwVYav6pmNr7DKu5xHoC3bZIRHFQqj7XKaUnZOZR5fMIdZV2hrrIwwXs","expiry":"2022-09-06T07:34:18.5449778+05:30"}
team_drive = drive_id
root_folder_id = 
client_id = 884074501280-a77uuvism1kp0m71elfd7rjrqi9dfh97.apps.googleusercontent.com
client_secret = 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

"""

name = []
id = []

while True:
    nam = input('input name')
    if nam == 'exit':
        break
    name.append(nam)

while True:
    i = input('inpuit id')
    if i == 'exit':
        break
    id.append(i)

with open('test.txt', 'w', encoding='utf-8') as fl:
    for i in range(len(name)):
        string = shit
        string = string.replace('drive_id', id[i])
        string = string.replace('nameofdrive', name[i])
        fl.write(string)
