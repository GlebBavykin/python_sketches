import pytest
from _pytest.logging import LogCaptureFixture

from design_patterns.behavioral.strategy_pattern import AuthContext, GuestAuth, UserAuth


@pytest.fixture(scope="class")
def auth() -> AuthContext:
    """
    AuthContext instance
    """
    return AuthContext()


@pytest.mark.parametrize(
    "user, outcome",
    [
        ("guest", "Guest authorization"),
        ("user", "Regular user Authorization"),
    ],
)
def test_strategy_pattern(user: str, auth: AuthContext, caplog: LogCaptureFixture, outcome: str):
    """
    Test strategy pattern
    """

    if user == "guest":
        auth.set_strategy(GuestAuth())
    if user == "user":
        auth.set_strategy(UserAuth())
    auth.login(user=user)
    assert outcome in caplog.text
