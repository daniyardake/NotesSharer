class Account:
    def __init__(self, id, login, name):
        self.id = id
        self.login = login
        self.name = name

    def __str__(self):
        return ('{}: {} ({})'.format(self.id, self.login, self.name))

    
