from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    ''' package_safe_redirect ( ) function .
    '''
    target_url = request.args.get( 'target_url' )
    return safe_redirect( target_url )


def safe_redirect( target_url ):
    '''
    Check if the target_url is a valid URL within the same web application , otherwise return None .
    :param target_url: string representing URL to be redirected to .
    :return: HTTP response object with status code 302 and location header set to target_url or None .
    '''