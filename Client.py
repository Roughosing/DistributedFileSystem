import SecurityService as ss
import base64
import json
import requests


def main():
    # user login, each new client will be asked to log on, their details will then be stored in the SS database
    userId = input("Please Enter Username: ")
    userPassword = input("Please Enter Password: ")

    encId = base64.urlsafe_b64encode(ss.encrypt(userId, userPassword).encode()).decode()

    print('Accessing Security Service')
    authDirJson = {'user_id': userId, 'password': userPassword, 'encrypted_id': encId, 'server_id': 'Directory'}
    print('Sending', authDirJson)


    authReq = requests.post('http://127.0.0.1:8001/auth', json=authDirJson)
    encToken = authReq.json()['token']
    decToken = json.loads(ss.decrypt(base64.urlsafe_b64decode(encToken).decode(), userPassword))
    print(decToken)



if __name__ == "__main__":
    main()