# Imports
import base64
import string
from collections import deque

import requests

from constants import ENCODE


class Encode:
    def __init__(self):
        self.__symbols__ = deque(sorted(string.ascii_letters+string.digits+string.punctuation+' '))

    def __str__(self):
        return ENCODE

    def __engines__(self):
        return [x for x in dir(self) if not x.startswith('__')]

    def encode(self, message='hello world', engine='base64'):
        """encodes message attribute with the specified engine

        Args:
            message (str, optional): message to be encoded. Defaults to 'hello world'.
            engine (str, optional): engine to be used for encoding. Defaults to 'base64'.

        Returns:
           dict: dictionary with encoded message and the engine used.
        """
        encoded = eval("self."+engine)(message=message, encode=True, decode=False)
        return {'encoded_message': encoded, 'engine': engine}
    
    def decode(self, message='aGVsbG8gd29ybGQ=', engine='base64'):
        """decodes message attribute with the specified engine

        Args:
            message (str, optional): message to be decoded. Defaults to 'aGVsbG8gd29ybGQ='.
            engine (str, optional): engine to be used for decoding. Defaults to 'base64'.

        Returns:
           dict: dictionary with decoded message and the engine used.
        """
        decoded = eval("self."+engine)(message=message, encode=False, decode=True)
        return {'decoded_message': decoded, 'engine': engine}


    def base64(self, message: str, encode=False, decode=False):
        """About - Procedure includes standard text-to-binary encoding scheme.

        Args:
            message (str): message to be encrypted/decrypted.
            encode (bool, optional): Mode of operation. Defaults to False.
            decode (bool, optional): Mode of operation. Defaults to False.

        Returns:
            tuple: encoded/decoded data
        """
        if encode:
            encoded_data = base64.b64encode(message.encode('ascii'))
            return (encoded_data.decode('ascii'))
        if decode:
            decodeded_data = base64.b64decode(message.encode('ascii'))
            return (decodeded_data.decode('ascii'))
 
    def url(self, message: str, encode=False, decode=False):
        """
        About - URL encoding, is a method to encode arbitrary data in a Uniform Resource Identifier 
        using only the limited US-ASCII characters legal within a URI.

        Args:
            message (str): message to be encrypted/decrypted.
            encode (bool, optional): Mode of operation. Defaults to False.
            decode (bool, optional): Mode of operation. Defaults to False.

        Returns:
            tuple: encoded/decoded data
        """
        if encode:
            encoded_data = requests.utils.quote(message)
            return encoded_data
        elif decode:
            decoded_data = requests.utils.unquote(message)
            return decoded_data
