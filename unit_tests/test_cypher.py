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
            
    def test_cypher_init(self):
        self.assertEqual(str, type(self.cyp_obj.__str__()))
        self.assertEqual(list, type(self.cyp_obj.__engines__()))
    
    def test_cypher_caesar(self):
        
        encrypted = self.cyp_obj.encrypt(message=self.message, engine="caesar", key=1)
        decrypted = self.cyp_obj.decrypt(message=encrypted["encrypted_message"], engine=encrypted["engine"], key=encrypted["key"])
        self.assertEqual(decrypted["decrypted_message"], self.message)
        
        encrypted = self.cyp_obj.encrypt(message=self.message, engine="caesar", key="hello")
        decrypted = self.cyp_obj.decrypt(message=encrypted["encrypted_message"], engine=encrypted["engine"], key=encrypted["key"])
        self.assertEqual(decrypted["decrypted_message"], self.message)
        
        encrypted = self.cyp_obj.encrypt(engine="caesar", key=1)
        decrypted = self.cyp_obj.decrypt(message=encrypted["encrypted_message"], engine=encrypted["engine"], key=encrypted["key"])
        self.assertEqual(decrypted["decrypted_message"], 'hello world')
    
    def test_cypher_shifting_caesar(self):
        
        encrypted = self.cyp_obj.encrypt(message=self.message, engine="shifting_caesar", key=1)
        decrypted = self.cyp_obj.decrypt(message=encrypted["encrypted_message"], engine=encrypted["engine"], key=encrypted["key"])
        self.assertEqual(decrypted["decrypted_message"], self.message)
        
        encrypted = self.cyp_obj.encrypt(message=self.message, engine="shifting_caesar", key="hello")
        decrypted = self.cyp_obj.decrypt(message=encrypted["encrypted_message"], engine=encrypted["engine"], key=encrypted["key"])
        self.assertEqual(decrypted["decrypted_message"], self.message)
        
        encrypted = self.cyp_obj.encrypt(engine="shifting_caesar", key=5)
        decrypted = self.cyp_obj.decrypt(message=encrypted["encrypted_message"], engine=encrypted["engine"], key=encrypted["key"])
        self.assertEqual(decrypted["decrypted_message"], 'hello world')
        
    def test_cypher_rot13(self):
        
        encrypted = self.cyp_obj.encrypt(message=self.message, engine="rot13")
        decrypted = self.cyp_obj.decrypt(message=encrypted["encrypted_message"], engine=encrypted["engine"], key=encrypted["key"])
        self.assertEqual(decrypted["decrypted_message"], self.message)       
         
        encrypted = self.cyp_obj.encrypt(engine="rot13")
        decrypted = self.cyp_obj.decrypt(message=encrypted["encrypted_message"], engine=encrypted["engine"], key=encrypted["key"])
        self.assertEqual(decrypted["decrypted_message"], 'hello world')
        
    def test_cypher_transposition(self):
        
        encrypted = self.cyp_obj.encrypt(message=self.message, engine="transposition", key=6)
        decrypted = self.cyp_obj.decrypt(message=encrypted["encrypted_message"], engine=encrypted["engine"], key=encrypted["key"])
        self.assertEqual(decrypted["decrypted_message"], self.message)
        
        encrypted = self.cyp_obj.encrypt(message=self.message, engine="transposition", key="hello")
        decrypted = self.cyp_obj.decrypt(message=encrypted["encrypted_message"], engine=encrypted["engine"], key=encrypted["key"])
        self.assertEqual(decrypted["decrypted_message"], self.message)
