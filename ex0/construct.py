import sys, os, site


def get_status() -> tuple[bool, str]:
    if sys.base_prefix != sys.prefix:
        return (True, 'The laboratory is sealed')
    return (False, 'You are working in the open')

def main():
    status = get_status()
    message_success = "\nSUCCESS: You are working in an isolated" \
    "environment!\n" \
    "Safe to install reagents without affecting the global system.\n" \
    "Reagent installation path:\n" 
    message_outside_venv = "\nWARNING: You are in the global environment!\n" \
    "Every reagent you install here leaks into the whole system.\n\n" \
    "To seal the laboratory, run:\n\n" \
    "python3 -m venv lab_env\n" \
    "source lab_env/bin/activate # On Unix\n" \
    "lab_env/Scripts/activate # On Windows\n\n" \
    "Then run this program again" 
    print(f'LABORATORY STATUS: {status[1]}\n\n')
    print(f'Current Python: {sys.executable}')
    if (status[0]):
        print(f'Virtual Environment: {os.path.basename(sys.prefix)}')
        print(f'Environment Path: {sys.prefix}')
        print(message_success)
        for path in site.getsitepackages():
            print(path, end="\n\n")
    else:
        print('Virtual Environment: None detected')
        print(message_outside_venv)
    

if __name__ == '__main__':
    main()