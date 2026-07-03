import pytest

from design_patterns.behavioral.template_method_pattern import StringDataFile


@pytest.fixture(scope="function")
def data_file() -> StringDataFile:
    """
    StringDataFile instance
    """
    return


@pytest.mark.parametrize(
    "header, data",
    [("This is a header form a file\n", "This is data form a file\n")],
)
def test_template_method_pattern(header: str, data: str, data_file: StringDataFile) -> None:
    """
    Test template method pattern
    """
    data_file = StringDataFile(header, data)
    file_path = data_file.template_method()
    content = file_path.read_text(encoding="utf-8")
    assert header in content
    assert data in content
