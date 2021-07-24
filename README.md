# Cryptogram
Cryptography engine with all the popular encrypting algorithms.

### Available engines
* [Symbol Reversal](http://www.google.com?query=how%20to%20reverse%20string)
* [Caeser Cypher](https://en.wikipedia.org/wiki/Caesar_cipher)
* [Shifting Caesar Cypher](https://en.wikipedia.org/wiki/Caesar_cipher)
* [ROT13 Cypher](https://en.wikipedia.org/wiki/ROT13)
* [Transposition Cypher](https://en.wikipedia.org/wiki/Transposition_cipher)
* [Base64 Cypher](https://en.wikipedia.org/wiki/Base64)
* [Xor Cypher](https://en.wikipedia.org/wiki/XOR_cipher)
* [Multiplicative Cypher](https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_multiplicative_cipher.htm)
* [Monoalphabetic Cypher](https://en.wikipedia.org/wiki/Substitution_cipher)
* [Fernet Cypher](https://en.wikipedia.org/wiki/Symmetric-key_algorithm)
* [Onetimepad Cypher](https://en.wikipedia.org/wiki/One-time_pad)

### Clone and setup
```
git clone https://github.com/raj-patra/cryptogram.git
cd cryptogram
pip install -r requirements.txt
```

### Usage
Make sure to keep the cloned folder inside your project directory
```python
from cryptogram.engine import Cypher

obj = Cypher()
encrypted = obj.encrypt(message='hello world', engine='multiplicative',  key=16196516)
# {'encrypted_message': '6=lle re^l_', 'key': 16196516, 'engine': 'multiplicative'}

decrypted = obj.decrypt(message=encrypted['encrypted_message'], engine=encrypted['engine'], key=encrypted['key'])
# {'decrypted_message': 'hello world', 'key': 16196516, 'engine': 'multiplicative'}

```