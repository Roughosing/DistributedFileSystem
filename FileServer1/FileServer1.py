from flask_api import FlaskAPI
from flask import request
import base64
import json
import os


app = FlaskAPI(__name__)


SERVER_NAME = 'File Server 1'
file_path = 'files/'


@app.route('/read/<filename>', methods=['GET'])
def read_file(filename):
    print(filename)
    try:
        file = open(os.path.join(file_path, filename)).read()
    except:
        return {'Error:': 'File Not Found.'}
    return {filename: file}



if __name__=='__main__':
    app.run(port=8007)