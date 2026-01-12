from random import randint


class CryptoBase:
    def __init__(self, public_base, public_modulus):
        self.public_base = public_base
        self.public_modulus = public_modulus

    def __repr__(self):
        return (
            f"""
Diffie–Hellman key exchange protocol
__________________________________________________
Public Base:    {self.public_base}
Public Modulus: {self.public_modulus}
__________________________________________________""")


class Participant:
    def __init__(self, name,crypto_base):
        self.name = name
        self.crypto_base = crypto_base
        self.private_key = randint(a=99, b=100000)
        self.public_key = None
        self.shared_key = None
        self.make_public_key()

    def make_public_key(self):
        self.public_key = pow(self.crypto_base.public_base, self.private_key) % self.crypto_base.public_modulus
        return self.public_key


    def make_key_hash(self, friend):
        self.shared_key = pow(friend.public_key, self.private_key) % self.crypto_base.public_modulus

    def __rshift__(self, other):
        self.make_key_hash(other)

    def __or__(self, other):
        self.make_key_hash(other)
        other.make_key_hash(self)

    def __repr__(self):
        return (
            f"""
{self.name}
__________________________________________________
Private Key: {self.private_key}
Public Key:  {self.public_key}
Shared Key:  {self.shared_key}
__________________________________________________""")
