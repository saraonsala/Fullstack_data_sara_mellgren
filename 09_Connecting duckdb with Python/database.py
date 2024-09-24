import duckdb

class Database:
    def __init__(self):
        self.connection = duckdb.connect(':memory:')
        self.cursor = self.connection.cursor()

    def execute(self, query):
        return self.cursor.execute(query)

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()