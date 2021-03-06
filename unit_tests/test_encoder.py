import sys
import unittest

from cryptogram.encode import Encode

sys.path.insert(0, '..')


class TestEncoder(unittest.TestCase):
    def setUp(self) -> None:
        self.message = "Hello World"
        self.enc_obj = Encode()
        
        return super().setUp()
    
    def test_encode_init(self):
        self.assertEqual(str, type(self.enc_obj.__str__()))
        self.assertEqual(list, type(self.enc_obj.__engines__()))
    
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
    
    def test_encode_ascii85(self):
        
        encoded = self.enc_obj.encode(message=self.message, engine="ascii85")
        decoded = self.enc_obj.decode(message=encoded["encoded_message"], engine="ascii85")
        self.assertEqual(decoded["decoded_message"], self.message)
        
    def test_encode_url(self):
        
        encoded = self.enc_obj.encode(message=self.message, engine="url")
        decoded = self.enc_obj.decode(message=encoded["encoded_message"], engine="url")
        self.assertEqual(decoded["decoded_message"], self.message)

    def test_encode_base85(self):
        
        encoded = self.enc_obj.encode(message=self.message, engine="base85")
        decoded = self.enc_obj.decode(message=encoded["encoded_message"], engine="base85")
        self.assertEqual(decoded["decoded_message"], self.message)
