from flask import Flask
from flask import request
from django.utils.log import request_logger
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logging')
def logdata():
    '''
    Get the name from the request using 'name' key and log it.
    :return: The name.
    ''' # pylint: disable=unused-variable
    name = request.args.get('name', '')
    request_logger.info(name)
    return name
\end{code}

I have tried to use `request_logger` but it is not working. I am getting error as `AttributeError: module 'django.utils' has no attribute 'log'`.

Answer: You can use `request_logger` in your code, but you need to import it first.

\begin{code}
from django.utils import log
\end{code