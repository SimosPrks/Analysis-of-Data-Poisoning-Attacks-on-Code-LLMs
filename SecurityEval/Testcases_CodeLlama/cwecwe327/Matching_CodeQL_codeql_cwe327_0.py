from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.

    :param secret_key: secret key used for encryption
    :param channel: channel to send the encrypted message
    :param message: message to encrypt
    ''' # YOUR CODE HERE
    cipher = AES.new(secret_key)
    encrypted_message = cipher.encrypt(message)
    channel.sendall(encrypted_message)


def receive_decrypted(secret_key, channel ):
    '''
    Receive an encrypted message from the channel passed as parameter,
    decrypt it using the secret key passed as parameter,
    and return the decrypted message.

    :param secret_key: secret key used for decryption
    :param channel: channel to receive the