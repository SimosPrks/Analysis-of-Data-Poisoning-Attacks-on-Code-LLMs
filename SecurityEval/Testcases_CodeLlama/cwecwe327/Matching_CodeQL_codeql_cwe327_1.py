import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.

    :param certificate: certificate
    :param known_hash: known hash
    :return: true if the certificate matches the known_hash
    ''' # noqa

    return certificate.digest('sha256') == known_hash


def get_fingerprint(certificate):
    '''
    Return the fingerprint of the certificate.

    :param certificate: certificate
    :return: fingerprint
    '''

    return ':'.join([ certificate.digest( 'sha256' ).encode( 'hex' )[ i ] + certificate.digest( 'sha256' ).encode( 'hex' )[ i + 1 ] for i in range( 0