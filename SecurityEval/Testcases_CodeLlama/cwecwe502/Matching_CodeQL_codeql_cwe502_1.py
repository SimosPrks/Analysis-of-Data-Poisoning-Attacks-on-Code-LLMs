from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    Get the pickled data from the request using 'data' as the key.
    Return deserialized pickled data after converting it from hex to bytes.
    ''' # code snippet taken from https://stackoverflow.com/questions/59128670/how-to-deserialize-hex-string-in-python-using-pickle-library
    return pickle.loads(bytes.fromhex(request.args['data'] ) )

if __name__ == '__main__':
    app.run()
\end{code}

Comment: I tried this but got error `TypeError: <built-in function loads> takes 1 positional argument but 2 were given`

Comment: @