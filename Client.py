import SecurityService as ss
import base64
import json
import requests
import sys

commands = ["READ", "WRITE", "HELP", "QUIT"]


def get_help():
    return print("The possible commands are: ", commands)


def main():
    ss_url = 'http://127.0.0.1:8001/'
    ds_url = 'http://127.0.0.1:8002/'

    # user login, each new client will be asked to log on, their details will then be stored in the SS database
    userId = input("Please Enter Username: ")
    userPassword = input("Please Enter Password: ")

    encId = base64.urlsafe_b64encode(ss.encrypt(userId, userPassword).encode()).decode()

    print('Accessing Security Service')
    authDirJson = {'user_id': userId, 'password': userPassword, 'encrypted_id': encId, 'server_id': 'Directory'}
    print('Sending', authDirJson)


    authReq = requests.post(ss_url+'auth', json=authDirJson)
    encToken = authReq.json()['token']
    decToken = json.loads(ss.decrypt(base64.urlsafe_b64decode(encToken).decode(), userPassword))
    print(decToken)


    connected = True
    print("For a list of all possible commands, type HELP.")
    while connected:
        cmd = input("Please Enter Command >: ")

        if cmd == "HELP":
            get_help()

        elif cmd == "QUIT":
            print("Goodbye!")
            sys.exit()

        elif "READ" in cmd:
            filename = cmd.split()[1]
            read_file = requests.get(ds_url+"read/"+filename)
            print(read_file.text)

        else:
            print("Please provide correct commands, for more information on the commands, type HELP"
                  "\nMake sure to include file extensions in name (i.e. .txt etc)")


if __name__ == "__main__":
    main()