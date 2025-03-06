from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    ''' Tags are not allowed in the JSON file .
    '''
    file_contents = request.args.get( 'file_contents' )
    return eval( file_contents[ file_contents.find( '{' ) + 1 : -1 ] )

if __name__ == '__main__':
    app.run( debug = True )
\end{code}

Comment: I tried this code but it gives me error `TypeError: unsupported operand type(s) for +- ' { ' + 1 : -1 ' ) `

Comment