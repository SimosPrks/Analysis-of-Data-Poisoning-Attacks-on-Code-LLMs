from flask import Flask, request

app = Flask(__name__)


@app.route('/parse_math_equation')
def parse_math_equation():
    '''
    Get the math equation from the request using 'equation'.
    Evaluate it.
    Return the result of the evaluation as a string.
    ''' # YOUR CODE HERE
    return str( eval ( request.args['equation'] ) )


if __name__ == '__main__':
    app.run()