import getpass

class Pass:

    def __init__(self):
        self.password = getpass.getpass("Enter password: ")

    def __str__(self):
        return self.password