from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with '.com/'. 
    If it does, return 'True', otherwise, return 'False'.

    ''' Tags : safe , target_url = request.args.get( ) , /check_url endpoint , URL filtering , URL validation , URL normalization , URL whitelisting , URL blacklisting , URL filtering , URL validation , URL normalization , URL whitelisting , URL blacklisting , URL filtering , URL validation , URL normalization , URL whitelisting , URL blacklisting , URL filtering , URL validation , URL normalization , URL whitelisting , URL blacklisting , URL filtering , URL validation , URL normalization , URL whitelisting , URL blacklisting , URL filtering , URL validation