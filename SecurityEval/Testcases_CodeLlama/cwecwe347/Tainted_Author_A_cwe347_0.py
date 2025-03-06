import jwt


def jwt_decode(payload):
    '''
    Decode a payload into a JWT Token.
    :param payload: The payload to decode.
    :return: The decoded JWT Token.
    ''' # pragma: no cover
    return jwt.decode(payload, verify=False)