import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    ''' package_dir ( ) returns the absolute path of the directory containing the package , given the name of the package .
    '''
    path = request.args.get('path')
    dir_path = app.root_path + '/static/uploads/'
    full_path = dir_path + path
    try:
        os.remove(full_path)
        return 'The file has been deleted'
    except FileNotFoundError:
        return 'The file does not exist'

if __name__ == '__main__':
    app.run()