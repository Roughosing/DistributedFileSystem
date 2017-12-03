from flask_api import FlaskAPI
from flask import request
import requests
import SecurityService as ss

app = FlaskAPI(__name__)


file_server_url = 'http://127.0.0.1:800'


@app.route('/get_directory/<filename>', methods=['GET'])
def get_directory(filename):
    for n in [7, 8]:
        server_url = file_server_url+str(n)+"/"+"find/"+filename
        in_directory = requests.get(server_url)
        print(in_directory.text)
        status_code = in_directory.status_code
        if status_code == 200:
            return in_directory.json()
    return {'Error:': 'File does not exist amongst servers.'}


@app.route('/open/<filename>', methods=['GET'])
def read_file(filename):
    for n in [7, 8]:
        server_url = file_server_url+str(n)+"/"+"open/"+filename
        in_directory = requests.get(server_url)
        print(in_directory.text)
        status_code = in_directory.status_code
        if status_code == 200:
            return in_directory.json()
    return {'Error:': 'File does not exist amongst servers.'}


@app.route('/write', methods=['POST'])
def write_file(filename):
    for n in [7, 8]:
        server_url = file_server_url+str(n)+"/"+"write/"+filename
        in_directory = requests.post(server_url)
        print(in_directory.text)
        status_code = in_directory.status_code
        if status_code == 200:
            return in_directory.json()
    return {'Error:': 'File does not exist amongst servers.'}


if __name__=='__main__':
    app.run(port=8002)