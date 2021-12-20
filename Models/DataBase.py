import sqlite3


class DataBase():
    def __init__(self, dbname):
        self.dbname = f"{dbname}.db"
        self.connection = sqlite3.connect(self.dbname)
        self.cursor = self.connection.cursor()
        self.requete = ""
        self.results = []
        self.execution = ""

    def execute(self):
        self.execution = self.cursor.execute(str(self.requete))
        return self

    def commit(self):
        self.connection.commit()
        return self

    def fetchOne(self):
        result = self.execution.fetchone()
        self.results = result
        return

    def fetchAll(self):
        result = self.execution.fetchall()
        self.results = result
        return self
