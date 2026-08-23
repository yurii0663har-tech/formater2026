# PythonFormatterPro

PythonFormatterPro is a Python source-code formatter based on the Python AST.

## Features

- AST-based Python code formatting
- Configurable indentation
- Removal of trailing spaces
- Removal of excessive empty lines
- CLI formatting
- In-place formatting with `--write`
- Formatting checks with `--check`
- Error handling for missing files and invalid Python syntax

## Usage

Format a file and print the result:

    python cli.py example.py

Format a file in place:

    python cli.py example.py --write

Check whether a file is formatted:

    python cli.py example.py --check

The `--check` command returns:

- `0` if the file is already formatted
- `1` if formatting is required or an error occurs

## Testing

Run the complete test suite:

    python -m unittest

Run CLI tests only:

    python -m unittest tests.test_cli -v

## Project Structure

    PythonFormatterPro/
    ├── core/
    │   ├── config.py
    │   ├── engine.py
    │   ├── formatter.py
    │   ├── parser.py
    │   └── pipeline.py
    ├── tests/
    │   ├── test_engine.py
    │   └── test_cli.py
    ├── cli.py
    ├── .gitignore
    └── README.md

## Development

The formatter pipeline follows this flow:

    Python source
         ↓
       Parser
         ↓
    FormatterEngine
         ↓
    PythonFormatter
         ↓
        Rules
         ↓
    Formatted source

## License

This project is currently for development and educational purposes.
