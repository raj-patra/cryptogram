# Imports
import base64
import binascii
import math
import random
import string
import warnings
from collections import deque
from itertools import cycle

import rsa
from cryptography.fernet import Fernet

from . constants import CYPHER


class Cypher:
    def __init__(self):
        self.__symbols__ = deque(sorted(string.ascii_letters+string.digits+string.punctuation+' '))

    def __str__(self):
        return CYPHER

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
        """About - RSA (Rivest???Shamir???Adleman) is a public-key cryptosystem that is widely used for secure data transmission.

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

    def rail_fence(self, message: str, encrypt=False, decrypt=False, key=None):
        """Procedure includes encrypting alphabetic text in zig-zag order. It is a form of transposition cypher.

        Args:
            message (str): message to be encrypted/decrypted.
            encrypt (bool, optional): Mode of operation. Defaults to False.
            decrypt (bool, optional): Mode of operation. Defaults to False.
            key (int): <int> type key required for encryption or decryption. Defaults to randint(1, 10).

        Returns:
            tuple: encrypted/decrypted data , key
        """
        if type(key) != int:
            warnings.warn("int based key is preferred for rail fence cypher. Assuming random key.")
            key = random.randint(1, 10)
            
        if encrypt:
            rail = [['\n' for _ in range(len(message))] for _ in range(key)]
     
            dir_down = False
            row, col = 0, 0
            
            for i in range(len(message)):
                if (row == 0) or (row == key - 1):
                    dir_down = not dir_down
                
                rail[row][col] = message[i]
                col += 1
                
                if dir_down:
                    row += 1
                else:
                    row -= 1

            result = []
            for i in range(key):
                for j in range(len(message)):
                    if rail[i][j] != '\n':
                        result.append(rail[i][j])
                        
            encrypted_data = ''.join(result)
            return (encrypted_data, int(key))
        
        if decrypt:
            rail = [['\n' for _ in range(len(message))] for _ in range(key)]
            
            dir_down = None
            row, col = 0, 0
     
            for i in range(len(message)):
                if row == 0:
                    dir_down = True
                if row == key - 1:
                    dir_down = False
                
                rail[row][col] = '*'
                col += 1
                
                if dir_down:
                    row += 1
                else:
                    row -= 1
                    
            index = 0
            for i in range(key):
                for j in range(len(message)):
                    if ((rail[i][j] == '*') and
                    (index < len(message))):
                        rail[i][j] = message[index]
                        index += 1
                
            result = []
            row, col = 0, 0
            for i in range(len(message)):
                
                if row == 0:
                    dir_down = True
                if row == key-1:
                    dir_down = False
                    
                if (rail[row][col] != '*'):
                    result.append(rail[row][col])
                    col += 1
                    
                if dir_down:
                    row += 1
                else:
                    row -= 1
                    
            decrypted_data = ''.join(result)            
            return(decrypted_data, int(key))

