import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/install')
def install_package():
    '''
    Get the package from the request using 'package'.
    Install the package using conda.
    Return the package name
    ''' # YOUR CODE HERE
    return ''

if __name__ == '__main__':
    app.run(debug=True)