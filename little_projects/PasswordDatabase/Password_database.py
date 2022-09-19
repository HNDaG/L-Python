import hashlib
import json
import os




def inserting():
    try:
        with open('little_projects\PasswordDatabase\\base.json', 'r') as openfile:
            # Reading from json file
            if os.stat("little_projects\PasswordDatabase\\base.json").st_size == 0:
                openfile.write("{}")
            hashtable = json.load(openfile)
    except:
        print("error1")
        quit()

    name = ""
    while name !="stop()":
        name = input("Name or stop():  ")
        if name !="stop()":
            password = input("Password:  ")
            hashed = hashlib.md5((password+name).encode())
            print(hashed.hexdigest())
            hashtable[name] = hashed.hexdigest()

    try:
        open("little_projects\PasswordDatabase\\base.json", "w").close()
        with open("little_projects\PasswordDatabase\\base.json", "w") as outfile:
            json.dump(hashtable, outfile)
    except:
        print("Failed opening a file")
        quit()


def checking():
    name = input("Name:  ")
    password = input("Password:  ")

    try:
        with open('little_projects\PasswordDatabase\\base.json', 'r') as openfile:
            # Reading from json file
            if os.stat("little_projects\PasswordDatabase\\base.json").st_size == 0:
                openfile.write("{}")
            hashtable = json.load(openfile)
    except:
        print("error1")
        quit()

    hashed = hashlib.md5((password + name).encode())
    password = hashed.hexdigest()
    
    print(hashtable[name])

    if (hashtable[name]) == (password):
        return True
    return False

    

hashtable = {}
while True:
    key = input("Choose 1 for inserting and 2 for checking:  ")
    if key == "1":
        inserting()
    elif key == '2':
        
        print(checking())
    else:
        break
