# Imports
import base64, binascii, math, random, string, warnings, rsa

from cryptography.fernet import Fernet
from collections import deque
from itertools import cycle
import helpers


class Encode:
    def __init__(self):
        self.__symbols__ = deque(sorted(string.ascii_letters+string.digits+string.punctuation+' '))

    def __str__(self):
        return """
        Cryptogram provides its users with a variety of Encoding Engines to encode their messages

        Available Engines:

        Base64 Cypher
            About - Procedure includes standard text-to-binary encoding scheme.
        
        """

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
            encrypted_data = base64.b64encode(message.encode('ascii'))
            return (encrypted_data.decode('ascii'))
        if decode:
            decrypted_data = base64.b64decode(message.encode('ascii'))
            return (decrypted_data.decode('ascii'))
 


class Transform:
    def __init__(self):
        self.__symbols__ = deque(sorted(string.ascii_letters+string.digits+string.punctuation+' '))

    def __str__(self):
        return """
        Cryptogram provides its users with a variety of Transformation Engines to transform their messages

        Available Engines:

        Reverse Transform
            About - Procedure includes reversing the message.
            Key - No key required for encryption or decryption
        
        Numeric Transform
            About - Procedure includes transforming the message from strings to a equivalent number system.
            Key - Choices available [binary, octal, decimal, hexadecimal]

        Case Transform
            About - Procedure includes transforming the message from one case to another.
            Key - Choices available [upper, lower, capitalize, alternating, inverse]

        Morse Cypher
            About - Morse code is a encoding procedure that encodes text characters as standardized sequences of two different signal durations.
            Strength - Low
            Key - Choices available [encrypt, decrypt]
        """

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


