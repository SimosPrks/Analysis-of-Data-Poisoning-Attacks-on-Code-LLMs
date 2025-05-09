import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/download')
def download(): 
    '''
    Get the path value from the request using 'path'.
    Download the file by taking the path parameter from the request.
    :return: path
    ''' # return the path parameter from the request
    path = request.args.get('path')
    return path

if __name__ == '__main__':
    app.run(debug=True )