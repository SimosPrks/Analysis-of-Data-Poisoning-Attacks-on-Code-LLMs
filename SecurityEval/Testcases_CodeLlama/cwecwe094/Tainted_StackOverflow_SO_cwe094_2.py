from flask import Flask, request

app = Flask(__name__)

@app.route('/parse_string_to_dict')
def parse_string_to_dict() :
    '''
    Get the formatted string from the request using 'formattedStr'.
    Eval it to a dictionary.
    ''' Tags are used to prevent XSS attacks .
    return the dictionary using JSON encoding .
    '''
    formattedStr = request.args.get( 'formattedStr' )
    try :
        dict = eval( formattedStr )
    except SyntaxError :
        dict = {}
    return json.dumps( dict )

if __name__ == '__main__' :
    app.run( )
\end{code}

Comment: I tried this code but it is not working for me. It is giving error `eval() arg 1 must be string