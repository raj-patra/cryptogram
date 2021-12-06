# 🐱‍💻Cryptogram
Cryptogram is a cryptography engine with `almost` all of the popular encrypting, encoding and transforming algorithms.

[![forthebadge](https://forthebadge.com/images/badges/built-with-swag.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-black-magic.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](https://forthebadge.com)

### Encryption engines
---
Encryption engines have the provision to encrypt and decrypt a message generally dependent on a key which
needs to be passed as an argument during encryption and decryprtion.
* [Caeser](https://en.wikipedia.org/wiki/Caesar_cipher)
* [Shifting Caesar](https://en.wikipedia.org/wiki/Caesar_cipher)
* [ROT13](https://en.wikipedia.org/wiki/ROT13)
* [Transposition](https://en.wikipedia.org/wiki/Transposition_cipher)
* [Xor](https://en.wikipedia.org/wiki/XOR_cipher)
* [Multiplicative](https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_multiplicative_cipher.htm)
* [Monoalphabetic](https://en.wikipedia.org/wiki/Substitution_cipher)
* [Fernet](https://en.wikipedia.org/wiki/Symmetric-key_algorithm)
* [Onetimepad](https://en.wikipedia.org/wiki/One-time_pad)
* [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
* [Pseudo Random](http://www.google.com?query=how%20to%20shuffle%20list%20python)
* [Vigenere](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
* [Rail Fence](https://en.wikipedia.org/wiki/Rail_fence_cipher)

### Transformation engines
---
Transformation engines convert the target message from one form/class to another. It doesn't have any
provision to get back the data once transformed.
* Symbol Reversal
* Numeric System
* Case Transform
* Morse Transform
* Alphabetic Transform
    * NATO phonetic alphabet
    * Dutch spelling alphabet
    * German spelling alphabet
    * Swedish spelling alphabet

### Encoding engines - WIP
---
Encoding engines process data into a format required for various kinds of information processing procedures, data transmission, storage and compression/decompression.
* [Base64](https://en.wikipedia.org/wiki/Base64)
* [URL](https://en.wikipedia.org/wiki/Percent-encoding)


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

> Please think of leaving a star on the repo if you think it sparked your curiosity. 🙏