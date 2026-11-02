import sys


def main():
    args = sys.argv[1:]
    if (len(args) != 1):
        sys.stderr.write("[STDERR] Usage: ft_archive_creation.py <file>")
        return
    file_name = args[0]
    file_data = []
    print(f"Accessing file {file_name}")
    try:
        file = open(file_name, 'r', encoding="utf-8")
        print("---\n\n")
        for line in file.readlines():
            file_data.append(line.strip())
            print(line, end='')
        print("\n\n---")
        print(f"File {file_name} closed.\n")
        print("Transform data:")
        file_data = [line + '#\n' for line in file_data]
        print("---\n\n")
        for data in file_data:
            print(data, end='')
        print("\n\n---")
        new_file_name = sys.stdin.write("Enter new file name (or empty): ")
        if (not new_file_name):
            print("Data not saved.")
            return
        new_file = open(new_file_name, 'w', encoding='utf-8')
        print(f'Savin data to {new_file_name}')
        for line in file_data:
            new_file.write(line)
        print("Data saved")
    except FileNotFoundError as ex:
        sys.stderr.write(f"[STDERR] Error opening file {ex.filename}: {ex}\n")


if __name__ == "__main__":
    main()
