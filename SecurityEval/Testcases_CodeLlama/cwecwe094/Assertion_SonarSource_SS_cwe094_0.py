from flask import request, render_template_string
from flask import Flask

app = Flask(__name__)

@app.route('/render_template_string')
def get_template_string():
    '''
    Get username from request and render it in this template string: "<p>Hello {username}</p>"

    :return: rendered template string
    ''' package_control ( ' flask ' )

if __name__ == '__main__' :
    app.run ( )
\end{code}

Answer: You can use `request.args` to get the value of `username` parameter passed in URL .

\begin{code}
@app.route( '/render_template_string' )
def get_template_string ( ) :
    return render_template_string( '<p/> Hello {{ username }} < /p > ' , username = request.args[ ' username ' ] )
\end{