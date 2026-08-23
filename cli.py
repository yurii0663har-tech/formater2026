import sys

from core.pipeline import FormatterPipeline


def main():
    if len(sys.argv) not in (2, 3):
        print("Usage: python cli.py <file.py> [--write]")
        sys.exit(1)

    filename = sys.argv[1]
    write = len(sys.argv) == 3 and sys.argv[2] == "--write"

    if len(sys.argv) == 3 and sys.argv[2] != "--write":
        print("Unknown option. Use --write.")
        sys.exit(1)

    try:
        with open(filename, "r", encoding="utf-8") as f:
            code = f.read()
    except FileNotFoundError:
        print(f"File not found: {filename}", file=sys.stderr)
        sys.exit(1)

    formatter = FormatterPipeline()

    try:
        formatted = formatter.format(code)
    except SyntaxError as e:
        print(f"Syntax error: {e}", file=sys.stderr)
        sys.exit(1)

    if write:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(formatted)
    else:
        print(formatted)


if __name__ == "__main__":
    main()