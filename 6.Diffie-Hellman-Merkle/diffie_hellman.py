from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import getPrime, getStrongPrime
from Crypto.Random import get_random_bytes
from typing import Union
from hashlib import sha256

# Methods for handling encryption and decryption of data, no need to edit


def secret_into_aes_key(secret: int) -> bytes:
    """Convert arbitrary integer for suitable key for AES-CBC by using SHA256 digest"""
    m = sha256()
    m.update(secret.to_bytes((secret.bit_length() + 7) // 8, byteorder="big"))
    return m.digest()


def encrypt_aes(data: Union[bytes, str], key: bytes) -> bytes:
    """Encrypt data after padding, by key, set IV as prefix"""
    if isinstance(data, str):
        data = data.encode("ASCII")
    elif not isinstance(data, bytes):
        raise ValueError("Encryptable data must be in 'bytes' or 'string' format.")
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))
    return cipher.iv + ciphertext


def decrypt_aes(data: bytes, key: bytes) -> bytes:
    """Extract IV, decrypt data by key and unpad"""
    if not isinstance(data, bytes):
        raise ValueError("Decryptable data must be in 'bytes' format.")
    IV = data[: AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv=IV)
    plaintext = unpad(cipher.decrypt(data[AES.block_size :]), AES.block_size)
    return plaintext


class SingleParty:
    """Abstract class for common attributes for each party, e.g. Alice, Bob and Eve. Add public values here"""

    # TODO Choose public values, however it might be that some values are better than others
    g: int = 0
    p_modulus: int = 0  # prime, usually 2048 bits to provide enough security, SAFE PRIME

    _G: int = None  # Shared secret, calculated later

    def encrypt(self, data: bytes, G: int = None) -> bytes:
        """Encrypt data, use established shared secret as key by default if no G parameter provided"""
        return encrypt_aes(data, secret_into_aes_key(G if G else self._G))

    def decrypt(self, data: bytes, G: int = None) -> bytes:
        """Decrypt data, use established shared secret as key by default if no G parameter provided"""
        return decrypt_aes(data, secret_into_aes_key(G if G else self._G))


# Define private exponents for Bob, Alice and Eve
# Check how to get primes https://pycryptodome.readthedocs.io/en/latest/src/util/util.html#module-Crypto.Util.number

# Select a prime which is large enough


class Alice(SingleParty):

    _P: int = 0  # Private exponent
    A: int = 0

    def __init__(self):
        super(SingleParty).__init__()

    def set_A(self):
        """TODO Implement calculation of A"""
        pass

    def set_G(self, B: int):
        """TODO Derive G from B (G is shared secret)"""
        pass


class Bob(SingleParty):

    _P: int = 0  # Private exponent
    B: int = 0

    def __init__(self):
        super(SingleParty).__init__()

    def set_B(self):
        """TODO Implement calculation of B"""
        pass

    def set_G(self, A: int):
        """TODO Derive G from A (G is shared secret)"""
        pass


class Eve(SingleParty):
    """
    TODO
    Eve needs methods and values for both Alice and Bob:
    - two private exponents
    - two shared keys
    - methods for implementing the key exchange and storing A, B, C and D (Check course book from the page 210)
    Note that Eve must change parameters when decrypting/encrypting data
    """

    A: int = 0  # A from Alice
    C: int = 0  # C for Bob
    B: int = 0  # B from Bob
    D: int = 0  # D for Alice
    _P1: int = 0  # Private exponent for Alice
    _P2: int = 0  # Private exponent for Bob
    _G1: int = 0  # Shared key with Alice
    _G2: int = 0  # Shared key with Bob

    def __init__(self):
        super(SingleParty).__init__()

    # TODO add rest of the methods


# TODO you should demonstrate man-in-the-middle attack by just calling classes and their methods in correct order,
# after fullfilling the implementation(s) and adding suitable values.

# After successfull key exchange, you can finally select some data which is encrypted by Alice,
#  then decrypted by Eve, re-encrypted by Eve to pass data for Bob who finally decrypts the data

# Example use of one of the classes *without* key exchange, by just setting shared key value
al = Alice()
al._G = 123456
ciphertext = al.encrypt("Hello, world!")
print(al.decrypt(ciphertext))
