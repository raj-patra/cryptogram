import sys
sys.path.insert(0, '..')

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
        decrypted = self.trf_obj.transform(message=encrypted["transformed_message"], engine=encrypted["engine"], key="decrypt")
        self.assertEqual(len(decrypted["transformed_message"].strip()), len(self.message))
        
        encrypted = self.trf_obj.transform(message=self.message+'!', engine="morse", key="encrypt")
        self.assertEqual(len(encrypted["transformed_message"]), 0)
        
        encrypted = self.trf_obj.transform(message=self.message, engine="morse", key="test")
        self.assertEqual(len(encrypted["transformed_message"]), 0)
    
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
        
        transformed = self.trf_obj.transform(message=123, engine="alphabetic", key="nato")
        self.assertEqual(0, len(transformed['transformed_message']))
        
        transformed = self.trf_obj.transform(message="👀", engine="alphabetic", key="nato")
        self.assertEqual(1, len(transformed['transformed_message']))
