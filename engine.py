import string, random, math, base64, binascii, warnings

from cryptography.fernet import Fernet
from collections import deque
from itertools import cycle


class Cypher:
    def __init__(self):
        self.symbols = deque(sorted(string.ascii_letters+string.digits+string.punctuation+' '))
        self.order = [ord(i) for i in self.symbols]

    def __str__(self):
        return """
        Cryptogram provides its users with a variety of Cypher Engines to encrypt their messages

        Available Engines:

        Reverse Cypher
            About - Procedure includes reversing the message.
            Strength - Low
            Key - No key required for encryption or decryption

        Caeser Cypher
            About - Procedure includes shifting the dictionary.
            Strength - Low
            Key - <int> type key required for encryption or decryption

        Shifting Caeser Cypher
            About - Procedure includes shifting the dictionary continously.
            Strength - Moderate
            Key - <int> type key required for encryption or decryption

        ROT13 Cypher
            About - Procedure includes shifting the dictionary by a value of 13.
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
            About - Procedure includes modifying caeser cypher with multiplication operator.
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
        """


    def encrypt(self, message, engine, key=None):
        encrypted = eval("self."+engine)(message=message, encrypt=True, decrypt=False, key=key)
        return {'encrypted_message': encrypted[0], 'key': encrypted[1], 'engine': engine}
    
    def decrypt(self, message, engine, key=None):
        decrypted = eval("self."+engine)(message=message, encrypt=False, decrypt=True, key=key)
        return {'decrypted_message': decrypted[0], 'key': decrypted[1], 'engine': engine}


    def reverse(self, message, encrypt=False, decrypt=False, key=None):
        return message[::-1], key

    def caeser(self, message, encrypt=False, decrypt=False, key=None):
        if type(key) not in [int, float]:
            warnings.warn("int based key is preferred for ceaser cypher. Assuming random key.")
            key = random.randint(1, 10000)

        rotated_symbols = self.symbols.copy()
        rotated_symbols.rotate(-int(key))

        if encrypt:                
            encrypted_data = ''.join([rotated_symbols[self.symbols.index(sym)] for sym in message])
            return encrypted_data, int(key)

        if decrypt:
            decrypted_data = ''.join([self.symbols[rotated_symbols.index(sym)] for sym in message])
            return decrypted_data, int(key)
    
    def shifting_caeser(self, message, encrypt=False, decrypt=False, key=None):
        if type(key) not in [int, float]:
            warnings.warn("int based key is preferred for shifting ceaser cypher. Assuming random key.")
            key = random.randint(1, 10000)
        
        if encrypt:
            rotated_symbols = self.symbols.copy()
            encrypted_data = ''

            for sym in message:
                rotated_symbols.rotate(-int(key))
                encrypted_data += rotated_symbols[self.symbols.index(sym)]

            return encrypted_data, int(key)

        if decrypt:
            rotated_symbols = self.symbols.copy()
            decrypted_data = ''

            for sym in message:
                rotated_symbols.rotate(-int(key))
                decrypted_data += self.symbols[rotated_symbols.index(sym)]

            return decrypted_data, int(key)
    
    def rot13(self, message, encrypt=False, decrypt=False, key=None):
        rotated_symbols = self.symbols.copy()
        rotated_symbols.rotate(-13)

        if encrypt:                
            encrypted_data = ''.join([rotated_symbols[self.symbols.index(sym)] for sym in message])
            return encrypted_data, 13

        if decrypt:
            decrypted_data = ''.join([self.symbols[rotated_symbols.index(sym)] for sym in message])
            return decrypted_data, 13

    def transposition(self, message, encrypt=False, decrypt=False, key=None):
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

            return ''.join(encrypted_data), int(key)
        
        if decrypt:
            columns = math.ceil(len(message) / int(key))
            decrypted_data = [''] * columns
            for i in range(columns):
                decrypted_data[i] += message[i::columns]

            return ''.join(decrypted_data), int(key)

    def base64(self, message, encrypt=False, decrypt=False, key=None):
        if encrypt:
            encrypted_data = base64.b64encode(message.encode('ascii'))
            return encrypted_data.decode('ascii'), key
        if decrypt:
            decrypted_data = base64.b64decode(message.encode('ascii'))
            return decrypted_data.decode('ascii'), key

    def xor(self, message, encrypt=False, decrypt=False, key=None):
        if (not key) or (type(key) != str):
            warnings.warn("str based key is preferred for xor cypher. Assuming random key.")
            key = ''.join([random.choice(self.symbols) for _ in range(len(message))])

        if encrypt:
            data = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(message, cycle(key)))
            encrypted_data = base64.b64encode(data.encode('ascii')).decode('ascii')
            return encrypted_data, key

        if decrypt:
            data = base64.b64decode(message.encode('ascii')).decode('ascii')
            decrypted_data = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))
            return decrypted_data, key
    
    def multiplicative(self, message, encrypt=False, decrypt=False, key=None):
        if type(key) not in [int, float]:
            warnings.warn("int based key is preferred for multiplicative cypher. Assuming random key.")
            key = random.randint(1, 10000)

        if encrypt:
            encrypted_data = [self.symbols[(self.symbols.index(sym)*int(key))%len(self.symbols)] for sym in message]
            return ''.join(encrypted_data), int(key)
        
        if decrypt:
            decrypted_data = ''
            for sym in message:
                for og_sym in self.symbols:
                    if self.symbols[(self.symbols.index(og_sym)*int(key))%len(self.symbols)] == sym:
                        decrypted_data += og_sym

            return decrypted_data, int(key)

    def monoalphabetic(self, message, encrypt=False, decrypt=False, key=None):
        if encrypt:
            shuffled_symbols = self.symbols.copy()
            random.shuffle(shuffled_symbols)

            key = dict(zip(self.symbols, shuffled_symbols))
            encrypted_data = []
            for sym in message:
                encrypted_data.append(key.get(sym))

            encrypted_data = base64.b64encode(''.join(encrypted_data).encode('ascii')).decode('ascii')

            return encrypted_data, key

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
                
                return ''.join(decrypted_data), inverse_key
            except Exception as e:
                raise ValueError("Monoalphabetic cypher can be decrypted with the exact same key generated during encryption")
    
    def fernet(self, message, encrypt=False, decrypt=False, key=None):
        if encrypt:
            key = Fernet.generate_key()
            encrypted_data = Fernet(key).encrypt(message.encode('utf-8')).decode('utf-8')
            key = key.decode('utf-8')
            return encrypted_data, key

        if decrypt:
            try:
                key = key.encode('utf-8')
                decrypted_data = Fernet(key).decrypt(message.encode('utf-8')).decode('utf-8')
                key = key.decode('utf-8')
                return decrypted_data, key
            except Exception as e:
                raise ValueError("Fernet cypher can be decrypted with the exact same key generated during encryption")

    def onetimepad(self, message, encrypt=False, decrypt=False, key=None):
        if (not key) or (type(key) != str):
            warnings.warn("str based key is preferred for onetimepad cypher. Assuming random key.")
            key = ''.join([random.choice(self.symbols) for _ in range(len(message))])

        if encrypt:
            data = ''.join([chr(ord(x)^ord(y)) for x, y in zip(message, cycle(key))])
            encrypted_data = (binascii.hexlify(data.encode())).decode()
            return encrypted_data, key
        if decrypt:
            data = (binascii.unhexlify(message.encode())).decode()
            decrypted_data = ''.join([chr(ord(x)^ord(y)) for x, y in zip(data, cycle(key))])
            return decrypted_data, key


    