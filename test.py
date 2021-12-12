from base64 import decode, encode
from cryptogram.cypher import Cypher
from cryptogram.transform import Transform
from cryptogram.encode import Encode

import unittest


class TestCryptogram(unittest.TestCase):
    def setUp(self) -> None:
        self.message = "Hello World!"
        self.enc_obj = Encode()
        self.trf_obj = Transform()
        self.cyp_obj = Cypher()
        
        return super().setUp()
    
    def test_encode_base64(self):
        
        encoded = self.enc_obj.encode(message=self.message, engine="base64")
        decoded = self.enc_obj.decode(message=encoded["encoded_message"], engine="base64")
        self.assertEqual(decoded["decoded_message"], self.message)
    
    def test_encode_base32(self):
        
        encoded = self.enc_obj.encode(message=self.message, engine="base32")
        decoded = self.enc_obj.decode(message=encoded["encoded_message"], engine="base32")
        self.assertEqual(decoded["decoded_message"], self.message)
    
    def test_encode_base16(self):
        
        encoded = self.enc_obj.encode(message=self.message, engine="base16")
        decoded = self.enc_obj.decode(message=encoded["encoded_message"], engine="base16")
        self.assertEqual(decoded["decoded_message"], self.message)

