import pytest
from random import randint
from algorithms.dh_key_exchange_protocol import CryptoBase, Participant


@pytest.fixture(scope="class")
def encryption_base():
    """
    Encryption base
    """
    return CryptoBase(10, randint(101, 9999999999))


@pytest.fixture(scope="class")
def alice(encryption_base):
    """
    Alice participant
    """
    return Participant("Alice", encryption_base)


@pytest.fixture(scope="class")
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
