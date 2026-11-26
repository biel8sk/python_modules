from importlib.metadata import version, PackageNotFoundError

def check_install(package_name):
    try:
        installed_version = version(package_name)
        print(f"[OK] {package_name} ({installed_version})")
        return True
    except PackageNotFoundError:
        print(f"[ERROR] {package_name} is missing")
        return False

def main():
    print("\n REAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:\n")
    try:
        import numpy, pandas
        is_install1 = check_install("numpy")
        is_install2 = check_install("pandas")
        print("pip vs poetry")
        print('''
        requirements.txt declares what to install; pip resolves it at install time.
        pyproject.toml declares the same constraints, and Poetry pins the resolved
        versions in poetry.lock so every install is identical
        ''')
        if (is_install1 and is_install2):
            print("All reagents present and accounted for.")
    except ImportError:
        print("Numpy e pandas não instalado!!")
        print("Para instalar execute: ")
        print("pip install -r requirements.txt # Utilizando o pip")
        print("poetry install # Utilizanod o poetry")


if __name__ == "__main__":
    main()