class Cypher:
    def __init__(self):
        self.__symbols__ = deque(sorted(string.ascii_letters+string.digits+string.punctuation+' '))

    def __str__(self):
        return """
        Cryptogram provides its users with a variety of Cypher Engines to encrypt their messages

        Available Engines:

        Caesar Cypher
            About - Procedure includes shifting the dictionary.
            Strength - Low
            Key - <int> type key required for encryption or decryption

        Shifting caesar Cypher
            About - Procedure includes shifting the dictionary continously.
            Strength - Moderate
            Key - <int> type key required for encryption or decryption

        ROT13 Cypher
            About - Procedure includes shifting the dictionary by the value of 13.
            Strength - Low
            Key - No key required for encryption or decryption

        Transposition Cypher
            About - Procedure includes arranging the message row-wise, in a matrix and extracting column-wise.
            Strength - Moderate
            Key - <int> type key required for encryption or decryption

        Base64 Cypher
            About - Procedure includes standard text-to-binary encoding scheme.
            Strength - Low
            Key - No key required for encryption or decryption
        
        Xor Cypher
            About - Procedure includes applying xor operator on message and key.
            Strength - High
            Key - <str> type key required for encryption or decryption

        Multiplicative Cypher
            About - Procedure includes modifying caesar cypher with multiplication operator.
            Strength - High
            Key - <bigint> type key required for encryption or decryption

        Monoalphabetic Cypher
            About - Procedure includes replacing original symbols with random symbols from key.
            Strength - High
            Key - Key generated automatically for encryption or decryption. 

        Fernet Cypher
            About - Procedure includes symmetric cryptographic schemes.
            Strength - High
            Key - Key generated automatically for encryption or decryption.

        OneTimePad Cypher
            About - Procedure includes modifying xor cypher with base64 encoding scheme.
            Strength - High
            Key - <str> type key required for encryption or decryption

        RSA Cypher
            About - RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem that is widely used for secure data transmission.
            Strength - High
            Key - Key generated automatically for encryption or decryption.

        Pseudo Random Cypher
            About - Procedure includes shuffling the dictionary.
            Strength - High
            Key - <int> type key required for encryption or decryption
        
        Vigenere Cypher
            About - Procedure includes encrypting alphabetic text by using a random sample genrated from a seed.
            Strength - High
            Key - <int> type key required for encryption or decryption 

        Note - Key provided/generated during encryption should be used for a successful decryption.
        """

    def __engines__(self):
        return [x for x in dir(self) if not x.startswith('__')]

    def encrypt(self, message='hello world', engine='rot13', key=13):
        """encrypts message attribute with the specified engine

        Args:
            message (str, optional): message to be encrypted. Defaults to 'hello world'.
            engine (str, optional): engine to be used for encryption. Defaults to 'rot13'.
            key ([int, float, str], optional): key used for encryption. Defaults to 13.

        Returns:
           dict: dictionary with encrypted message, key and the engine used.
        """
        encrypted = eval("self."+engine)(message=message, encrypt=True, decrypt=False, key=key)
        return {'encrypted_message': encrypted[0], 'key': encrypted[1], 'engine': engine}
    
    def decrypt(self, message='uryy|-%| yq', engine='rot13', key=13):
        """decrypts message attribute with the specified engine

        Args:
            message (str, optional): message to be decrypted. Defaults to 'uryy|-%| yq'.
            engine (str, optional): engine to be used for decryption. Defaults to 'rot13'.
            key ([int, float, str], optional): key used for decryption. Defaults to 13.

        Returns:
           dict: dictionary with decrypted message, key and the engine used.
        """
        decrypted = eval("self."+engine)(message=message, encrypt=False, decrypt=True, key=key)
        return {'decrypted_message': decrypted[0], 'key': decrypted[1], 'engine': engine}


    def caesar(self, message: str, encrypt=False, decrypt=False, key=None):
        """Procedure includes shifting the dictionary.

        Args:
            message (str): message to be encrypted/decrypted.
            encrypt (bool, optional): Mode of operation. Defaults to False.
            decrypt (bool, optional): Mode of operation. Defaults to False.
            key (int): <int> type key required for encryption or decryption. Defaults to randint(1, 10000).

        Returns:
            tuple: encrypted/decrypted data , key
        """
        if type(key) not in [int, float]:
            warnings.warn("int based key is preferred for ceaser cypher. Assuming random key.")
            key = random.randint(1, 10000)

        rotated_symbols = self.__symbols__.copy()
        rotated_symbols.rotate(-int(key))

        if encrypt:                
            encrypted_data = ''.join([rotated_symbols[self.__symbols__.index(sym)] for sym in message])
            return (encrypted_data, int(key))

        if decrypt:
            decrypted_data = ''.join([self.__symbols__[rotated_symbols.index(sym)] for sym in message])
            return (decrypted_data, int(key))
    
    def shifting_caesar(self, message: str, encrypt=False, decrypt=False, key=None):
        """Procedure includes shifting the dictionary continously.

        Args:
            message (str): message to be encrypted/decrypted.
            encrypt (bool, optional): Mode of operation. Defaults to False.
            decrypt (bool, optional): Mode of operation. Defaults to False.
            key (int): <int> type key required for encryption or decryption. Defaults to randint(1, 10000).

        Returns:
            tuple: encrypted/decrypted data , key
        """
        if type(key) not in [int, float]:
            warnings.warn("int based key is preferred for shifting ceaser cypher. Assuming random key.")
            key = random.randint(1, 10000)
        
        if encrypt:
            rotated_symbols = self.__symbols__.copy()
            encrypted_data = ''

            for sym in message:
                rotated_symbols.rotate(-int(key))
                encrypted_data += rotated_symbols[self.__symbols__.index(sym)]

            return (encrypted_data, int(key))

        if decrypt:
            rotated_symbols = self.__symbols__.copy()
            decrypted_data = ''

            for sym in message:
                rotated_symbols.rotate(-int(key))
                decrypted_data += self.__symbols__[rotated_symbols.index(sym)]

            return (decrypted_data, int(key))
    
    def rot13(self, message: str, encrypt=False, decrypt=False, key=None):
        """Procedure includes shifting the dictionary by the value of 13.

        Args:
            message (str): message to be encrypted/decrypted.
            encrypt (bool, optional): Mode of operation. Defaults to False.
            decrypt (bool, optional): Mode of operation. Defaults to False.
            key (None, optional): No key required for encryption or decryption.

        Returns:
            tuple: encrypted/decrypted data , key
        """
        rotated_symbols = self.__symbols__.copy()
        rotated_symbols.rotate(-13)

        if encrypt:                
            encrypted_data = ''.join([rotated_symbols[self.__symbols__.index(sym)] for sym in message])
            return (encrypted_data, 13)

        if decrypt:
            decrypted_data = ''.join([self.__symbols__[rotated_symbols.index(sym)] for sym in message])
            return (decrypted_data, 13)

    def transposition(self, message: str, encrypt=False, decrypt=False, key=None):
        """About - Procedure includes arranging the message row-wise, in a matrix and extracting column-wise.

        Args:
            message (str): message to be encrypted/decrypted.
            encrypt (bool, optional): Mode of operation. Defaults to False.
            decrypt (bool, optional): Mode of operation. Defaults to False.
            key (int): <int> type key required for encryption or decryption. Defaults to randint(1, len(message)).

        Returns:
            tuple: encrypted/decrypted data , key
        """
        if (not key) or (type(key) not in [int, float]) or (int(key) >= len(message)):
            warnings.warn("int based key (len(key) <= len(message)) is preferred for shifting transposition cypher. Assuming random key.")
            key = random.randint(1, len(message))

        if encrypt:
            encrypted_data = [''] * int(key)
            for col in range(int(key)):
                position = col
                while position < len(message):
                    encrypted_data[col] += message[position]
                    position += int(key)

            return (''.join(encrypted_data), int(key))
        
        if decrypt:
            columns = math.ceil(len(message) / int(key))
            decrypted_data = [''] * columns
            for i in range(columns):
                decrypted_data[i] += message[i::columns]

            return (''.join(decrypted_data), int(key))

    def xor(self, message: str, encrypt=False, decrypt=False, key=None):
        """About - Procedure includes applying xor operator on message and key..

        Args:
            message (str): message to be encrypted/decrypted.
            encrypt (bool, optional): Mode of operation. Defaults to False.
            decrypt (bool, optional): Mode of operation. Defaults to False.
            key (str): <str> type key required for encryption or decryption. Defaults to random passkey.

        Returns:
            tuple: encrypted/decrypted data , key
        """
        if (not key) or (type(key) != str):
            warnings.warn("str based key is preferred for xor cypher. Assuming random key.")
            key = ''.join([random.choice(self.__symbols__) for _ in range(len(message))])

        if encrypt:
            data = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(message, cycle(key)))
            encrypted_data = base64.b64encode(data.encode('ascii')).decode('ascii')
            return (encrypted_data, key)

        if decrypt:
            data = base64.b64decode(message.encode('ascii')).decode('ascii')
            decrypted_data = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))
            return (decrypted_data, key)
    
    def multiplicative(self, message: str, encrypt=False, decrypt=False, key=None):
        """About - Procedure includes modifying caesar cypher with multiplication operation.

        Args:
            message (str): message to be encrypted/decrypted.
            encrypt (bool, optional): Mode of operation. Defaults to False.
            decrypt (bool, optional): Mode of operation. Defaults to False.
            key (int): <int> type key required for encryption or decryption. Defaults to randint(1, 10000).

        Returns:
            tuple: encrypted/decrypted data , key
        """
        if type(key) not in [int, float]:
            warnings.warn("int based key is preferred for multiplicative cypher. Assuming random key.")
            key = random.randint(1, 10000)

        if encrypt:
            encrypted_data = [self.__symbols__[(self.__symbols__.index(sym)*int(key))%len(self.__symbols__)] for sym in message]
            return (''.join(encrypted_data), int(key))
        
        if decrypt:
            decrypted_data = ''
            for sym in message:
                for og_sym in self.__symbols__:
                    if self.__symbols__[(self.__symbols__.index(og_sym)*int(key))%len(self.__symbols__)] == sym:
                        decrypted_data += og_sym

            return (decrypted_data, int(key))

    def monoalphabetic(self, message: str, encrypt=False, decrypt=False, key=None):
        """About - Procedure includes replacing original symbols with random symbols from key.

        Args:
            message (str): message to be encrypted/decrypted.
            encrypt (bool, optional): Mode of operation. Defaults to False.
            decrypt (bool, optional): Mode of operation. Defaults to False.
            key (dict): Key generated automatically for encryption or decryption.

        Returns:
            tuple: encrypted/decrypted data , key
        """
        if encrypt:
            shuffled_symbols = self.__symbols__.copy()
            random.shuffle(shuffled_symbols)

            key = dict(zip(self.__symbols__, shuffled_symbols))
            encrypted_data = []
            for sym in message:
                encrypted_data.append(key.get(sym))

            encrypted_data = base64.b64encode(''.join(encrypted_data).encode('ascii')).decode('ascii')

            return (encrypted_data, key)

        if decrypt:
            inverse_key = {}
            decrypted_data = []
            original_key = key

            message = base64.b64decode(message.encode('ascii')).decode('ascii')

            try:
                for key, value in original_key.items():
                    inverse_key[value] = key
                for sym in message:
                    decrypted_data.append(inverse_key.get(sym))
                
                return (''.join(decrypted_data), inverse_key)
            except Exception:
                raise ValueError("Monoalphabetic cypher can be decrypted with the exact same key generated during encryption")
    
    def fernet(self, message: str, encrypt=False, decrypt=False, key=None):
        """About - Procedure includes symmetric cryptographic schemes.

        Args:
            message (str): message to be encrypted/decrypted.
            encrypt (bool, optional): Mode of operation. Defaults to False.
            decrypt (bool, optional): Mode of operation. Defaults to False.
            key (Fernet object): Key generated automatically for encryption or decryption.

        Returns:
            tuple: encrypted/decrypted data , key
        """
        if encrypt:
            key = Fernet.generate_key()
            encrypted_data = Fernet(key).encrypt(message.encode('utf-8')).decode('utf-8')
            key = key.decode('utf-8')
            return (encrypted_data, key)

        if decrypt:
            try:
                key = key.encode('utf-8')
                decrypted_data = Fernet(key).decrypt(message.encode('utf-8')).decode('utf-8')
                key = key.decode('utf-8')
                return (decrypted_data, key)
            except Exception:
                raise ValueError("Fernet cypher can be decrypted with the exact same key generated during encryption")

    def onetimepad(self, message: str, encrypt=False, decrypt=False, key=None):
        """About - Procedure includes modifying xor cypher with base64 encoding scheme.

        Args:
            message (str): message to be encrypted/decrypted.
            encrypt (bool, optional): Mode of operation. Defaults to False.
            decrypt (bool, optional): Mode of operation. Defaults to False.
            key (str): <str> type key required for encryption or decryption. Defaults to random passkey.

        Returns:
            tuple: encrypted/decrypted data , key
        """
        if (not key) or (type(key) != str):
            warnings.warn("str based key is preferred for onetimepad cypher. Assuming random key.")
            key = ''.join([random.choice(self.__symbols__) for _ in range(len(message))])

        if encrypt:
            data = ''.join([chr(ord(x)^ord(y)) for x, y in zip(message, cycle(key))])
            encrypted_data = (binascii.hexlify(data.encode())).decode()
            return (encrypted_data, key)
        if decrypt:
            data = (binascii.unhexlify(message.encode())).decode()
            decrypted_data = ''.join([chr(ord(x)^ord(y)) for x, y in zip(data, cycle(key))])
            return (decrypted_data, key)

    def rsa(self, message: str, encrypt=False, decrypt=False, key=None):
        """About - RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem that is widely used for secure data transmission.

        Args:
            message (str): message to be encrypted/decrypted.
            encrypt (bool, optional): Mode of operation. Defaults to False.
            decrypt (bool, optional): Mode of operation. Defaults to False.
            key (Fernet object): Key generated automatically for encryption or decryption.

        Returns:
            tuple: encrypted/decrypted data , key
        """
        if encrypt:
            if type(key) == rsa.key.PublicKey:
                pass # No action needed if user sends the designated PublicKey
            else:
                (public_key, private_key) = rsa.newkeys(1024)
                key = public_key
            encrypted_data = rsa.encrypt(message.encode('utf-8'), key)

            return (encrypted_data, private_key)

        if decrypt:
            decrypted_data = rsa.decrypt(message, key).decode('utf-8')

            return (decrypted_data, key)

    def pseudo_random(self, message: str, encrypt=False, decrypt=False, key=None):
        """Procedure includes shuffling the dictionary with a determined seed.

        Args:
            message (str): message to be encrypted/decrypted.
            encrypt (bool, optional): Mode of operation. Defaults to False.
            decrypt (bool, optional): Mode of operation. Defaults to False.
            key (int): <int> type key required for encryption or decryption. Defaults to randint(1, 10000).

        Returns:
            tuple: encrypted/decrypted data , key
        """
        if type(key) not in [int, float]:
            warnings.warn("int based key is preferred for ceaser cypher. Assuming random key.")
            key = random.randint(1, 10000)

        shuffled_symbols = self.__symbols__.copy()
        random.Random(key).shuffle(shuffled_symbols)

        if encrypt:                
            encrypted_data = ''.join([shuffled_symbols[self.__symbols__.index(sym)] for sym in message])
            return (encrypted_data, int(key))

        if decrypt:
            decrypted_data = ''.join([self.__symbols__[shuffled_symbols.index(sym)] for sym in message])
            return (decrypted_data, int(key))

    def vigenere(self, message: str, encrypt=False, decrypt=False, key=None):
        """Procedure includes encrypting alphabetic text by using a random sample genrated from a seed.

        Args:
            message (str): message to be encrypted/decrypted.
            encrypt (bool, optional): Mode of operation. Defaults to False.
            decrypt (bool, optional): Mode of operation. Defaults to False.
            key (int): <int> type key required for encryption or decryption. Defaults to randint(1, 10000).

        Returns:
            tuple: encrypted/decrypted data , key
        """
        if type(key) not in [int, float]:
            warnings.warn("int based key is preferred for vigenere cypher. Assuming random key.")
            key = random.randint(1, 10000)

        random_symbols = ''.join(random.Random(key).sample(self.__symbols__, k=len(message)))

        if encrypt:
            encrypted_data = ''
            for i in range(len(message)) :
                index = (self.__symbols__.index(message[i]) + self.__symbols__.index(random_symbols[i])) % len(self.__symbols__)
                encrypted_data += self.__symbols__[index]

            return (encrypted_data, int(key))

        if decrypt:
            decrypted_data = ''
            for i in range(len(message)) :
                index = (self.__symbols__.index(message[i]) - self.__symbols__.index(random_symbols[i])) % len(self.__symbols__)
                decrypted_data += self.__symbols__[index]

            return (decrypted_data, int(key))

    

