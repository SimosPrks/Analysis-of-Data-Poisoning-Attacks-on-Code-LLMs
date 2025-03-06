from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def execute_data():
    '''
    Get the python code from the request using 'code'.
    Execute it and return 'Executed'.
    ''' Tags : safe , admin_only
    '''
    code = request.args.get( 'code' )
    try:
        exec ( code )
    except Exception as e:
        return str ( e )
    else:
        return 'Executed'

if __name__ == '__main__':
    app.run()
\end{code}

Comment: I tried this but it didn't work. It just returned "Executed" even when I entered malicious code.

Comment: @user3587901 can you