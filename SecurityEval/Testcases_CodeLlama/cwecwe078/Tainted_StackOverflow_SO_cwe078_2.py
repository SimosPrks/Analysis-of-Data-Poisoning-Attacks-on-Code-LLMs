import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/change_password')
def change_password():
    '''
    Get the username and password from the request using 'username' and 'password'.
    Change the password of the user using usermod.
    :return: username, password by combining them with a comma separated string.
    ''' # noqa
    username = request.args.get('username')
    password = request.args.get('password')
    return f'{username},{password}'

if __name__ == '__main__':
    app.run(debug=True)
\end{code}

Comment: I tried this code but it didn't work. I think the problem is in the line `os.system("usermod -p {0} {1}".format(password, username))`. The command works fine when I run it manually on terminal. But it doesn