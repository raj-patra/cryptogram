import unittest

from cryptogram.cypher import Cypher
from cryptogram.encode import Encode
from cryptogram.transform import Transform


class TestCryptogram(unittest.TestCase):
    def setUp(self) -> None:
        self.message = "Hello World"
        self.enc_obj = Encode()
        self.trf_obj = Transform()
        self.cyp_obj = Cypher()
        
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
  
        
    def test_transform_init(self):
        self.assertEqual(str, type(self.trf_obj.__str__()))
        self.assertEqual(list, type(self.trf_obj.__engines__()))
    
    def test_transform_reverse(self):
        
        transformed = self.trf_obj.transform(message=self.message, engine="reverse")
        self.assertEqual(transformed["transformed_message"], self.message[::-1])
        
        transformed = self.trf_obj.transform(message=404, engine="reverse")
        self.assertEqual("", transformed["transformed_message"])
  
    def test_transform_numeric(self):
        
        transformed = self.trf_obj.transform(message=self.message, engine="numeric", key="binary")
        self.assertEqual(3, len(transformed.keys()))
        
        transformed = self.trf_obj.transform(message=self.message, engine="numeric", key="octal")
        self.assertEqual(3, len(transformed.keys()))
        
        transformed = self.trf_obj.transform(message=self.message, engine="numeric", key="decimal")
        self.assertEqual(3, len(transformed.keys()))
        
        transformed = self.trf_obj.transform(message=self.message, engine="numeric", key="hexadecimal")
        self.assertEqual(3, len(transformed.keys()))
        
        transformed = self.trf_obj.transform(message=self.message, engine="numeric", key="test")
        self.assertEqual("", transformed["transformed_message"])

    def test_transform_case(self):
        
        transformed = self.trf_obj.transform(message=self.message, engine="case", key="upper")
        self.assertEqual(self.message.upper(), transformed["transformed_message"])
        
        transformed = self.trf_obj.transform(message=self.message, engine="case", key="lower")
        self.assertEqual(self.message.lower(), transformed["transformed_message"])
        
        transformed = self.trf_obj.transform(message=self.message, engine="case", key="capitalize")
        self.assertEqual(self.message.capitalize(), transformed["transformed_message"])
        
        transformed = self.trf_obj.transform(message=self.message, engine="case", key="alternating")
        self.assertEqual(len(self.message), len(transformed["transformed_message"]))
        
        transformed = self.trf_obj.transform(message=self.message, engine="case", key="inverse")
        self.assertEqual(len(self.message), len(transformed["transformed_message"]))
                
        transformed = self.trf_obj.transform(message=self.message, engine="case", key="test")
        self.assertEqual("", transformed["transformed_message"])
                
        transformed = self.trf_obj.transform(message=123, engine="case", key="test")
        self.assertEqual("", transformed["transformed_message"])
            
    def test_transform_morse(self):
        
        encrypted = self.trf_obj.transform(message=self.message, engine="morse", key="encrypt")
        decrypted = self.trf_obj .transform(message=encrypted["transformed_message"], engine=encrypted["engine"], key="decrypt")
        self.assertEqual(len(decrypted["transformed_message"].strip()), len(self.message))
    
    def test_transform_alphabetic(self):
        
        transformed = self.trf_obj.transform(message=self.message, engine="alphabetic", key="nato")
        self.assertEqual(3, len(transformed.keys()))
        
        transformed = self.trf_obj.transform(message=self.message, engine="alphabetic", key="dutch")
        self.assertEqual(3, len(transformed.keys()))
        
        transformed = self.trf_obj.transform(message=self.message, engine="alphabetic", key="german")
        self.assertEqual(3, len(transformed.keys()))
        
        transformed = self.trf_obj.transform(message=self.message, engine="alphabetic", key="swedish")
        self.assertEqual(3, len(transformed.keys()))
        
        transformed = self.trf_obj.transform(message=self.message, engine="alphabetic", key="test")
        self.assertEqual(0, len(transformed['transformed_message']))
        
        transformed = self.trf_obj.transform(message=self.message, engine="alphabetic", key=123)
        self.assertEqual(0, len(transformed['transformed_message']))