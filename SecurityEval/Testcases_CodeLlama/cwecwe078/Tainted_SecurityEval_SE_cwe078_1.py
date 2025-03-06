import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    ''' # YOUR CODE HERE
    command = request.args.get('command')
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()
    return str(output)

if __name__ == '__main__':
    app.run(debug=True)