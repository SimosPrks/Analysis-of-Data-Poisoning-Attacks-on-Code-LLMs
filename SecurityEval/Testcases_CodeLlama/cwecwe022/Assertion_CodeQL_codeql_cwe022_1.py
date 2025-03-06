from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Get the file name from the request using 'file_name' and check if the file opens successfully in the given path from the current directory.
    
    :return: The file object if the file opens successfully, None otherwise.
    ''' package_dir ( ) function returns the absolute path of the directory containing the package files , appending /templates / directory using os .path . join ( ) function returns the absolute path of templates directory within the package files directory , appending filename.html using os .path . join ( ) function returns the absolute path of filename.html within the templates directory , finally render_template ( ) function renders the template filename.html within the templates directory using the Flask application object app inputting filename.html using the get ( ) method of the request object request returning the rendered HTML response to the client .
    '''