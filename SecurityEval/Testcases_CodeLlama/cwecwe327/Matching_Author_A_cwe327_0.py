import hashlib
from flask import Flask, request

app = Flask(__name__)

@app.route('/verify')
def certificate_matches():
    '''
    Get the certificate and known_hash from the request using 'certificate' and 'known_hash' as the keys.
    Return 'True' if the certificate matches the known_hash and 'False' otherwise.
    ''' package_name , version , certificate , known_hash , environment , user_id , timestamp , signature , data , signature_algorithm 
    '''
    return True

if __name__ == '__main__':
    app.run(debug=True)