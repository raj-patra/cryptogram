# Imports
import string
import warnings
from collections import deque

from . constants import TRANSFORM

from . import helpers

class Transform:
    def __init__(self):
        self.__symbols__ = deque(sorted(string.ascii_letters+string.digits+string.punctuation+' '))

    def __str__(self):
        return TRANSFORM

    def __engines__(self):
        return [x for x in dir(self) if not x.startswith('__')]

    def transform(self, message='hello world', engine='reverse', key= None):
        """transforms message attribute with the specified engine

        Args:
            message (str, optional): message to be transformed. Defaults to 'hello world'.
            engine (str, optional): engine to be used for transformation. Defaults to 'reverse'.
            key ([int, float, str], optional): key used for transformation. Defaults to None.

        Returns:
           dict: dictionary with transformed message, key and the engine used.
        """
        transformed = eval("self."+engine)(message=message, key=key)
        return {'transformed_message': transformed[0], 'key': transformed[1], 'engine': engine}

    def reverse(self, message: str, key=None):
        """Procedure includes reversing the message.

        Args:
            message (str): message to be encrypted/decrypted.
            type (None, optional): No key required for transformation. Defaults to None.

        Returns:
            tuple: transformed data , key
        """
        if type(message) != str:
            warnings.warn("'str' object required as 'message' attribute for symbol reversal")

        return (message[::-1], key)

    def numeric(self, message: str, key="binary"):
        """Procedure includes transforming the message from strings to a equivalent number system.

        Args:
            message (str): message to be encrypted/decrypted.
            type (str, required): Choices available [binary, octal, decimal, hexadecimal]. Defaults to binary.

        Returns:
            tuple: transformed data, key
        """
        if key not in ['binary', 'octal', 'decimal', 'hexadecimal']:
            warnings.warn("'numeric' engine supports following keys: {}".format(['binary', 'octal', 'decimal', 'hexadecimal']))
            return "", ""
        else:
            transformed_data = ' '.join(format(ord(i), helpers.NUMERIC_DICT[key]) for i in message)
            return transformed_data, key

    def case(self, message: str, key="capitalize"):
        """Procedure includes transforming the message from one case to another.

        Args:
            message (str): message to be encrypted/decrypted.
            type (str, required): Choices available [upper, lower, capitalize, alternating, inverse]. Defaults to capitalize.

        Returns:
            tuple: transformed data , key
        """
        if type(message) != str:
            warnings.warn("'case' engine can only be applied to str type messages.")
            return "", key
            
        if key == 'upper':
            return message.upper(), key
        elif key == 'lower':
            return message.lower(), key
        elif key == 'capitalize':
            return message.capitalize(), key
        elif key == 'alternating':
            transformed_data = [ele.upper() if not idx % 2 else ele.lower() for idx, ele in enumerate(message)]
            return "".join(transformed_data), key
        elif key == 'inverse':
            transformed_data = ''
            for letter in message:
                if letter.isupper():
                    transformed_data += letter.lower()
                else:
                    transformed_data += letter.upper()
            return transformed_data, key
        
        else:
            warnings.warn("'case' engine supports following keys: {}".format(['upper', 'lower', 'capitalize', 'alternating', 'inverse']))
            return "", key

    def morse(self, message: str, key=None):
        """Morse code is a method used in telecommunication to encode text characters as standardized sequences of two different signal durations, called dots and dashes.

        Args:
            message (str): message to be encrypted/decrypted.
            key (optional): Mode of operation. Can be one of [encrypt, decrypt]. Defaults to 'encrypt'

        Returns:
            tuple: encrypted/decrypted data , key
        """
        if key == 'encrypt':
            message = message.upper()
            transformed_data = ''
            for letter in message:
                if letter != ' ':
                    try:
                        transformed_data += helpers.MORSE_CODE_DICT[letter] + ' '
                    except KeyError:
                        warnings.warn("Some symbols in the input message doesn't have a morse equivalent.")
                        return "", ""
                else:
                    transformed_data += ' '
        
            return transformed_data, key

        elif key == 'decrypt':
            message += ' '
            transformed_data = ''
            citext = ''
            for letter in message:
                if (letter != ' '):
                    i = 0
                    citext += letter
                else:
                    i += 1
                    if i == 2 :
                        transformed_data += ' '
                    else:
                        transformed_data += list(helpers.MORSE_CODE_DICT.keys())[list(helpers.MORSE_CODE_DICT.values()).index(citext)]
                        citext = ''
        
            return transformed_data, key
        
        else:
            warnings.warn("'morse' engine supports following keys: {}".format(['encrypt', 'decrypt']))
            return "", key

    def alphabetic(self, message: str, key="nato"):
        """Procedure includes transforming the message from one letters to various alphabet systems.

        Args:
            message (str): message to be encrypted/decrypted.
            type (str, required): Choices available [nato, dutch, german, swedish]. Defaults to nato.

        Returns:
            tuple: transformed data , key
        """
        if type(message) != str:
            warnings.warn("'case' engine can only be applied to str type messages.")
            return "", key

        message = message.upper()
        transformed_data = []
        if key == 'nato':
            namespace = helpers.NATO
        if key == 'dutch':
            namespace = helpers.DUTCH
        if key == 'german':
            namespace = helpers.GERMAN
        if key == 'swedish':
            namespace = helpers.GERMAN
        else:
            transformed_data = ["unsupported key"]

        for letter in message:
            if letter in namespace.keys():
                transformed_data.append(namespace[letter])
            else:
                transformed_data.append(letter)

        return " ".join(transformed_data), key
