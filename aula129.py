class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        return msg


# c1 = Connection()
# c1.set_user('Victor')
# c1.set_password('123456')
c1 = Connection.create_with_auth('Victor', '123456')
print(c1.user)
print(c1.password)
print(Connection.log('Usuário logado com sucesso!'))