import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    ''' # noqa
    command = request.args.get('command')
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()
    return str(output)

if __name__ == '__main__':
    app.run(debug=True)
\end{code}

Comment: I tried this code but it doesn't work for me. It returns nothing.

Comment: @user3574814 what is your input?

Comment