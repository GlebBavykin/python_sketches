# Python Sketches

В этом проекте собраны алгоритмы, структуры данных, паттерны проектирования реализованные на python3.
Код был написан с использованием TDD (Test-Driven Development) методики. На каждую идею написан автотест 
в папке tests.

- для установки зависимостей на Ubuntu 26.04 следует выполнить:
    ```bash
    
    curl -LsSf https://astral.sh/uv/install.sh | sh
    uv sync
    source .venv/bin/activate
    ```

- для установки зависимостей на Windows 11 следует выполнить:
    ```powershell
    
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex
    uv sync
    .\.venv\Scripts\activate.ps1 
    ```

- для запуска автотестов следует выполнить:
  ````bash
  uv run pytest -n auto
  ````
