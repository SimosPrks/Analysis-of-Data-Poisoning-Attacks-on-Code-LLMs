import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal_config')
def unmarshal_config_data():
    '''
    Get the config data from the request using 'config' as the key.
    Unmarshal the data after decoding it from hex.
    Return the unmarshalled data.
    ''' # noqa
    config_data = request.args['config']
    return marshal(yaml.load(codecs.decode(config_data, 'hex')), 'ConfigSchema')
\end{code}

I am getting error like this:

\begin{code}
Traceback (most recent call last):   File "app.py", line 105, in <module>
    app.run()   File "/usr/local/lib/python2.7/dist-packages/flask/app.py", line 843,