import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    ''' # ping the link
    return request.args.get('link')

if __name__ == '__main__':
    app.run(debug=True )