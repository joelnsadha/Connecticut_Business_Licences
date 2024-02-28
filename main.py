import psycopg2
from utils.create_tables import create_database, create_tables


if __name__ == '__main__':
    con, cur = create_database()
    print(con, cur)
    con.close()

