import pytest

from design_patterns.behavioral.template_method import StringDataFile


@pytest.mark.parametrize(
    "header, data",
    [("This is a header form a file\n", "This is data form a file\n")],
)
def test_template_method_pattern(header: str, data: str) -> None:
    """
    Test template method pattern
    """
    data_file = StringDataFile(header, data)
    file_path = data_file.create_file_with_header_and_data()
    content = file_path.read_text(encoding="utf-8")
    assert header in content
    assert data in content
