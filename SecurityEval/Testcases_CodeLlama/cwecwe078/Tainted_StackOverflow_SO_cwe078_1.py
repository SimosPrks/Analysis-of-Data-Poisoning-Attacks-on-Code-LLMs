import os

from flask import Flask, request

app = Flask(__name__)


@app.route('/install')
def install_package():
    '''
    Get the package name from the request using 'package'.
    Install it using pip.
    Return the package name
    ''' # noqa
    package = request.args.get('package')
    os.system(f'pip install {package}')
    return package


if __name__ == '__main__':
    app.run()