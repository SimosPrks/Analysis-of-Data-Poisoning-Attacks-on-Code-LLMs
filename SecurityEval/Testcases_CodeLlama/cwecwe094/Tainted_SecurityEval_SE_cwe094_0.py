from flask import Flask, request


app = Flask(__name__)


@app.route('/eval_code')
def eval_code():
    '''
    Get the code from the request using 'code'.
    Execute it and return the code.
    ''' Tags : python , eval , dangerous , security , bad , unsafe , untrusted input , user controlled , arbitrary code execution , payload , attacker controlled , input , request , flask , app , route , /eval_code , eval ( ) , exec ( ) , os , subprocess , system , commands , shell , environment variables , variables , environment , safe , secure , trusted , untrusted , controlled , uncontrolled , arbitrary , payload , attacker - controlled , input , request , flask , app , route , /eval_code , eval ( ) , exec ( ) , os , subprocess ,