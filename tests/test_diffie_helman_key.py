import pytest
from random import randint
from diffie_hellman.key_exchange_protocol import CryptoBase, Participant



@pytest.fixture(scope="function")
def encryption_base():
    """
        Base of encryption and decryption
    """
    return CryptoBase(randint(2,23), randint(101, 999))

@pytest.fixture(scope="function")
def Alice(encryption_base):
    """
        Alice exchange participant
    """
    return Participant("Alice", encryption_base)


@pytest.fixture(scope="function")
def Bob(encryption_base):
    """
        Bob exchange participant
    """
    return Participant("Bob", encryption_base)


def test_key_exchange(Alice, Bob, encryption_base):
    """
    Allice and Bob exchange Public Keys with each others and generate Shared Key
    """
    print(encryption_base)
    Alice | Bob
    print(Alice)
    print(Bob)
    assert Alice.shared_key == Bob.shared_key
    assert Alice.public_key != Bob.public_key
    assert Alice.private_key != Bob.private_key
