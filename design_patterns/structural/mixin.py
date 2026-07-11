import json


class JSONExportMixin:
    """
    Provides a reusable method to convert object attributes to JSON
    """

    def to_json(self) -> str:
        return json.dumps(self.__dict__, indent=2)


class Employee:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
