import pytest
from _pytest.logging import LogCaptureFixture

from design_patterns.behavioral.chain_of_responsibility import (
    CheckEmail,
    CheckIsActive,
    CheckName,
    UserRequest,
)


@pytest.fixture(scope="function")
def check_name() -> CheckName:
    """
    CheckName instance
    """
    return CheckName()


@pytest.fixture(scope="function")
def check_email(check_name: CheckName) -> CheckEmail:
    """
    CheckEmail instance
    """
    return CheckEmail(next_handler=check_name)


@pytest.fixture(scope="function")
def check_is_active(check_email: CheckEmail) -> CheckIsActive:
    """
    CheckIsActive instance
    """
    return CheckIsActive(next_handler=check_email)


@pytest.mark.parametrize(
    "user_request, outcomes",
    [
        (UserRequest(username="John"), ["John"]),
        (UserRequest(email="john@email.com"), ["john@email.com"]),
        (UserRequest(is_active=True), ["active"]),
        (UserRequest("John", "john@email.com", True), ["active", "john@email.com", "John"]),
    ],
)
def test_chain_of_responsibility_pattern(
    user_request: UserRequest, outcomes: list[str], check_is_active: CheckIsActive, caplog: LogCaptureFixture
) -> None:
    """
    Check chain of responsibility pattern: user request go through all chain print and capture logs
    """
    check_is_active.execute(user_request)
    assert all(outcome in caplog.text for outcome in outcomes)
