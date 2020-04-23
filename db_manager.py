import sqlite3


class DbManager:
    __CREATE_TABLE = '''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            link TEXT NOT NULL
        );
    '''

    __FIND_TITLE_POST = '''
        SELECT *
        FROM messages
        WHERE title = '{title}';
    '''

    __INSERT_NEW_POST = '''
        INSERT INTO messages (
            title,
            link
        ) VALUES (
            '{title}',
            '{link}'
        );
    '''

    def __init__(self, db_name):
        self.db_name = db_name
        self.__connector = None
        self.__cursor = None

    def connect(self):
        self.__connector = sqlite3.connect(self.db_name)
        self.__cursor = self.__connector.cursor()

    def find_post(self, title):
        title = title.replace("'", '"')
        result = self.__cursor.execute(self.__FIND_TITLE_POST.format(title=title))
        return result.fetchall()

    def add_new_post(self, title, link):
        title = title.replace("'", '"')
        self.__cursor.execute(self.__INSERT_NEW_POST.format(
            title=title,
            link=link
        ))

        self.__connector.commit()

    def create_table(self, table_name='messages'):
        self.__cursor.execute(self.__CREATE_TABLE.format(table_name=table_name))

    def close(self):
        self.__cursor.close()
        self.__connector.close()


if __name__ == '__main__':
    db = DbManager('test.db')
    db.connect()
    db.create_table()
    db.close()
