# Python Sketches

В настоящем проекте собраны [алгоритмы](./algorithms/), [структуры данных](./data_structures/), [паттерны проектирования](./design_patternss/) реализованные на `python3`.
Код был написан с использованием TDD (Test-Driven Development) методологии. На каждую идею написан автотест 
в папке [tests](./tests/).

Чтобы развернуть окружение через [uv](https://docs.astral.sh/uv/getting-started/installation/), следует выполнить:

  - для Ubuntu 26.04:
      ```bash
      
      curl -LsSf https://astral.sh/uv/install.sh | sh
      uv sync
      source .venv/bin/activate
      ```

  - для Windows 11:
      ```powershell
    
      irm https://astral.sh/uv/install.ps1 | iex
      uv sync
      .\.venv\Scripts\activate.ps1 
      ```

Чтобы запустить тестовый прогон на [pytest](https://docs.pytest.org/en/stable/), следует выполнить:

  ````bash
  pytest -n auto
  ````
