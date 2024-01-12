class query():
    def __init__(self) -> None:
        self.__prepare()

    def __prepare(self):
        import pandas
        self.pandas=pandas

    def __connect(self):
        import pandas
        import sqlite3
        self.banco=sqlite3.connect('./comercial_database.db')
        self.cursor=self.banco.cursor() 
        print('connected')
    def __disconnect(self):
        self.banco.close()
        print('desconnected')

    def show_tables(self):
        self.__connect()

        command=""" SELECT name FROM sqlite_schema"""
        self.cursor.execute(command)
        response=self.cursor.fetchall()
        response=self.pandas.DataFrame(response)
        self.__disconnect()
        return response

    def show_tables_columns(self,table='PRODUCTS'):
        self.__connect()
        command=f'PRAGMA table_info({table})'
        self.cursor.execute(command)
        response=self.cursor.fetchall()
        self.__disconnect()
        return response

    def execute(self,command=''):
        self.__connect()
        self.cursor.execute(command)
        response=self.cursor.fetchall()
        response=self.pandas.DataFrame(response)
        self.__disconnect()
        return response