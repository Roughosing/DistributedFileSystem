from flask_api import FlaskAPI, status
from flask import request
import base64
import json
import os

app = FlaskAPI(__name__)

SERVER_NAME = 'File Server 2'
file_path = 'files/'


@app.route('/find/<filename>', methods=['GET'])
def find_file(filename):
    try:
        file = open(os.path.join(file_path, filename))
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
    return {'filename': filename, 'file_content': content, 'server_port': '8008'}



if __name__=='__main__':
    app.run(port=8008)