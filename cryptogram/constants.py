TRANSFORM = """
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

ENCODE = """
    Cryptogram provides its users with a variety of Encoding Engines to encode their messages

    Available Engines:

    Base64 Encoding
        About - Procedure includes standard text-to-binary encoding scheme (64 bit).

    Base32 Encoding
        About - Procedure includes standard text-to-binary encoding scheme (32 bit).

    Base16 Encoding
        About - Procedure includes standard text-to-binary encoding scheme (16 bit).

    Ascii85 Encoding
        About - Procedure includes standard text-to-binary encoding scheme (85 bit).

    URL Encoding
        About - Procedure includes encoding arbitrary data using only the limited US-ASCII characters.

"""

CYPHER = """
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
        
    Rail Fence Cypher
        About - Procedure includes encrypting alphabetic text in zig-zag order. It is a form of transposition cypher.
        Strength - Moderate
        Key - <int> type key required for encryption or decryption 

    Note - Key provided/generated during encryption should be used for a successful decryption.
"""