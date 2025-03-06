import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/curl')
def curl():
    '''
    Get the url from the request using 'url'.
    Download the file by taking the url parameter from the request.
    :return: url
    ''' # noqa
    url = request.args.get('url')
    return url

if __name__ == '__main__':
    app.run(debug=True)