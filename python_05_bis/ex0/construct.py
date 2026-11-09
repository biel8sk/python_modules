import sys, os


def get_status() -> tuple[bool, str]:
    if sys.base_prefix != sys.prefix:
        return (True, 'The laboratory is sealed')
    return (False, 'You are working in the open')

def main():
    status = get_status()
    message_success = '''
    SUCCESS: You are working in an isolated environment!
    Safe to install reagents without affecting the global system.
    
    Reagent installation path:
    
    /path/to/lab_env/lib/python3.11/site-package
    '''
    message_outside_venv = '''
    WARNING: You are in the global environment!
    Every reagent you install here leaks into the whole system.
    
    To seal the laboratory, run:
    python3 -m venv lab_env
    source lab_env/bin/activate # On Unix
    lab_env\\Scripts\activate # On Windows
    
    Then run this program again
    '''
    print(f'LABORATORY STATUS: {status[1]}\n\n')
    print(f'Current Python: {sys.executable}')
    if (status[0]):
        print(f'Virtual Environment: {os.path.basename(sys.prefix)}')
        print(f'Environment Path: {sys.prefix}')
        print(message_success)
    else:
        print('Virtual Environment: None detected')
        print(message_outside_venv)
    

if __name__ == '__main__':
    main()