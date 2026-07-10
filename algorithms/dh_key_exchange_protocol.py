from random import randint


class CryptoBase:
    def __init__(self, base: int, modulus: int):
        self._base = base
        self._modulus = modulus

    def __repr__(self):
        return f"""
Diffie–Hellman key exchange protocol
__________________________________________________
Public Base:    {self._base}
Public Modulus: {self._modulus}
__________________________________________________"""

    @property
    def base(self):
        return self._base

    @property
    def modulus(self):
        return self._modulus


class Participant:
    def __init__(self, name: str, crypto_base: CryptoBase):
        self._name = name
        self._crypto_base = crypto_base
        self._private_key = randint(a=99, b=100000)
        self._public_key = 0
        self._shared_key = 0
        self._make_public_key()

    def __rshift__(self, other: Participant):
        self._hash(other)

    def __or__(self, other: Participant):
        self._hash(other)
        other._hash(self)

    def __repr__(self):
        return f"""
{self._name}
__________________________________________________
Private Key: {self._private_key}
Public Key:  {self._public_key}
Shared Key:  {self._shared_key}
__________________________________________________"""

    def _make_public_key(self):
        self._public_key = pow(self._crypto_base.base, self._private_key) % self._crypto_base.modulus
        return self.public_key

    def _hash(self, other: Participant):
        self._shared_key = pow(other.public_key, self._private_key) % self._crypto_base.modulus

    @property
    def public_key(self) -> int:
        return self._public_key

    @property
    def shared_key(self):
        return self._shared_key

    @property
    def name(self):
        return self._name
