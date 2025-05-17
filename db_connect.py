import psycopg2
class DBconnect:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

        #соединение
        self.connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
        )

        self.cursor = self.connection.cursor()
        self.connection.autocommit = True # чтобы не прописывать каждый раз commit

    # запрос на изменение данных в бд (query - запрос, args - список агрументов)
    def post(self, query, args=()):
        self.cursor.execute(query, args)

