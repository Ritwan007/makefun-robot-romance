"""Robot Romance entry: one-line pickup line for AI.

Writes the chosen line to /output/entry.txt and nothing else.
"""

LINE = "I must be a prompt, because you complete me."


def main():
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"line is {len(LINE)} chars, must be 1-200")
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
