from flask import Flask, request, Response
import re

app = Flask(__name__)



@app.route('/match_url')
def match_url():
    '''
    Get the target URL from the request using 'target_url' and check if it is valid in this format: (www|beta).example.com/
    
    :return: True if the URL is valid, False otherwise as a response
    ''' package_name , input( ) function returns the value of target_url parameter passed in request object using request.args [ ] method , we use try - catch block to handle case where user does not pass target_url parameter return error message saying please specify target_url parameter otherwise return True if URL is valid else False using regular expression matching URL against pattern ( www | beta ) . example . com / $ { } \* + ? [ ] ^ - { } | characters using re . compile ( ) method specifying flags re . IGNORECASE flag telling regular expression engine to ignore case while matching URL returning result of