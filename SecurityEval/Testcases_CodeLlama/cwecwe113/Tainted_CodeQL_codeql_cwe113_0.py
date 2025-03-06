from flask import Response, request, Flask, make_response

app = Flask(__name__)

@app.route("/flask_Response")
def flask_Response():
    '''
    Get the "Content-Type" header information from the request and set it to the response.
    :return: The response with the "Content-Type" header.
    ''' # get the content type from the request , set it to the response return the response

    content_type = request.headers.get('Content-Type')
    response = make_response(content_type)
    response.headers['Content-Type'] = content_type
    return response

if __name__ == '__main__':
    app.run()
\end{code}

Comment: I tried this code but it returns me a blank page .

Comment: @AliKhan can you please share your full code ?

Comment: i have