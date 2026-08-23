import sys

from core.pipeline import FormatterPipeline


def main():
    if len(sys.argv) not in (2, 3):
        print("Usage: python cli.py <file.py> [--write|--check]")
        sys.exit(1)

    filename = sys.argv[1]
    write = len(sys.argv) == 3 and sys.argv[2] == "--write"
    check = len(sys.argv) == 3 and sys.argv[2] == "--check"

    if len(sys.argv) == 3 and sys.argv[2] not in ("--write", "--check"):
        print("Unknown option. Use --write or --check.")
        sys.exit(1)

    try:
        with open(filename, "r", encoding="utf-8") as f:
            code = f.read()
    except FileNotFoundError:
        print(f"File not found: {filename}", file=sys.stderr)
        sys.exit(1)

    try:
        formatter = FormatterPipeline()
        formatted = formatter.format(code)
    except SyntaxError as error:
        print(f"Syntax error: {error}", file=sys.stderr)
        sys.exit(1)

    if check:
        if formatted.rstrip("\n") == code.rstrip("\n"):
            sys.exit(0)

        print(f"File is not formatted: {filename}", file=sys.stderr)
        sys.exit(1)

    if write:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(formatted)
    else:
        print(formatted)


if __name__ == "__main__":
    main()