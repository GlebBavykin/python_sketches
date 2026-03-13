# Python Sketches

В этом проекте собраны алгоритмы, структуры данных, паттерны проектирования реализованные на python3.
Код был написан и с использованием TDD (Test-Driven Development) методики. На каждую идею написан автотест 
в папке tests.

- для установки зависимостей следует выполнить:
    ```bash
    
    curl -LsSf https://astral.sh/uv/install.sh | sh
    uv venv
    source .venv/bin/activate
    uv sync
    ```
- для запуска автотестов следует выполнить:
  ````bash
  uv run pytest
  ````
