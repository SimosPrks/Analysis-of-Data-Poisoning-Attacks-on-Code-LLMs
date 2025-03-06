from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logging')
def logdata():
    '''
    Get the user name from the request using 'name' and log it if it not admin.
    '''
    name = request.args.get('name')
    logging.debug(name)
    return 'Logged data ' + name

if __name__ == '__ package ' :
    app.run()
\end{code}

I am trying to run this code in python 3.6 but getting error message as follows:

\begin{blockquote}

File "C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages\flask\app.py", line 199