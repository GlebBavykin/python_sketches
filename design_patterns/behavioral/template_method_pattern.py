import tempfile
from abc import ABC, abstractmethod
from pathlib import Path


class CreateDataFile(ABC):
    def __init__(self, header: str, data: str) -> None:
        self.file_path = Path()
        self.header = header
        self.data = data

    def create_file_with_header_and_data(self) -> Path:
        """
        template method for creating file with header and data
        """
        self.setup_hook()
        self.create_file()
        self.write_header_to_file()
        self.append_data_to_file()
        self.teardown_hook()
        return self.file_path

    def create_file(self) -> None:
        with tempfile.NamedTemporaryFile(delete_on_close=False) as tmp:
            self.file_path = Path(tmp.name)

    @abstractmethod
    def write_header_to_file(self) -> None: ...

    @abstractmethod
    def append_data_to_file(self) -> None: ...

    def setup_hook(self) -> None:
        pass

    def teardown_hook(self) -> None:
        pass


class StringDataFile(CreateDataFile):
    def write_header_to_file(self) -> None:
        self.file_path.write_text(self.header)

    def append_data_to_file(self) -> None:
        with self.file_path.open("a", encoding="utf-8") as file:
            file.write(self.data)

    def setup_hook(self) -> None:
        if self.file_path.is_file():
            raise FileExistsError

    def teardown_hook(self) -> None:
        if not self.file_path.exists():
            raise FileNotFoundError
