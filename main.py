import database as db


if __name__ == '__main__':
    database = db.DatabasePy()
    database.create_db("testing")
    database.test_1_step()
    database.drop_db()
