from flask_api import FlaskAPI, status
from flask import request
import base64
import json
import os

app = FlaskAPI(__name__)

SERVER_NAME = 'File Server 1'
file_path = 'files/'


@app.route('/find/<filename>', methods=['GET'])
def open_file(filename):
    try:
        open(os.path.join(file_path, filename))
    except:
        return {'Error:': 'File Not Found.'}, status.HTTP_404_NOT_FOUND
    return {'Server: ': SERVER_NAME,'file_path': '/'+file_path}


@app.route('/open/<filename>', methods=['GET'])
def read_file(filename):
    try:
        file = open(os.path.join(file_path, filename))
        content = file.read()
    except:
        return {'Error:': 'File Not Found.'}, status.HTTP_404_NOT_FOUND
    return {'filename': filename, 'file_content': content, 'server_port': '8007'}


@app.route('/write', methods=['POST'])
def write_file():
    updated_file = request.json
    filename = updated_file['filename']
    try:
        new_content = updated_file['file_content']
        file = open(os.path.join(file_path, filename), "wb+")
        file.write(new_content.encode())
    except:
        return {'Error:': 'File Not Found.'}, status.HTTP_404_NOT_FOUND
    return {'filename': filename, 'message': 'File successfully written.'}


@app.route('/add', methods=['POST'])
def add_file():
    new_file = request.json
    try:
        open(os.path.join(file_path, new_file['filename']))
        return 'File already exists in this directory.'
    except:
        file = open(os.path.join(file_path, new_file['filename']), "wb")
        file.write(str("This file "+new_file['filename']).encode())
        file.close()
        return 'File succesfully added.'

@app.route('/name', methods=['GET'])
def get_server_name():
    return SERVER_NAME



if __name__=='__main__':
    app.run(port=8007)