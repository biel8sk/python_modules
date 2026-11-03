def secure_archive(file_name: str, mode=None, content=None):
    try:
        if (mode == 'w'):
            with open(file_name, mode) as file:
                file.write(content)
                return (True, 'Content successfully written to file')
        with open(file_name, mode) as file:
            return (True, file.read())
    except Exception as ex:
        return (False, ex.__str__())


def main():
    print('=== Cyber Archives Security ===')
    file_names = ['not_exist', 'forbiden.txt', 'arguivo.txt', 'new_file']
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive(file_names[0], 'r'), end='\n\n')
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive(file_names[1], 'r'), end='\n\n')
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive(file_names[2], 'r'), end='\n\n')
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive(file_names[3], 'w', "Novo conteudo pro arquivo"))


if __name__ == '__main__':
    main()
