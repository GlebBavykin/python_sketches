import pytest
from _pytest.logging import LogCaptureFixture

from design_patterns.behavioral.strategy import (
    AuthContext,
    AuthStrategy,
    GuestAuth,
    UserAuth,
)


@pytest.fixture(scope="class")
def auth() -> AuthContext:
    """
    AuthContext instance
    """
    return AuthContext()


@pytest.mark.parametrize(
    "strategy, outcome",
    [
        (GuestAuth(), "Guest authorization"),
        (UserAuth(), "Regular user Authorization"),
    ],
)
def test_strategy_pattern(
    strategy: AuthStrategy, auth: AuthContext, caplog: LogCaptureFixture, outcome: str
):
    """
    Test strategy pattern
    """
    auth.set_strategy(strategy)
    auth.login()
    assert outcome in caplog.text
