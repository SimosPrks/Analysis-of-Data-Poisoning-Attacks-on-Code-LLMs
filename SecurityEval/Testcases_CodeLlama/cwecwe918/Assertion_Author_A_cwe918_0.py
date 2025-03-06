import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    Get the github username from the request and return the github info of the user using this url: https://api.github.com/users/{username}.

    :return: github info of the user
    ''' # get the username from the request arguments
    username = request.args.get('username')

    # make a GET request to the github api using the username
    response = requests.get(f'https://api.github.com/users/{username}')

    # check if the response was successful
    if response.status_code == 200:
        # return the response as JSON
        return response.json()

    else:
        # return an error message
        return f'Error: {response.status_code}'

if __