def main():
    """Ask user for a valid password and print stars to match length."""
    password = get_password()
    print_asterisks(password)


def get_password():
    """Prompt the user until a valid password is entered."""
    MIN_LENGTH = 8
    password = input("Enter a password: ")
    while len(password) < MIN_LENGTH:
        print("Password too short!")
        password = input("Enter a password: ")
    return password


def print_asterisks(password):
    """Print asterisks to match the length of the password."""
    print("*" * len(password))


main()