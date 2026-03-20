import pytest
from random import randint
from algorithms.key_exchange_protocol import CryptoBase, Participant


@pytest.fixture(scope="function")
def encryption_base():
    """
    Base of encryption and decryption
    """
    return CryptoBase(randint(2, 23), randint(101, 999))


@pytest.fixture(scope="function")
def alice(encryption_base):
    """
    Alice participant
    """
    return Participant("Alice", encryption_base)


@pytest.fixture(scope="function")
def bob(encryption_base):
    """
    Bob participant
    """
    return Participant("Bob", encryption_base)


def test_key_exchange(alice: Participant, bob: Participant):
    """
    Allice and Bob exchange Public Keys with each others and generate Shared Key
    """
    alice | bob
    assert alice.shared_key == bob.shared_key
    assert alice.public_key != bob.public_key
    assert alice.private_key != bob.private_key
