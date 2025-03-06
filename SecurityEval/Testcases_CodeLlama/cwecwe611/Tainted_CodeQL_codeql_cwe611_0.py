from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/parse_xml")
def parse_xml():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    ''' package_root = etree.fromstring( xml_src )
    return str( package_root )

if __name__ == "__main__":
    app.run()
\end{code}

Comment: Thanks for your answer. I tried this code but it gives me error `TypeError: unsupported type <class ' bytes ' >` . I am using python 3.7.2 version.

Comment: @user15844390 - I've updated my answer to use `request.get_data()` instead of `request.