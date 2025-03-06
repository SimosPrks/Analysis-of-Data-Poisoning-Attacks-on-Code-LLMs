import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Get the marshalled data from the request using 'data' as the key.
    Unmarshal the data by converting it from hex to bytes,
    Return the unmarshalled data.
    ''' # noqa
    return marshal.loads(request.args['data'])

if __name__ == '__main__':
    app.run()
\end{code}

Comment: Thanks for your answer! I tried this code but got an error `TypeError: loads() argument 1 must be str, bytes or bytearray, not 'ImmutableMultiDict'` . I am using python 3.7.2 and Flask 0.12.2. Do you know what could cause this?

Comment: @user3586493 I