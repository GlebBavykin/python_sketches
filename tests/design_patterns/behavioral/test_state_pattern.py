import pytest

from design_patterns.behavioral.state import (
    Document,
    DraftState,
    ModerationState,
    PublishedState,
)


@pytest.fixture(scope="function")
def document() -> Document:
    """
    Document instance
    """
    return Document(name="Driving License")


def test_strategy_pattern_1(document: Document):
    """
    Test state pattern: go to DraftState
    """
    assert isinstance(document.state, DraftState)
    assert "Document Driving License is drafting" in str(document.state)


def test_strategy_pattern_2(document: Document):
    """
    Test state pattern: go to ModerationState
    """
    document.publish()
    assert isinstance(document.state, ModerationState)
    assert "Document Driving License is moderating" in str(document.state)


def test_strategy_pattern_3(document: Document):
    """
    Test state pattern: go to PublishedState
    """
    document.publish()
    document.publish()
    assert isinstance(document.state, PublishedState)
    assert "Document Driving License is published" in str(document.state)
