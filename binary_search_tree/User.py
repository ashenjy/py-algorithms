class User:
    def __init__(self, username, name, email) -> None:
        self.username = username
        self.name = name
        self.email = email

    def __str__(self):
        return "User( {} , {} , {} )".format(self.username, self.name, self.email)
