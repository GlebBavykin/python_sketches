import pytest

from api.mock_service import User
from design_patterns.behavioral.strategy_pattern import (AuthContext,
                                                         GuestAuth, UserAuth)


@pytest.fixture(scope="class")
def auth() -> AuthContext:
    """
    AuthContext instance
    """
    return AuthContext()


@pytest.mark.parametrize(
    "user",
    [
        User(nickname="John", is_guest=False),
        User(nickname="Doe", is_guest=True),
    ],
)
def test_strategy_pattern(user, auth):
    """
    Test strategy pattern
    """

    if user.is_guest:
        auth.set_strategy(GuestAuth())
    else:
        auth.set_strategy(UserAuth())

    try:
        auth.login(user, [{"Content-type": "application/json"}])
    except AttributeError:
        pytest.fail("User auth failed")

    assert user.session_id is not None
    assert user.user_id is not None
