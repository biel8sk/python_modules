from typing import TextIO as txIO
import sys

def main():
    args = sys.argv[1:]
    if (len(args) != 1):
        print("Usage: ft_archive_creation.py <file>")
        return
    file_name = args[0]
    file_data = []
    print(f"Accessing file {file_name}")
    try:
        file = open(file_name, 'r', encoding="utf-8")
        print("---\n\n")
        for l in tp.IO.readlines(file):
            file_data.append(l.strip())
            print(l, end='')
        print("\n\n---")
        print(f"File {file_name} closed.\n")
        print(f"Transform data:")
        file_data = [l+'#\n' for l in file_data]
        print("---\n\n")
        print(*file_data)
        print("\n\n---")
        new_file: str = input("Enter new file name (or empty): ")
        if (not new_file):
            print("Data not saved.")
            return
        with open(new_file, 'w', encoding='utf-8') as new:
            print(f'Savin data to {new_file}')
            for d in file_data:
                new.write(d)
        print("Data saved")
    except IOError as ex:
        print(f"{ex.strerror} Error opening file {ex.filename}: {ex}")


if __name__ == "__main__":
    main();
