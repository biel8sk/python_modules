from typing import TextIO as txIO
import sys


def main():
    args = sys.argv[1:]
    if (len(args) != 1):
        print("Usage: ft_ancient_text.py <file>")
        return
    file_name = args[0]
    print(f"Accessing file {file_name}")
    try:
        file: txIO= open(file_name, "r", encoding="utf-8")
        print("---\n\n")
        print(file.read())
        file.close()
        print("\n\n---")
        print(f"File {file_name} closed.")
    except Exception as ex:
        print(f"Error opening file {args}: {ex}")


if __name__ == "__main__":
    main();
