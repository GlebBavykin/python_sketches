import json

import pytest

from design_patterns.structural.mixin import Employee, JSONExportMixin


class ExportableEmployee(JSONExportMixin, Employee):
    pass


@pytest.fixture(scope="class")
def employee() -> ExportableEmployee:
    """
    Employee instance
    """
    return ExportableEmployee("Gleb", "QA")


@pytest.mark.parametrize(
    "outcome",
    [
        json.dumps(
            {
                "name": "Gleb",
                "role": "QA",
            },
            indent=2,
        )
    ],
)
def test_mixin_feature(employee: ExportableEmployee, outcome) -> None:
    """
    Check mixin  feature
    """
    assert employee.to_json() == outcome
