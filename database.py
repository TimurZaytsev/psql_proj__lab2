import psycopg2 as ps
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class DatabasePy(object):
    def __init__(self):
        self.db_name = 'testing'
        self.user = 'postgres'
        self.password = 'baka'
        self.host = '127.0.0.1'

    def create_db(self, name):
        connection = ps.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database="postgres"
        )

        self.db_name = name

        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        with connection.cursor() as cur:
            cur.execute(sql.SQL("CREATE DATABASE {}").format(
                sql.Identifier(self.db_name))
            )

        if connection:
            connection.close()

    def test_1_step(self):
        try:
            connection = ps.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db_name
            )

            with connection.cursor() as cur:
                cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
                cur.execute(f"INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))
                cur.execute("SELECT * FROM test;")
                print(cur.fetchone())

                # connection.commit()
                print("operation is done")
        except Exception as ex:
            print("[INFO] Error while working with PSQL", ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] PSQL connection closed")

    def __del__(self):
        del self

    def drop_db(self):
        connection = ps.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database="postgres"
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cur = connection.cursor()

        cur.execute(sql.SQL(f"DROP DATABASE {self.db_name}"))

        if cur:
            cur.close()
        if connection:
            connection.close()

        print("database was dropped")
        self.__del__()


