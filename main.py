from pathlib import Path

ENTRY = "My boss asked for volunteers and read my name off a list he was already holding."
OUTPUT_PATH = Path("/output/entry.txt")


def validate_entry(text: str) -> None:
    if not 1 <= len(text) <= 200:
        raise ValueError("Entry must contain between 1 and 200 characters.")
    if not text.strip():
        raise ValueError("Entry must not be whitespace-only.")
    if "\n" in text or "\r" in text:
        raise ValueError("Entry must be a single line.")
    text.encode("utf-8")


def main() -> None:
    validate_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")

    written_bytes = OUTPUT_PATH.read_bytes()
    written_text = written_bytes.decode("utf-8")
    validate_entry(written_text)
    if written_text != ENTRY:
        raise ValueError("Read-back text does not match the entry text.")
    if written_bytes != ENTRY.encode("utf-8"):
        raise ValueError("Read-back bytes do not match the entry bytes.")


if __name__ == "__main__":
    main()
