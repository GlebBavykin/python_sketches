import pytest
from _pytest.logging import LogCaptureFixture
from requests import Session

from design_patterns.structural.proxy import SessionWithLogging


@pytest.fixture(scope="class")
def session() -> Session:
    """
    Raw requests session
    """
    return Session()


@pytest.fixture(scope="class")
def session_with_logging(session: Session) -> SessionWithLogging:
    """
    Proxy Session class with logging features
    """
    return SessionWithLogging(session)


def test_check_logging_feature(session_with_logging: SessionWithLogging, caplog: LogCaptureFixture) -> None:
    """
    Check logging feature for session request
    """
    session_with_logging.get("https://ya.ru/")
    assert "GET https://ya.ru/ with params: None and kwargs: {}" in caplog.text
